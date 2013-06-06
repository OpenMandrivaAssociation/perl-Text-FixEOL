%define upstream_name    Text-FixEOL
%define upstream_version 1.06
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.06
Release:	1

Summary:	Canonicalizes mixed convention EOL/EOF
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-FixEOL-1.06.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.50.0-4mdv2011.0
+ Revision: 658551
- rebuild for updated spec-helper
- rebuild for updates rpm-setup

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-2mdv2010.0
+ Revision: 405950
- force rebuild
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.05-4mdv2009.0
+ Revision: 258615
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.05-3mdv2009.0
+ Revision: 246629
- rebuild
- fix description-line-too-long

* Fri Jan 18 2008 Jérôme Quelin <jquelin@mandriva.org> 1.05-1mdv2008.1
+ Revision: 154662
- import perl-Text-FixEOL



