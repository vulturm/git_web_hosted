#!/bin/bash
#-- make sure we have those installed
sudo yum install -y xmlto asciidoc subversion-perl perl-YAML
mkdir -p ~/rpmbuild ~/rpmbuild/BUILD ~/rpmbuild/BUILDROOT ~/rpmbuild/RPMS ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS
pushd ~/rpmbuild/SOURCES
wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/git-core/git-1.9.0.tar.gz
rpmbuild -tb git-1.9.0.tar.gz

#yum -y install ~/rpmbuild/RPMS/`uname -i`/git-1.9.0-1.el6.x86_64.rpm ~/rpmbuild/RPMS/`uname -i`/perl-Git-1.9.0-1.el6.x86_64.rpm
