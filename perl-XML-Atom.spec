#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-XML-Atom
Version  : 0.43
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-0.43.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-0.43.tar.gz
Summary  : 'Atom feed and API implementation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-Atom-license = %{version}-%{release}
Requires: perl-XML-Atom-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
XML::Atom - Atom feed and API implementation
SYNOPSIS
use XML::Atom;
DESCRIPTION

%package dev
Summary: dev components for the perl-XML-Atom package.
Group: Development
Provides: perl-XML-Atom-devel = %{version}-%{release}
Requires: perl-XML-Atom = %{version}-%{release}

%description dev
dev components for the perl-XML-Atom package.


%package license
Summary: license components for the perl-XML-Atom package.
Group: Default

%description license
license components for the perl-XML-Atom package.


%package perl
Summary: perl components for the perl-XML-Atom package.
Group: Default
Requires: perl-XML-Atom = %{version}-%{release}

%description perl
perl components for the perl-XML-Atom package.


%prep
%setup -q -n XML-Atom-0.43
cd %{_builddir}/XML-Atom-0.43
pushd ..
cp -a XML-Atom-0.43 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Atom
cp %{_builddir}/XML-Atom-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-Atom/2434119d9a2c5e02869672c3767acc217fc2d4ba || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Atom.3
/usr/share/man/man3/XML::Atom::Client.3
/usr/share/man/man3/XML::Atom::Entry.3
/usr/share/man/man3/XML::Atom::Feed.3
/usr/share/man/man3/XML::Atom::Person.3
/usr/share/man/man3/XML::Atom::Server.3
/usr/share/man/man3/XML::Atom::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Atom/2434119d9a2c5e02869672c3767acc217fc2d4ba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
