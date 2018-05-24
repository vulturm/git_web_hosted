%undefine _disable_source_fetch
%define project_name gitea

Name:           %{project_name}
Version:        master
Release:        1%{?dist}
Summary:        Gitea web-hosted Git service.

License:        GPL
URL:            https://gitea.io
Source0:        https://dl.gitea.io/gitea/%version/%name-%version-linux-amd64
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
%define _prefix /opt



%prep
wget %{_url_binary} -O ../SOURCES/%name-%version-linux-amd64
wget %{_url_binary_sha} -O ../SOURCES/%name-%version-linux-amd64.sha256
wget %{_url_config} -O ../SOURCES/app.ini

#sha256sum -c -
#%setup -q

%build
/bin/true


%install
mkdir -p %{buildroot}%{_prefix}/%{project_name}/{custom/conf,data,log}
install -p -m 755 %{SOURCE0} %{buildroot}%{_prefix}/%{project_name}
install -p -m 640 %{SOURCE2} %{buildroot}%{_prefix}/%{project_name}/custom/conf/


%files
%defattr(0644,git,git,0755)
%attr (755,git,git) %{_prefix}/%{project_name}
%attr(0640,git,git) %config(noreplace) %{_prefix}/%{project_name}/custom/conf/app.ini


%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group git > /dev/null || groupadd -r git
getent passwd git > /dev/null || \
	useradd -m -g git -s /bin/bash \
	-c "Hosted git account" git

#%post 


%changelog
* Thu May 24 2018 Mihai Vultur <mihai.vultur@__.com>
- initial spec
