%define		fversion	%(echo %{version} |tr r -)
%define		modulename	xtable
Summary:	Coerce data to LaTeX and HTML tables
Name:		R-cran-%{modulename}
Version:	1.7r1
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	ede8e4076134edd4743a7fb91e4a11c2
BuildRequires:	R >= 2.8.1
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-booktabs
Requires:	R >= 2.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coerce data to LaTeX and HTML tables.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%doc %{modulename}/NEWS
%{_libdir}/R/library/%{modulename}
