#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Excel
%define		pnam	Writer-XLSX
Summary:	Excel::Writer::XLSX - Create a new file in the Excel 2007+ XLSX format
Name:		perl-Excel-Writer-XLSX
Version:	0.98
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10c9bd6bb77fc08da41c385d994ce20d
URL:		http://search.cpan.org/dist/Excel-Writer-XLSX/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-modules >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Excel::Writer::XLSX module can be used to create an Excel file in
the 2007+ XLSX format. The XLSX format is the Office Open XML (OOXML)
format used by Excel 2007 and later. Multiple worksheets can be added
to a workbook and formatting can be applied to cells. Text, numbers,
and formulas can be written to the cells. This module cannot, as yet,
be used to write to an existing Excel XLSX file.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/{README,*.pl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extract_vba
%doc Changes README
%dir %{perl_vendorlib}/Excel
%dir %{perl_vendorlib}/Excel/Writer
%{perl_vendorlib}/Excel/Writer/XLSX.pm
%dir %{perl_vendorlib}/Excel/Writer/XLSX
%{perl_vendorlib}/Excel/Writer/XLSX/*.pm
%{perl_vendorlib}/Excel/Writer/XLSX/Chart
%{perl_vendorlib}/Excel/Writer/XLSX/Package
%{_mandir}/man?/*
#dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}
