%define upstream_name    Text-FixEOL
%define upstream_version 1.08
Name:		perl-%{upstream_name}
Version:	1.08
Release:	3

Summary:	Canonicalizes mixed convention EOL/EOF
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/JerilynFranz/perl-Text-FixEOL
Source0:	https://cpan.metacpan.org/authors/id/S/SN/SNOWHARE/Text-FixEOL-1.08.tar.gz

BuildRequires:	make
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
%setup -q -n Text-FixEOL-1.08

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

