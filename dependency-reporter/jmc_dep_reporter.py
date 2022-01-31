#!/usr/bin/python3

import os, re, sys

dict = {
    # <dependency> : <source>
    # e.g., tycho-2.5.0.pom : https://repo.maven.apache.org/maven2/org/eclipse/tycho/tycho/2.5.0/tycho-2.5.0.pom
}

def initialize_dependency_dictionary(tree):
    with open(tree, 'r') as f:
        parse_tree(f.read())
    f.close()

# Given a tree output, find all of the *.jar and *.pom files and place them in the dict
def parse_tree(tree):
    deps = re.findall(r"\b(.*(\.jar|\.pom|\.zip))\b(?!\.sha1)", tree)
    for dep in deps:
        dict[dep[0]] = ''

def scrape_dependencies_from_logs(logs):
    for log in logs:
        with open(log, 'r') as f:
            parse_log(f.read())
        f.close()

# Given a Maven log, find each downloaded dependency and add it's url to the dict
def parse_log(log):
    scrape_maven_central_deps(log)
    scrape_eclipse_osgi_deps(log)
    scrape_jmc_core_snapshots(log)
    # replace instances of local p2: http://localhost:8080/site/plugins/

def scrape_maven_central_deps(log):
    deps = re.findall(r"Downloaded.+:\s(http.*\/(.*)(\.pom|\.jar))", log)
    for dep in deps:
        string, url = dep[1] + dep[2], dep[0]
        if string in dict and dict[string] == '':
            dict[string] = url

def scrape_eclipse_osgi_deps(log):
    deps = re.findall(r"Fetching\s(.*?(.jar|.pom|.pack.gz)?)\s.*(http.*?)\s", log)
    for dep in deps:
        string, url = dep[0], dep[2]
        if string.startswith('org.w3c.dom.events'):
            # the underscore/hyphen strategy is reversed for this jar
            i = string.find('_')
            string = string[:i] + '-' + string[i+1:]
        else:
            # the last instance of an underscore needs to be brought up to a hyphen
            i = string.rfind('_')
            string = string[:i] + '-' + string[i+1:]

        # handle extensions, or lackthereof
        if dep[1] == '.pack.gz':
            i = string.find(dep[1])
            string = string[:i]
        elif dep[1] == '':
            string = string + '.jar'

        # add it to the dictionary
        if string in dict and dict[string] == '':
            dict[string] = url

def scrape_jmc_core_snapshots(log):
    snapshots = re.findall(r"Installing\s.+\/(.*-SNAPSHOT.*?(.jar|.pom))", log)
    for snapshot in snapshots:
        dict[snapshot[0]] = 'locally built jmc core libaries'

# Whatever is left unresolved at this point is provided by the tycho-bundles-external zips.
# In the log of the m2 tree, the jars will be listed directly above the *.zip file that provides them.
# The idea here is to create a list of all the tycho-bundles-external provided
# jars (and the name of the zip itself), and then iterate through the list backwards
# such that we'll first hit the zip (and resolve it's url), and then all entries until the next
# zip will be all the jars provided by that instance of tycho-bundles-external. 
def resolve_tycho_bundles_external_plugins(logs):
    tycho_bundles_external = []
    for item in dict.items():
        if item[1] == '':
            tycho_bundles_external.append(item[0])

    i = len(tycho_bundles_external) - 1
    url = ''
    while i >= 0:
        # locate the first .zip (which *should* be the last element in the list)
        if tycho_bundles_external[i].endswith('.zip'):
            # find the log file it was downloaded in
            for log in logs:
                with open(log, 'r') as f:
                    line = re.findall(r"Downloaded.+\s(http.*\/(%s))" % tycho_bundles_external[i], f.read())
                    if len(line) == 1:
                        url = line[0][0]
                        break
                f.close()
        dict[tycho_bundles_external[i]] = url
        i = i - 1

# In the mvn build logs some dependencies resolve to http://localhost:8080/site/plugins/, so there's
# a need to go back into the files and find where the jars were downloaded from when setting up the local p2 repo
def resolve_local_p2_jars(logs):
    # this dict will use the modified jar name as a key, so it can be easily accessed in the subsequent for loop
    # the values will be the original names, so that the main dict can be updated quickly
    p2_jars = {}

    # each of these have different patterns for how they're resolved
    # org.eclipse.jetty: splice on period before jetty, and raise period after jetty to a hyphen
    # - e.g., org.jetty.xml-10.0.5.jar -> jetty-xml-10.0.5.jar
    # org.objectweb.asm: splice on period before asm, but then the subsequent periods are raised to hyphens, and last digit is removed
    # - e.g., org.objectweb.asm.tree-9.2.0.jar -> asm-tree-9.2.jar
    # the rest: splice on the last period before package name
    # - e.g., org.lz4.lz4-java-1.8.0.jar -> lz4-java-1.8.0.jar
    for item in dict.items():
        if dict[item[0]] == 'http://localhost:8080/site/plugins/':
            # line = re.findall(r"Downloaded.*?http.*\/(.*.jar)\s", item[0])
            dep = item[0].split('.', 2)[2]
            if 'jakarta' in dep:
                dep = dep.split('.', 1)[1]
            elif dep.startswith('asm'):
                dep = re.split('\.\d\.jar', dep)[0] + '.jar'
                if not re.findall(r"asm-\d", dep):
                    dep = dep.replace('.', '-', 1)
                # asm.tree.analysis will need the extra .tree to be removed; it resolves to asm-analysis-\d.\d.jar
                if '-tree.' in dep:
                    dep = dep.replace('tree.', '', 1)
            elif dep.startswith('jetty'):
                tmp = re.findall('(.*)(-[\d\.]+?\.jar)', dep)[0]
                dep = tmp[0].replace('.', '-') + tmp[1]
                if 'websocket' in dep:
                    # the websocket jars are all over the place..
                    # they either become websocket-jetty-.*-\d.\d.\d.jar or 
                    dep = dep.replace('jetty-', '')
                    # there are a couple of extra special cases here. in particular, these mappings:
                    # websocket-api-1.1.2.jar -> jetty-javax-websocket-api-1.1.2.jar
                    # websocket-api-10.0.5.jar -> websocket-jetty-api-10.0.5.jar
                    # websocket-common-10.0.5.jar -> websocket-jetty-common-10.0.5.jar
                    # websocket-server-10.0.5.jar -> websocket-jetty-server-10.0.5.jar
                    if re.findall(r"websocket\-(common|api|server)\-\d+", dep):
                        if re.findall(r".*\-\d\.\d\.\d\.jar", dep):
                            dep = 'jetty-javax-' + dep
                        else:
                            dep = dep.replace('websocket-', 'websocket-jetty-')
            p2_jars[dep] = item[0]

    for jar in p2_jars.items():
        for log in logs:
            with open(log, 'r') as f:
                line = re.findall(r"Downloaded.+\s(http.*\/%s)" % jar[0], f.read())
                if len(line) == 1:
                    dict[jar[1]] = line[0]
                    break

def write_report():
    with open(os.getcwd() + '/report.csv', 'w') as f:
        [f.write('{0},{1}\n'.format(key, value)) for key, value in dict.items()]
    f.close()

def main(argv):
    initialize_dependency_dictionary(argv.pop(0))
    scrape_dependencies_from_logs(argv)
    resolve_tycho_bundles_external_plugins(argv)
    resolve_local_p2_jars(argv)
    write_report()

if __name__ == "__main__":
    # first file in *must* be the tree file, and the rest are build logs.
    # The logs required would be:
    # - mvn p2:site from releng/third-party
    # - mvn jetty:run from releng/third-party
    # - mvn clean install for jmc core
    # - mvn package for jmc
    if len(sys.argv) > 3:    
        main(sys.argv[1:])
    else:
        print('Whoops! you did not supply the required files needed for this script.')
        print('The first argv must be the output of the tree command on the local m2 repository.')
        print('The subsequent argvs (~4 of them) should be the piped output from the mvn commands required for building jmc.')
        print('e.g., python jmc_dep_reporter.py logs/m2-tree.log logs/p2-site.log logs/jetty.log logs/core.log logs/application.log')
