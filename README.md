# Offline builds of JDK Mission Control (JMC)

This repository contains a number of scripts and patches that can be used to prepare for offline Maven builds of JMC.

The idea here is to fetch (and document) all of the dependencies required to build JMC, and stash them into a zip that can be used alongside the source code to build an RPM in an offline environment. To do so, there's a couple of things we'll need to do, namely: construct a local m2 repository that can be used for builds, and audit the logs to find out exactly where they were being sourced from (Maven central, Eclipse servers, etc.).

## Generate Sources (local m2 repository)
This script (`generate-sources.sh`) is responsible for fetching and generating the sources required for local packaging of JMC. This portion will need to be run using an internet connection, because it's going to download the internet.

Usage: `bash generate-sources.sh`

Running the included script will retrieve the JMC sources from GitHub, build all JMC parts and store their dependencies in a local m2 repository, and run the dependency reporter script on the piped logs to create a report of where all the external dependencies were downloaded from. The resulting local m2 repository and dependency report will then be zipped, and can be used for offline packaging.

## Dependency Reporter
Once a local repository has been populated with jars and files from Eclipse and Maven central (& wherever dependencies are fetched from), we need a way to audit and track where each of these dependencies were sourced from. This is of course in an effort to make sure that each step of the build process uses trusted and appropriate dependencies.

See the `README.md` in `dependency-reporter` for more details.

## Generate Provides
Because we're supplying a pre-populated repository for building JMC, the jars won't be delivered through traditional yum/dnf means. As a result, we should declare which jars we're bundling with the JMC application. The jars in question are specifically the ones that end up in the target /plugins folder, which are required for the execution of JMC. Use the `generate-provides.py` script to create a `provides.txt` file, in which the contents can easily be copy-pasta'd over into the JMC spec file. The input to this script is the output of the `tree` command on the target/**/"JDK Mission Control" folder. This will generate a long list of dependencies (mainly Eclipse-related) that we're supplying.

Usage: `python generate-provides <tree-output>`

## Build JMC offline (mock)
The idea here is that the spec file can be used along with `mock` to create local rpm builds of JMC (and optionally mock install it as well). Alternatively, the srpm could be passed off to copr or some other rpm build tool, where the resulting rpm could be installed onto your system.

Create the srpm: `fedpkg srpm`

Mock build the rpm, and install afterwards: `mock -r fedora-35-x86_64 *.src.rpm --postinstall`

All-in-one: `bash generate-sources.sh && fedpkg srpm && mock -r fedora-35-x86_64 *.src.rpm --postinstall`

## Updating to the newest version of JMC

Just a checklist to follow when preparing for a new version of a JMC rpm:

- Update the tagged version in `generate-sources.sh`
- Run `generate-sources.sh`
- Update the sources file with the new local repository and jmc sources
- Add the new provides information into the jmc.spec file
- Update the version in the jmc.spec file
- Update the changelog of the jmc.spec file
- Create the new srpm
- Build it.

