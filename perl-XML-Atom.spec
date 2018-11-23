#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Atom
Version  : 0.42
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-0.42.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-0.42.tar.gz
Summary  : 'Atom feed and API implementation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-Atom-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

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

%description dev
dev components for the perl-XML-Atom package.


%package license
Summary: license components for the perl-XML-Atom package.
Group: Default

%description license
license components for the perl-XML-Atom package.


%prep
%setup -q -n XML-Atom-0.42

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Atom
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-Atom/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Base.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Category.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Client.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Content.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Entry.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/ErrorHandler.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Feed.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Link.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Person.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Server.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Thing.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/Atom/Util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Atom.3
/usr/share/man/man3/XML::Atom::Base.3
/usr/share/man/man3/XML::Atom::Category.3
/usr/share/man/man3/XML::Atom::Client.3
/usr/share/man/man3/XML::Atom::Content.3
/usr/share/man/man3/XML::Atom::Entry.3
/usr/share/man/man3/XML::Atom::ErrorHandler.3
/usr/share/man/man3/XML::Atom::Feed.3
/usr/share/man/man3/XML::Atom::Link.3
/usr/share/man/man3/XML::Atom::Person.3
/usr/share/man/man3/XML::Atom::Server.3
/usr/share/man/man3/XML::Atom::Thing.3
/usr/share/man/man3/XML::Atom::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Atom/LICENSE
