%define 	module nwdiag
Summary:	nwdiag generate network-diagram image file from spec-text file
Name:		python-%{module}
Version:	0.5.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
URL:		http://blockdiag.com/en/%{module}/index.html
Source0:	http://pypi.python.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	affeeca174b6b68a7fca416d6831f1af
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-blockdiag >= 0.8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nwdiag generate network-diagram image file from spec-text file.

Features:
- Generate network-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}_sphinxhelper.py[co]
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib_%{module}.py[co]

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{module}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{module}
%attr(644,root,root) %{_mandir}/man1/%{module}.*.gz
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
