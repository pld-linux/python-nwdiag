%define 	module nwdiag
Summary:	nwdiag generate network-diagram image file from spec-text file
Name:		python-%{module}
Version:	0.7.0
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	be27a6238a5275cc2bbe376fd1c2b6e9
URL:		http://blockdiag.com/en/nwdiag/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
Requires:	python-blockdiag >= 1.1.0
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
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}_sphinxhelper.py[co]
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/rackdiag_sphinxhelper.py[co]

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{module}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{module}
%attr(755,root,root) %{_bindir}/rackdiag
%{_mandir}/man1/%{module}.1*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/rackdiag
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
