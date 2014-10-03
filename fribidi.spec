Summary:	Library implementing the Unicode BiDi algorithm
Name:		fribidi
Version:	0.19.6
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://fribidi.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	ce93d862344991173dabb609bf93ca1d
URL:		http://fribidi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Free Implementation of the Unicode BiDi algorithm.

%package devel
Summary:	Library implementing the Unicode BiDi algorithm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The fribidi-devel package includes header files for the fribidi
package.

%prep
%setup -q

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/fribidi
%attr(755,root,root) %ghost %{_libdir}/libfribidi.so.?
%attr(755,root,root) %{_libdir}/libfribidi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/fribidi
%{_pkgconfigdir}/*.pc

