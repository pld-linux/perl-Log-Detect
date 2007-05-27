#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Detect
Summary:	Log::Detect - read logfiles to detect error and warning messages
Summary(pl.UTF-8):	Log::Detect - przetwarzanie logów w celu wykrycia błędów i ostrzeżeń
Name:		perl-Log-Detect
Version:	1.422
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7f026e74269c2049aa53b6ddeb48704
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-IO-Zlib
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Detect is used to read logfiles, and apply regexps to determine if
the logfile contains any errors or warning messages.  This is generally
useful for those programs that refuse to return bad exit status when
they should.

%description -l pl.UTF-8
Log::Detect używany jest do czytania plików z logami, oraz użycia wyrażeń
regularnych do stwierdzenia, czy zawierają jakieś informacje o błędach
lub ostrzeżenia.  Najczęściej jest to przydatne w przypadku programów,
które nie zwracają sygnalizującego błąd kodu wyjścia, gdy powinny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
