
%define realname   Text-FixEOL
%define version    1.05
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Canonicalizes mixed convention EOL/EOF
Source:     http://www.cpan.org/modules/by-module/Text/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
Converts the EOL and EOF conventions in the passed string to a canonicalization
form that handles 'mixed' EOL conventions.

It canonicalizes EOL as \n (the platform defined EOL) if it does not know the
particular platform. Can also 'fix' the end-of-file mark if needed and ensure
that the last line of the string is EOL terminated.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



