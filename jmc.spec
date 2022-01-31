# Version
%global major 8
%global minor 2
%global patchlevel 0

# Revision
%global revnum 1

# SNAPSHOT version
%global revhash 14d2f6ca7a404a71c8aa8676cfd301dcab647093
%global revdate 20211026
%global releasestr %{revnum}

# TODO: uncomment me
# %global tarball_name %{major}.%{minor}.%{patchlevel}-ga.tar.gz
%global jmc_dir_name jmc-%{major}.%{minor}.%{patchlevel}-ga
# TODO: remove me
%global tarball_name master.zip

# Install jmc in /usr/lib/jmc (arch-specific and multilib exempt)
%global _jmcdir %{_prefix}/lib/%{name}

%global debug_package %{nil}

# Don't export Eclipse libraries
%global __provides_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$
%global __requires_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$

%global __requires_exclude ^osgi\\((javax|org\\.apache|org\\.eclipse|org\\.sat4j|org\\.w3c).*$
%global __provides_exclude ^osgi\\((com|javax|org\\.apache|org\\.glassfish|org\\.kxml2|org\\.sat4j|org\\.tukaani|org\\.w3c|org\\.xmlpull).*$

Name:       jmc
Version:    %{major}.%{minor}.%{patchlevel}
Release:    %{releasestr}%{?dist}
Summary:    JDK Mission Control is a profiling and diagnostics tool

License:    UPL
URL:        http://openjdk.java.net/projects/jmc/

Source0:    %{tarball_name}
Source1:    repository-%{major}.%{minor}.%{patchlevel}.tar.gz
Source2:    %{name}.desktop
Source3:    %{name}.1

# The JavaScript visualizations fetch the required JS files at build time and
# are loaded into the HTML template by the corresponding Java class. This patch
# instead inlines the scripts so there's no build-time fetching.
Patch0:     0-inline-javascript-into-templates.patch
# Remove Windows and Mac environments
Patch1:     1-remove-non-linux-environments.patch

ExclusiveArch: x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  java-11-openjdk
BuildRequires:  maven-local

Requires: gtk3
Requires: java-11-openjdk
Requires: libGLU.so.1()(64bit)
Requires: webkitgtk4

Provides: bundled(osgi(com.ibm.icu)) = 67.1.0
Provides: bundled(osgi(com.sun.activation.jakarta.activation)) = 2.0.1
Provides: bundled(osgi(com.sun.el)) = 2.2.0
Provides: bundled(osgi(com.sun.jna)) = 5.8.0
Provides: bundled(osgi(com.sun.jna.platform)) = 5.8.0
Provides: bundled(osgi(com.sun.mail.jakarta.mail)) = 2.0.1
Provides: bundled(osgi(jakarta.servlet-api)) = 4.0.0
Provides: bundled(osgi(javax.annotation)) = 1.3.5
Provides: bundled(osgi(javax.el)) = 2.2.0
Provides: bundled(osgi(javax.inject)) = 1.0.0
Provides: bundled(osgi(javax.servlet.jsp)) = 2.2.0
Provides: bundled(osgi(org.apache.aries.spifly.dynamic.bundle)) = 1.3.4
Provides: bundled(osgi(org.apache.batik.constants)) = 1.14.0
Provides: bundled(osgi(org.apache.batik.css)) = 1.14.0
Provides: bundled(osgi(org.apache.batik.i18n)) = 1.14.0
Provides: bundled(osgi(org.apache.batik.util)) = 1.14.0
Provides: bundled(osgi(org.apache.commons.codec)) = 1.14.0
Provides: bundled(osgi(org.apache.commons.io)) = 2.8.0
Provides: bundled(osgi(org.apache.commons.jxpath)) = 1.3.0
Provides: bundled(osgi(org.apache.commons.logging)) = 1.2.0
Provides: bundled(osgi(org.apache.felix.gogo.command)) = 1.1.2
Provides: bundled(osgi(org.apache.felix.gogo.runtime)) = 1.1.4
Provides: bundled(osgi(org.apache.felix.gogo.shell)) = 1.1.4
Provides: bundled(osgi(org.apache.felix.scr)) = 2.1.24
Provides: bundled(osgi(org.apache.httpcomponents.httpclient)) = 4.5.13
Provides: bundled(osgi(org.apache.httpcomponents.httpcore)) = 4.4.14
Provides: bundled(osgi(org.apache.jasper.glassfish)) = 2.2.2
Provides: bundled(osgi(org.apache.lucene.analyzers-common)) = 8.4.1
Provides: bundled(osgi(org.apache.lucene.analyzers-smartcn)) = 8.4.1
Provides: bundled(osgi(org.apache.lucene.core)) = 8.4.1
Provides: bundled(osgi(org.apache.xmlgraphics)) = 2.6.0
Provides: bundled(osgi(org.apiguardian)) = 1.1.0
Provides: bundled(osgi(org.bouncycastle.bcpg)) = 1.69.0
Provides: bundled(osgi(org.bouncycastle.bcprov)) = 1.69.0
Provides: bundled(osgi(org.eclipse.core.commands.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.commands.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.contenttype)) = 3.8.0
Provides: bundled(osgi(org.eclipse.core.contenttype.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.contenttype.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.beans)) = 1.8.0
Provides: bundled(osgi(org.eclipse.core.databinding.beans.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.beans.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.observable)) = 1.11.0
Provides: bundled(osgi(org.eclipse.core.databinding.observable.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.observable.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.property)) = 1.9.0
Provides: bundled(osgi(org.eclipse.core.databinding.property.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.databinding.property.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.expressions)) = 3.8.0
Provides: bundled(osgi(org.eclipse.core.expressions.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.expressions.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.filesystem.linux.x86_64.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.filesystem.linux.x86_64.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.filesystem.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.filesystem.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.jobs)) = 3.12.0
Provides: bundled(osgi(org.eclipse.core.jobs.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.jobs.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.linux.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.linux.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.linux.x86_64.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.linux.x86_64.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.net.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.resources.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.resources.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.runtime)) = 3.23.0
Provides: bundled(osgi(org.eclipse.core.runtime.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.runtime.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.variables.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.core.variables.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.debug.core.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.debug.core.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.commands)) = 1.0.0
Provides: bundled(osgi(org.eclipse.e4.core.commands.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.commands.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.contexts)) = 1.9.0
Provides: bundled(osgi(org.eclipse.e4.core.contexts.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.contexts.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di)) = 1.8.0
Provides: bundled(osgi(org.eclipse.e4.core.di.annotations)) = 1.7.0
Provides: bundled(osgi(org.eclipse.e4.core.di.annotations.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.annotations.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.extensions)) = 0.17.0
Provides: bundled(osgi(org.eclipse.e4.core.di.extensions.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.extensions.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.extensions.supplier.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.extensions.supplier.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.di.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.services)) = 2.3.0
Provides: bundled(osgi(org.eclipse.e4.core.services.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.core.services.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.emf.xpath)) = 0.3.0
Provides: bundled(osgi(org.eclipse.e4.emf.xpath.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.emf.xpath.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.bindings.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.bindings.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.core.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.core.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.swt.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.swt.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.swt.theme)) = 0.13.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.swt.theme.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.css.swt.theme.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.di)) = 1.4.0
Provides: bundled(osgi(org.eclipse.e4.ui.dialogs)) = 1.3.0
Provides: bundled(osgi(org.eclipse.e4.ui.dialogs.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.dialogs.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.di.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.di.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.model.workbench)) = 2.2.0
Provides: bundled(osgi(org.eclipse.e4.ui.model.workbench.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.model.workbench.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.services)) = 1.5.0
Provides: bundled(osgi(org.eclipse.e4.ui.services.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.services.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.swt.gtk.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.swt.gtk.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.widgets)) = 1.3.0
Provides: bundled(osgi(org.eclipse.e4.ui.widgets.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.widgets.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench)) = 1.13.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench3)) = 0.16.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench3.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench3.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.addons.swt.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.addons.swt.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.renderers.swt.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.renderers.swt.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.swt.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.e4.ui.workbench.swt.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.emf.common)) = 2.23.0
Provides: bundled(osgi(org.eclipse.emf.ecore)) = 2.25.0
Provides: bundled(osgi(org.eclipse.emf.ecore.change)) = 2.14.0
Provides: bundled(osgi(org.eclipse.emf.ecore.xmi)) = 2.16.0
Provides: bundled(osgi(org.eclipse.equinox.app)) = 1.6.0
Provides: bundled(osgi(org.eclipse.equinox.app.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.app.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.bidi)) = 1.4.0
Provides: bundled(osgi(org.eclipse.equinox.bidi.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.bidi.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.common)) = 3.15.0
Provides: bundled(osgi(org.eclipse.equinox.common.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.common.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.concurrent)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.concurrent.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.concurrent.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.console.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.console.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.event)) = 1.6.0
Provides: bundled(osgi(org.eclipse.equinox.event.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.event.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.frameworkadmin)) = 2.2.0
Provides: bundled(osgi(org.eclipse.equinox.frameworkadmin.equinox.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.frameworkadmin.equinox.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.frameworkadmin.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.frameworkadmin.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.jetty)) = 3.8.0
Provides: bundled(osgi(org.eclipse.equinox.http.jetty.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.jetty.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.registry)) = 1.3.0
Provides: bundled(osgi(org.eclipse.equinox.http.registry.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.registry.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.servlet.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.http.servlet.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.jsp.jasper.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.jsp.jasper.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.jsp.jasper.registry)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.jsp.jasper.registry.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.jsp.jasper.registry.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.launcher.gtk.linux.x86_64.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.launcher.gtk.linux.x86_64.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.launcher.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.launcher.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.artifact.repository.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.artifact.repository.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.console)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.p2.console.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.console.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.core)) = 2.8.0
Provides: bundled(osgi(org.eclipse.equinox.p2.core.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.core.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.director.app)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.p2.director.app.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.director.app.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.director.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.director.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.directorywatcher)) = 1.3.0
Provides: bundled(osgi(org.eclipse.equinox.p2.directorywatcher.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.directorywatcher.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.engine.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.engine.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.extensionlocation)) = 1.4.0
Provides: bundled(osgi(org.eclipse.equinox.p2.extensionlocation.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.extensionlocation.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.garbagecollector)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.p2.garbagecollector.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.garbagecollector.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.jarprocessor)) = 1.2.0
Provides: bundled(osgi(org.eclipse.equinox.p2.jarprocessor.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.jarprocessor.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.metadata.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.metadata.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.metadata.repository)) = 1.4.0
Provides: bundled(osgi(org.eclipse.equinox.p2.metadata.repository.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.metadata.repository.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.operations)) = 2.6.0
Provides: bundled(osgi(org.eclipse.equinox.p2.operations.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.operations.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.publisher.eclipse)) = 1.4.1
Provides: bundled(osgi(org.eclipse.equinox.p2.publisher.eclipse.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.publisher.eclipse.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.publisher.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.publisher.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.reconciler.dropins)) = 1.4.0
Provides: bundled(osgi(org.eclipse.equinox.p2.reconciler.dropins.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.reconciler.dropins.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.repository.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.repository.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.touchpoint.eclipse.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.touchpoint.eclipse.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.touchpoint.natives.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.touchpoint.natives.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.transport.ecf.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.transport.ecf.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.sdk)) = 1.2.1
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.sdk.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.sdk.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.sdk.scheduler.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.ui.sdk.scheduler.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.updatechecker)) = 1.3.0
Provides: bundled(osgi(org.eclipse.equinox.p2.updatechecker.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.p2.updatechecker.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.preferences)) = 3.9.0
Provides: bundled(osgi(org.eclipse.equinox.preferences.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.preferences.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.registry)) = 3.11.0
Provides: bundled(osgi(org.eclipse.equinox.registry.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.registry.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.linux.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.linux.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.linux.x86_64.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.linux.x86_64.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.ui)) = 1.3.0
Provides: bundled(osgi(org.eclipse.equinox.security.ui.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.security.ui.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator)) = 1.4.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator.manipulator)) = 2.2.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator.manipulator.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator.manipulator.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.equinox.simpleconfigurator.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.base.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.base.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.ui.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.ui.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.webapp.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.help.webapp.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jetty.alpn.client)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.client)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.http)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.http)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.io)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.io)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.security)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.security)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.server)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.server)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.servlet)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.servlet)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.util)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.util)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.util.ajax)) = 10.0.6
Provides: bundled(osgi(org.eclipse.jetty.webapp)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.api)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket-api)) = 1.1.2
Provides: bundled(osgi(org.eclipse.jetty.websocket.common)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.core.client)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.core.common)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.core.server)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.javax.client)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.javax.common)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.javax.server)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.server)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.websocket.servlet)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jetty.xml)) = 10.0.7
Provides: bundled(osgi(org.eclipse.jface)) = 3.23.0
Provides: bundled(osgi(org.eclipse.jface.databinding)) = 1.13.0
Provides: bundled(osgi(org.eclipse.jface.databinding.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.databinding.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.notifications)) = 0.3.0
Provides: bundled(osgi(org.eclipse.jface.notifications.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.notifications.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.text.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.jface.text.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi)) = 3.17.0
Provides: bundled(osgi(org.eclipse.osgi.compatibility.state.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.compatibility.state.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.services.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.services.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.util.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.osgi.util.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.rcp)) = 4.21.0
Provides: bundled(osgi(org.eclipse.swt.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.swt.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.text)) = 3.12.0
Provides: bundled(osgi(org.eclipse.text.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.text.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.forms.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.forms.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.intro.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.intro.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.net)) = 1.4.0
Provides: bundled(osgi(org.eclipse.ui.net.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.net.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.views.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.views.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.workbench.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.ui.workbench.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.update.configurator.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.update.configurator.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.eclipse.urischeme)) = 1.2.0
Provides: bundled(osgi(org.eclipse.urischeme.nl_ja)) = 4.21.0
Provides: bundled(osgi(org.eclipse.urischeme.nl_zh)) = 4.21.0
Provides: bundled(osgi(org.hamcrest.core)) = 1.3.0
Provides: bundled(osgi(org.hdrhistogram.HdrHistogram)) = 2.1.12
Provides: bundled(osgi(org.junit)) = 4.13.0
Provides: bundled(osgi(org.junit.jupiter.api)) = 5.7.1
Provides: bundled(osgi(org.junit.jupiter.engine)) = 5.7.1
Provides: bundled(osgi(org.junit.jupiter.migrationsupport)) = 5.7.1
Provides: bundled(osgi(org.junit.jupiter.params)) = 5.7.1
Provides: bundled(osgi(org.junit.platform.commons)) = 1.7.1
Provides: bundled(osgi(org.junit.platform.engine)) = 1.7.1
Provides: bundled(osgi(org.junit.platform.launcher)) = 1.7.1
Provides: bundled(osgi(org.junit.platform.runner)) = 1.7.1
Provides: bundled(osgi(org.junit.platform.suite.api)) = 1.7.1
Provides: bundled(osgi(org.junit.vintage.engine)) = 5.7.1
Provides: bundled(osgi(org.lz4.lz4-java)) = 1.8.0
Provides: bundled(osgi(org.objectweb.asm)) = 9.2.0
Provides: bundled(osgi(org.objectweb.asm.commons)) = 9.2.0
Provides: bundled(osgi(org.objectweb.asm.tree)) = 9.2.0
Provides: bundled(osgi(org.objectweb.asm.tree.analysis)) = 9.2.0
Provides: bundled(osgi(org.objectweb.asm.util)) = 9.2.0
Provides: bundled(osgi(org.openjdk.jmc.alert)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.alert.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.alert.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.attach)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.attach)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.attach.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.attach.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.jdp)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.jdp.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.jdp.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.browser.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.commands)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.common)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.agent)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.persistence)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.persistence.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.persistence.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.diagnostic)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.diagnostic.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.diagnostic.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.mbeanbrowser)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.mbeanbrowser.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.mbeanbrowser.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.notification)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.notification.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.notification.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.console.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.docs)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.docs.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.docs.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.configuration)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.controlpanel.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.controlpanel.ui.configuration)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.controlpanel.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.controlpanel.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.flameview)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.graphview)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.heatmap)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.rules)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.rules.extensionprovider)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.rules.jdk)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.serializers)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.flightrecorder.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.greychart)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.greychart.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.greychart.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.greychart.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.jdp)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.joverflow)) = 1.0.0
Provides: bundled(osgi(org.openjdk.jmc.joverflow.ui)) = 1.0.1
Provides: bundled(osgi(org.openjdk.jmc.osgi.extension)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.application)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.application.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.application.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.intro)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.intro.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rcp.intro.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.ext)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.services.jfr)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.rjmx.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.ui)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.ui.celleditors)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.ui.common)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.ui.ja)) = 8.2.0
Provides: bundled(osgi(org.openjdk.jmc.ui.zh_CN)) = 8.2.0
Provides: bundled(osgi(org.opentest4j)) = 1.2.0
Provides: bundled(osgi(org.owasp.encoder)) = 1.2.3
Provides: bundled(osgi(org.sat4j.core)) = 2.3.5
Provides: bundled(osgi(org.sat4j.pb)) = 2.3.5
Provides: bundled(osgi(org.slf4j.api)) = 1.7.30
Provides: bundled(osgi(org.tukaani.xz)) = 1.9.0
Provides: bundled(osgi(org.w3c.css.sac)) = 1.3.1
Provides: bundled(osgi(org.w3c.dom.events)) = 3.0.0
Provides: bundled(osgi(org.w3c.dom.smil)) = 1.0.1
Provides: bundled(osgi(org.w3c.dom.svg)) = 1.1.0

%description
JDK Mission Control is a powerful profiler for HotSpot JVMs and has an
advanced set of tools that enables efficient and detailed analysis of the
extensive data collected by JDK Flight Recorder. The tool chain enables
developers and administrators to collect and analyze data from Java
applications running locally or deployed in production environments.

%prep
# TODO: uncomment me
# %setup -q -n %{jmc_dir_name}
# %setup -q -T -D -a 1 -n %{jmc_dir_name}
# TODO: remove these two lines below
%setup -q -n jmc-master
%setup -q -T -D -a 1 -n jmc-master

# Build & install jmc core libraries
mvn -Dmaven.repo.local=repository-%{major}.%{minor}.%{patchlevel} -o clean install -f core/pom.xml

%patch0 -p1
%patch1 -p1

%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin

# Info.plist are mac files and we only build for Linux
%pom_remove_plugin name.abuchen:fix-info-plist-maven-plugin application/org.openjdk.jmc.rcp.product

# disable tests that require the use of jfr
%pom_disable_module org.openjdk.jmc.rjmx.services.jfr.test application/tests
%pom_disable_module org.openjdk.jmc.flightrecorder.controlpanel.ui.test application/tests

# ide.launch tests expect SWT to be installed, but we're leveraging a local repository instead
%pom_disable_module org.openjdk.jmc.ide.launch.test application/tests

%build

# some tests require large heap and fail with OOM
# depending on the builder resources
mvn -Dmaven.repo.local=repository-%{major}.%{minor}.%{patchlevel} verify -o -Dmaven.test.failure.ignore=true -DbuildId=rhel -DbuildNumber=%{revhash} -Dbuild.date=%{revdate}

%install

# not using mvn_install macro because it installs JMC as an Eclipse plugin
# we want to install JMC as an RCP application

# change jmc.ini to use system java (remove -vm option line)
# TODO: uncomment -> sed -i '/^-vm$/d' %{_builddir}/%{jmc_dir_name}/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/%{name}.ini
# TODO: uncomment -> sed -i '/^..\/..\/bin\/$/d' %{_builddir}/%{jmc_dir_name}/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/%{name}.ini
sed -i '/^-vm$/d' %{_builddir}/jmc-master/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/%{name}.ini
sed -i '/^..\/..\/bin\/$/d' %{_builddir}/jmc-master/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/%{name}.ini

# move contents of target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control' to /usr/lib/jmc/
install -d -m 755 %{buildroot}%{_jmcdir}
# TODO: uncomment -> cp -p -r %{_builddir}/%{jmc_dir_name}/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/* %{buildroot}%{_jmcdir}/
cp -p -r %{_builddir}/jmc-master/target/products/org.openjdk.jmc/linux/gtk/x86_64/'JDK Mission Control'/* %{buildroot}%{_jmcdir}/

# move jmc.ini to /etc/jmc.ini
install -d -m 755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_jmcdir}/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
ln -s %{_sysconfdir}/%{name}.ini %{buildroot}%{_jmcdir}/%{name}.ini

# create symlink to jmc in /usr/bin/
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_jmcdir}/%{name} %{buildroot}%{_bindir}/%{name}

# create application launcher in desktop menu
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_jmcdir}/icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
chmod 644 %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

# install pom file
install -d -m 755 %{buildroot}%{_datadir}/maven-poms/%{name}
# TODO: uncomment -> install -p -m 644 %{_builddir}/%{jmc_dir_name}/pom.xml %{buildroot}%{_datadir}/maven-poms/%{name}/%{name}.pom
install -p -m 644 %{_builddir}/jmc-master/pom.xml %{buildroot}%{_datadir}/maven-poms/%{name}/%{name}.pom

# install manpage and insert location of config file
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1/%{name}.1
sed -i "/.SH FILES/a .I %{_sysconfdir}/%{name}.ini" %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license license/LICENSE.txt
%license license/THIRDPARTYREADME.txt
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.ini
%{_jmcdir}
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/maven-poms/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jan 27 2022 Alex Macdonald <almacdon@redhat.com> - 8.2.0-1
- Initial package using bundled m2 repository
- There are still TODOs to clean up once 8.2.0 is tagged
