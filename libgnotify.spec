Summary:	GNotify library
Summary(pl):	Biblioteka GNotify
Name:		libgnotify
Version:	1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gnotify/%{name}lib-%{version}.tar.gz
# Source0-md5:	2477a05eafed88cb202c55b324925478
URL:		http://gnotify.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNotify library.

%description -l pl
Biblioteka GNotify.

%package devel
Summary:	Header files for GNotify library
Summary(pl):	Pliki nag³ówkowe biblioteki GNotify
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GNotify library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GNotify.

%package static
Summary:	Static GNotify library
Summary(pl):	Statyczna biblioteka GNotify
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNotify library.

%description static -l pl
Statyczna biblioteka GNotify.

%prep
%setup -q -n %{name}lib-%{version}

rm -f COPYING INSTALL mkinstalldirs
touch COPYING INSTALL mkinstalldirs

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/GNotifyLib

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
