%define name	libmcrypto
%define oname	mcrypto
%define version 0.3.1
%define svn	3565
%define release %mkrel %svn.2

%define major	0
%define libname %mklibname %{oname} %major
%define develname %mklibname %{oname} -d

Name: 	 	%{name}
Summary: 	Cryptography library from MiniSip
Version: 	%{version}
Release: 	%{release}

Source:		http://www.minisip.org/source/%{name}-%{svn}.tar.bz2
URL:		https://www.minisip.org/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  openssl-devel >= 0.9.8
BuildRequires:	libmnetutil-devel >= 0.3.1-3565.0

%description
The libmcrypto library provides cryptographic encryption and hashing
interfaces that are leveraged by the Minisip application stack.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:       %{oname} = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name

%build
./bootstrap
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_libdir}/pkgconfig/%name.pc
%{_datadir}/aclocal/%name.m4
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


