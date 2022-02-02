#!/usr/bin/python3

import re, sys

def main(file):
    tree = ''
    with open(file, 'r') as f:
        tree = f.read()
    f.close()

    plugins = re.findall(r"(.*?)_((\d{1,2}\.){3}).*jar", tree)
    with open("provides.txt", "w") as f:
        for jar in plugins:
            name = jar[0].rsplit(" ", 1)[1]
            version = jar[1][:-1]
            f.write('Provides: bundled(osgi(' + name + ')) = ' + version + '\n')
    f.close()

# Usage:
# - python generate-provides.py <tree-output>
# - where tree-output is a file, and is the result of the tree command on the target/**/JDK Mission Control folder
# - the tree file will contain all of the jars in /plugins
# - the idea will be to scrape all of the jars, and create a provides.txt file that can be copy-pasta'd into the spec file
if __name__ == "__main__":
    if len(sys.argv) == 2:    
        main(sys.argv[1])
