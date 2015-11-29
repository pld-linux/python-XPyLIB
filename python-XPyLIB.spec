%define		module XPyLIB
Summary:	Library for Python, Boa constructor plug-ins
Summary(pl.UTF-8):	Biblioteka Pythona, wtyczki konstruktora Boa
Name:		python-%{module}
Version:	0.1.1
Release:	0.1
License:	BSD License
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/xpylib/%{module}-%{version}.zip
# Source0-md5:	5835b5b7fa9b50db4f917310ef11b735
URL:		http://sourceforge.net/projects/xpylib/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Python, Boa constructor plug-ins.

%description -l pl.UTF-8
Biblioteka Pythona, wtyczki konstruktora Boa.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/html/*
%dir %{py_sitescriptdir}/%{module}
%dir %{py_sitescriptdir}/%{module}/config
%dir %{py_sitescriptdir}/%{module}/test
%dir %{py_sitescriptdir}/XPyTools
%dir %{py_sitescriptdir}/XPyTools/codetpl
%dir %{py_sitescriptdir}/XPyTools/codetpl/templates
%dir %{py_sitescriptdir}/XPyTools/codetpl/test
%dir %{py_sitescriptdir}/XPyTools/scripts
%attr(755,root,root) %{py_sitescriptdir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/%{module}/test/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/XPyTools/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/XPyTools/codetpl/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/XPyTools/codetpl/templates/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/XPyTools/codetpl/test/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/XPyTools/scripts/*.py[co]
%{py_sitescriptdir}/%{module}/config/*.cfg
%{py_sitescriptdir}/%{module}/test/*.cfg
%{py_sitescriptdir}/XPyTools/codetpl/*.bmp
%{py_sitescriptdir}/XPyTools/codetpl/templates/*.cfg
%{py_sitescriptdir}/XPyTools/codetpl/templates/*.txt
%{py_sitescriptdir}/XPyTools/codetpl/test/*.cfg
%{py_sitescriptdir}/*.egg-info
