%define module	MDV-Repsys
%define name	perl-%{module}
%define version	2.0.6
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to Mandriva build system
License:	GPL
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.gz
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/%{module}/
BuildRequires: subversion-tools
BuildRequires: perl(Config::IniFiles)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(Date::Format)
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
Provides: mdvsys
# http://qa.mandriva.com/show_bug.cgi?id=28388
Requires: repsys
Requires: subversion-tools
Requires: perl(Youri::Package::RPM::Updater)
Requires: perl(Youri::Package::RPM::Builder)
Requires: perl(HTML::TableExtract)
Requires: perl(IO::String)
# (tv) lazy loaded (thus runtime error):
Requires: perl(Net::LDAP)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is an interface to Mandriva build system.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor SYSCONFDIR=%{_sysconfdir}
%{__make}

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
#%{_sysconfdir}/bash_completion.d/mdvsys
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/MDV
