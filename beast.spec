Summary:	BEAST (the Bedevilled Audio System)
Name:		beast
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://beast.gtk.org/beast-ftp/v0.5/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://beast.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >=  2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	guile-devel >= 1.4
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	mad-devel >= 0.14.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BEAST (the Bedevilled Audio System) is a GTK+/GNOME based front-end to
BSE (the Bedevilled Sound Engine). BSE is a shared library that comes
with the necessary framework to simulate audio synthesis (modular
synthesis) in realtime and allow for song composition.

%package devel
Summary: 	Header files for Beast
Group:		Libraries
Requires:	%{name} = %{version}

%description devel
Header files for Beast.

%prep
%setup -q
%patch0 -p1

%build
rm -f aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-devdsp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/bse
%{_libdir}/bse/v%{version}/plugins/*.so
%{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%{_includedir}/bse
%{_includedir}/bsw
%{_includedir}/sfi
%{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man3/*
%{_pkgconfigdir}/*.pc
# do we really need this?
%{_libdir}/bse/v%{version}/plugins/*.la
