#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Detect
Summary:	Log::Detect - Read logfiles to detect error and warning messages
Summary(pl):	Log::Detect - Przetwórz logi w celu wykrycia b³êdów i ostrze¿eñ
Name:		perl-Log-Detect
Version:	1.412
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Detect is used to read logfiles, and apply regexps to determine if
the logfile contains any errors or warning messages.  This is generally
useful for those programs that refuse to return bad exit status when
they should.

%description -l pl
Log::Detect u¿ywany jest do czytania plików z logami, oraz u¿ycia wyra¿eñ
regularnych do stwierdzenia, czy zawieraj± jakie¶ informacje o b³êdach
lub ostrze¿enia.  Najczê¶ciej jest to przydatne w przypadku programów,
które nie zwracaj± sygnalizuj±cego b³±d kodu wyj¶cia, gdy powinny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_examplesdir}/%{name}-%{version}
%{_bindir}/*
%{_mandir}/man?/*
