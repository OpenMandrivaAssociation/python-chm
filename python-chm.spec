%define name		python-chm
%define realname	pychm
%define version 0.8.4

Summary: Python package to handle CHM files
Name:			%{name}
Version:		%{version}
Release:		%mkrel 1
Source0: %{realname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRequires:	chmlib-devel
BuildRequires:	python-devel
Url: http://gnochm.sourceforge.net
Provides: pychm

%description
The chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library
chmlib and some additional classes and functions. They are
used to access MS-ITSS encoded files - Compressed Html Help
files (.chm).

%prep
%setup -q -n %{realname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README NEWS COPYING ChangeLog

