#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Detect
Summary:	Log::Detect - read logfiles to detect error and warning messages
Summary(pl):	Log::Detect - przetwarzanie log�w w celu wykrycia b��d�w i ostrze�e�
Name:		perl-Log-Detect
Version:	1.421
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de60b23c1479fc44e5d2c195828068b4
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

%description -l pl
Log::Detect u�ywany jest do czytania plik�w z logami, oraz u�ycia wyra�e�
regularnych do stwierdzenia, czy zawieraj� jakie� informacje o b��dach
lub ostrze�enia.  Najcz�ciej jest to przydatne w przypadku program�w,
kt�re nie zwracaj� sygnalizuj�cego b��d kodu wyj�cia, gdy powinny.

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
