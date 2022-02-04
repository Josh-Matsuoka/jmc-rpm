#!/bin/bash

# TODO: remove when 8.2.0 is tagged
JMC_ROOT=$(dirname "$0")/jmc-master
JMC_TARBALL=master.zip
JMC_URL=https://github.com/openjdk/jmc/archive/refs/heads/$JMC_TARBALL

# TODO: uncomment when 8.2.0 is tagged
JMC_VERSION=8.2.0
JMC_REVDATE=20220203
# JMC_TARBALL=$JMC_VERSION-ga.tar.gz
# JMC_URL=https://github.com/openjdk/jmc/archive/refs/tags/$JMC_TARBALL

# paths
DIR=$(dirname "$0")
LOGS_DIR=$DIR/logs
M2_DIR=$DIR/repository-$JMC_VERSION-$JMC_REVDATE
# JMC_ROOT=$DIR/jmc-$JMC_VERSION-ga
JMC_CORE=$JMC_ROOT/core
JMC_THIRD_PARTY=$JMC_ROOT/releng/third-party

LOCAL_REPO_ARGLINE=-Dmaven.repo.local=./$M2_DIR

# error messages
WGET_ERROR="Something happened while retrieving the jmc repo."
P2_ERROR="Something happened while setting up the p2 repo."
JMC_CORE_BUILD_ERROR="Something happened while building jmc-core."
JMC_BUILD_ERROR="Something happened while building jmc."

# if a jmc tarball already exists, remove it prior to downloading a new one
if [ -f $JMC_TARBALL ]; then
    rm $JMC_TARBALL
fi

wget $JMC_URL || { echo $WGET_ERROR; exit 1; };
# TODO: uncomment -> tar -zxvf $JMC_TARBALL
unzip $JMC_TARBALL

# set up a directory for logs if there isn't already one
if [ ! -f $LOGS_DIR ]; then
    mkdir $LOGS_DIR
fi

# setup the p2 repository
mvn p2:site $LOCAL_REPO_ARGLINE -f $JMC_THIRD_PARTY/pom.xml > $LOGS_DIR/p2-site.log || { echo $P2_ERROR; exit 1; };

# run the jetty server in the background
mvn jetty:run $LOCAL_REPO_ARGLINE -f $JMC_THIRD_PARTY/pom.xml > $LOGS_DIR/jetty.log &
jetty_pid=$!;

# build jmc-core
mvn clean install $LOCAL_REPO_ARGLINE -f $JMC_CORE/pom.xml > $LOGS_DIR/core.log || { echo $JMC_CORE_BUILD_ERROR; kill $jetty_pid; exit 1; }

# package jmc application to fetch dependencies
mvn clean package $LOCAL_REPO_ARGLINE -f $JMC_ROOT/pom.xml > $LOGS_DIR/application.log || { echo $JMC_BUILD_ERROR; kill $jetty_pid; exit 1;}

# kill the jetty process
kill $jetty_pid;

# generate the tree file of the m2 repository, and use it with the dependency tracker script
tree $M2_DIR > $LOGS_DIR/m2-tree.log
python dependency-reporter/jmc_dep_reporter.py $LOGS_DIR/m2-tree.log $LOGS_DIR/p2-site.log $LOGS_DIR/jetty.log $LOGS_DIR/core.log $LOGS_DIR/application.log

# generate the tree file for generating the provides that should be added into the spec file
tree $JMC_ROOT/target/products/org.openjdk.jmc/linux/gtk/x86_64/JDK\ Mission\ Control/ > $LOGS_DIR/plugins.log
python dependency-reporter/generate_provides.py $LOGS_DIR/plugins.log

# create the zip to be used by the spec file
tar -czvf repository-$JMC_VERSION-$JMC_REVDATE.tar.gz $M2_DIR/ report.csv provides.txt

# if generated, remove maven workspace folder
if [ -d workspace ]; then
    rm -r $DIR/workspace
fi

# delete the local m2 dir (now zipped), the raw logs, and the temp jmc sources used to generate m2
rm -r $M2_DIR
rm -r $LOGS_DIR
rm -r $JMC_ROOT

exit 0;
