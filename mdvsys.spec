%define name	mdvsys
%define version	2.1.0
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to Mandriva build system
License:	GPL
Group:		Development/Perl
Source0:	%{name}-%{version}.tar.gz
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/%{name}
BuildRequires: subversion-tools
BuildRequires: perl(Config::IniFiles)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(HTML::TableExtract)
BuildRequires: perl(IO::String)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(RPM4)
BuildRequires: perl(SVN::Client)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Youri::Package::RPM::Updater)
BuildRequires: perl(Youri::Package::RPM::Builder)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl-version
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod)
Requires: perl(Youri::Package::RPM::Updater)
Requires: perl(Youri::Package::RPM::Builder)
Requires: perl(HTML::TableExtract)
Requires: perl(IO::String)
# (tv) lazy loaded (thus runtime error):
Requires: perl(Net::LDAP)
Obsoletes: perl-MDV-Repsys
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is an interface to Mandriva build system.

%prep
%setup -q
# fixed in SVN for next release
rm -f t/pod-coverage.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor SYSCONFDIR=%{_sysconfdir}
%{__make}

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 etc/mdvsys %{buildroot}%{_sysconfdir}/bash_completion.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_sysconfdir}/bash_completion.d/mdvsys
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/MDV
