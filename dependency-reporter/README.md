# JMC Dependency Reporter

This script will create a csv file (`report.csv`) that contains a list of all the dependencies required to build & run JMC, and where they were downloaded from.

Usage: `python jmc_dependency_reporter.py <m2-tree-output> <maven build logs>`

The `m2-tree-output` will be the result of running `tree` on the local m2 repository. e.g., `tree ~/.m2 > m2-tree.log`

The `maven build logs` will be the result of piping the output from the various maven commands required to build jmc. At a minimum, this would include (1) `mvn p2:site` and (2) `mvn jetty:run` from `jmc/releng/third-party`, (3) `mvn install` in jmc/core, and (4) `mvn package` in /jmc
