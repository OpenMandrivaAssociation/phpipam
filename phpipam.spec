%define __noautoreqfiles %{_datadir}/%{name}/functions
%define __noautoreq 'pear.functions.PEAR.OLE.php|pear.functions.PEAR.PEAR.php'

Name:           phpipam
Version:        0.4
Release:        3
Summary:     	Open-source web IP address management application
License:     	GPLv2+
Group:       	Networking/Other
URL:         	http://phpipam.sourceforge.net/
Source0:     	%{name}-%{version}.tar
Requires:       apache-mod_php
Requires:       php-mysqli
Requires:	php-session
Requires:       php-gmp
Requires:       php-pear
BuildArch:      noarch
AutoReqProv: 	1
Suggests:	mysql
Requires(post): rpm-helper

%description
phpipam is an open-source web IP address management application. Its goal is 
to provide light and simple IP address management. It is ajax-based using 
jQuery libraries, php scripts, javascript and some HTML5/CSS3 features

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -aRf * %{buildroot}%{_datadir}/%{name}/

pushd %{buildroot}%{_datadir}/%{name}
    rm -f INSTALL UPDATE README 
popd


# provide a simple apache config
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{webappconfdir}

pushd  %{buildroot}%{_sysconfdir}/%{name}
    ln -s ../../%{_datadir}/%{name}/config.php config.php
popd

cat > %{buildroot}%{_webappconfdir}/%{name}.conf << EOF
Alias /%{name} %{_datadir}/%{name}

<Directory %{_datadir}/%{name}>
    Require local granted
    ErrorDocument 403 "Access denied per %{_webappconfdir}/%{name}.conf"
</Directory>
EOF


%files
%defattr(0755,root,root)
%doc INSTALL README UPDATE
%attr(-,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/config.php
%config(noreplace) %{_webappconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%{_datadir}/%{name}



%changelog
* Wed Nov 09 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.4-1mdv2011.0
+ Revision: 729285
- import phpipam

