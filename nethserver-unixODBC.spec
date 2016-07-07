Summary: NethServer module with ODBC configuration templates
Name: nethserver-unixODBC
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}
BuildArch: noarch

Requires: unixODBC
Requires: freetds
Requires: mysql-connector-odbc
Requires: postgresql-odbc
Requires: nethserver-base
BuildRequires: nethserver-devtools

%description
NethServer module with ODBC configuration templates

%prep
%setup

%build
perl createlinks

%install
/bin/rm -rf %{buildroot}
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(0644,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update


%changelog
* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.0.0-1
- First NS7 release

* Wed Jan 21 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.7-1.ns6
- Add MSSQL support in nethserver-unixODBC - Feature #3003 [NethServer]

* Tue Nov 11 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.6-1.ns6
* Missing dependency nethserver-base - Refs #2950

* Tue Jun 24 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.5-1.ns6
- First release - Feature #2781

* Mon Feb 10 2014 Stefano Fancello <stefano.fancello@nethesis.it> - 0.0.1-1
- First package
