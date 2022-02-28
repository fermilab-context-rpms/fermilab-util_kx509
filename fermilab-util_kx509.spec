Name: fermilab-util_kx509
Version: 3.1
Release: 2%{?dist}
License: BSD
Group:   Fermilab

URL:     https://github.com/fermilab-context-rpms/fermilab-util_kx509
Summary: Get an X.509 certificate for Fermilab using kerberos
Source0: kx509
Source1: kx509.1

Requires: cigetcert
Provides: krb5-fermi-getcert = %{version}
Obsoletes: krb5-fermi-getcert < 3

BuildArch: noarch

%description
fermilab-util_kx509 contains a kx509 command which gets an X.509
certificate for Fermilab using cigetcert with kerberos authentication.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/man/man1
cp %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/man/man1/kx509.1

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/kx509
%{_datadir}/man/man1/kx509*


%changelog
* Thu Feb 27 2020 Dave Dykstra <dwd@fnal.gov> 3.1-2
- Add Provides krb5-fermi-getcert and obsolete older versions

* Thu Feb 18 2016 Dave Dykstra <dwd@fnal.gov> 3.1-1
- Add support for X509_USER_PROXY variable

* Thu Feb 11 2016 Dave Dykstra <dwd@fnal.gov> 3.0-1
- Initial rpm packaging.  The numbering is starting with 3.0 to be 
  greater than the latest krb5-fermi-getcert, the package that this
  is replacing.
