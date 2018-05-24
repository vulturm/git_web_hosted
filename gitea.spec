%undefine _disable_source_fetch
%define project_name gitea
#-- so that we can identify build date
%define build_timestamp %(date +"%Y%m%d")


Name:           %{project_name}
Version:        master
Release:        %{build_timestamp}
Summary:        Gitea web-hosted Git service.

License:        GPL
URL:            https://gitea.io
Source0:        https://dl.gitea.io/gitea//%version/%name-%version-linux-amd64
Source1:	https://dl.gitea.io/gitea//%version/%name-%version-linux-amd64.sha256
Source2:	https://raw.githubusercontent.com/xxmitsu/gitea/master/app.ini

BuildRequires:	make

Requires: git >= 1.7.2

ExclusiveArch: x86_64

%description
Gitea web-hosted Git service, written in Golang

%define _url_binary https://dl.gitea.io/gitea/%version/%name-%version-linux-amd64
%define _url_binary_sha https://dl.gitea.io/gitea/%version/%name-%version-linux-amd64.sha256
%define _url_config https://raw.githubusercontent.com/xxmitsu/gitea/master/app.ini
%define _prefix /opt/git
%define _installdir %{buildroot}%{_prefix}


%prep
set +x
wget %{_url_binary} -O ../SOURCES/%name-%version-linux-amd64
wget %{_url_binary_sha} -O ../SOURCES/%name-%version-linux-amd64.sha256
wget %{_url_config} -O ../SOURCES/app.ini
pushd ../SOURCES/
sha256sum -c %name-%version-linux-amd64.sha256

%build
/bin/true


%install
#
mkdir -p %{_installdir}/%{project_name}/{custom/conf,data,log} 
mkdir -p %{_installdir}/%{project_name}-repositories
install -p -m 755 %{SOURCE0} %{_installdir}/%{project_name}
install -p -m 640 %{SOURCE2} %{_installdir}/%{project_name}/custom/conf/
sed -i 's=@@HOME_DIR@@=%{_prefix}/%{project_name}=g' %{_installdir}/%{project_name}/custom/conf/app.ini


%files
%defattr(0644,git,git,0755)
%dir %attr(0755,git,git) %{_prefix}/%{project_name}
%dir %attr(0755,git,git) %{_prefix}/%{project_name}-repositories
%dir %attr(0755,git,git) %{_prefix}/%{project_name}/custom/
%dir %attr(0755,git,git) %{_prefix}/%{project_name}/custom/conf
%dir %attr(0755,git,git) %{_prefix}/%{project_name}/data
%dir %attr(0755,git,git) %{_prefix}/%{project_name}/log

%attr(0755,git,git) %{_prefix}/%{project_name}/%name-%version-linux-amd64
%attr(0640,git,git) %config(noreplace) %{_prefix}/%{project_name}/custom/conf/*



%clean
rm -rf %{buildroot}

%pre
getent group git > /dev/null || groupadd -r git
getent passwd git > /dev/null || \
	useradd -m -g git -s /bin/bash \
	-c "Hosted git account" git



%changelog
* Thu May 24 2018 Mihai Vultur <mihai.vultur@__.com>
- Silent build, create directories with permissions, create default config 

* Thu May 24 2018 Mihai Vultur <mihai.vultur@__.com>
- initial spec
