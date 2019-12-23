%define name		python-chm
%define realname	pychm
%define version 0.8.6

Summary: Python package to handle CHM files
Name:			%{name}
Version:		%{version}
Release:		1
Url: http://gnochm.sourceforge.net
Source0: https://pypi.io/packages/source/p/%{realname}/%{realname}-%{version}.tar.gz
License: GPL
Group: Development/Python
BuildRequires:	chmlib-devel
BuildRequires:	python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Provides: pychm

%description
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions. They are
used to access MS-ITSS encoded files - Compressed Html Help
files (.chm).

%package -n	python-%{realname}
Summary:	Python package to handle CHM files
BuildRequires:	python-devel
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python-%{realname_name}}
%{?python_provide:%python_provide python-chm}

%description -n	python-%{realname}
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions. They are
used to access MS-ITSS encoded files - Compressed Html Help
files (.chm).

%prep
%setup -q -n %{realname}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info/

%build
%py_build

%install
%py_install

%files -n python-%{realnamename}
%license COPYING
%doc README
%{python_sitearch}/chm/
%{python_sitearch}/pychm-%{version}-py?.?.egg-info/


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.8.4-5mdv2011.0
+ Revision: 598962
- update file list
- update file list

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.8.4-5mdv2010.0
+ Revision: 442068
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4-4mdv2009.0
+ Revision: 259546
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4-3mdv2009.0
+ Revision: 247400
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8.4-1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.4-1mdv2008.0
+ Revision: 52595
- update to new version 0.8.4


* Fri May 26 2006 Jerome Soyer <saispo@mandriva.org> 0.8.3-1mdv2007.0
- New release 0.8.3
- add Provides pychm

* Fri Mar 31 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8.2-2mdk
- Rebuild

* Mon Feb 14 2005 Jerome Soyer <saispo@mandrake.org> 0.8.2-1mdk
- 0.8.2

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.8.0-2mdk
- Rebuild for new python

* Fri Jun 18 2004 Stefan van der Eijk <stefan@mandrake.org> 0.8.0-1mdk
- initial MDK package

