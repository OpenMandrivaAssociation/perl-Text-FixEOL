%define upstream_name    Text-FixEOL
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Canonicalizes mixed convention EOL/EOF
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Converts the EOL and EOF conventions in the passed string to a canonicalization
form that handles 'mixed' EOL conventions.

It canonicalizes EOL as \n (the platform defined EOL) if it does not know the
particular platform. Can also 'fix' the end-of-file mark if needed and ensure
that the last line of the string is EOL terminated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
