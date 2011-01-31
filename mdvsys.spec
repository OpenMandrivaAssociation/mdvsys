Name:		mdvsys
Version:	2.3.0
Release:	%mkrel 1
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
BuildRequires: perl(RPM)
BuildRequires: perl(SVN::Client)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Youri::Package::RPM::Updater)
BuildRequires: perl(Youri::Package::RPM::Builder)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl-version
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod)
Requires: perl(Youri::Package::RPM)
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

%build
%configure2_5x
%make

%check
%make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README
%{_sysconfdir}/bash_completion.d/mdvsys
%config(noreplace) %{_sysconfdir}/mdvsys.conf
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/mdvsys
