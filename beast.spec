Summary:	BEAST (the Bedevilled Audio System)
Summary(pl.UTF-8):	System dźwięku BEAST (Bedevilled Audio System)
Name:		beast
Version:	0.7.4
Release:	1
License:	LGPL v2.1+ (library/engine), GPL v2+ (application)
Group:		Applications/Sound
Source0:	http://beast.gtk.org/beast-ftp/v0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	f383762ef20a6ed1ee0ee0e43172bfd6
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-guile2.patch
Patch2:		%{name}-assert.patch
Patch3:		%{name}-c++.patch
URL:		http://beast.gtk.org/
BuildRequires:	alsa-lib-devel >= 1.0.5
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.9
BuildRequires:	glib2-devel >= 1:2.6.4
BuildRequires:	gtk+2-devel >= 2:2.12.12
BuildRequires:	guile-devel >= 2.0
BuildRequires:	libart_lgpl-devel >= 2.3.8
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libmad-devel >= 0.14.2
BuildRequires:	libogg-devel >= 1:1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0.0
BuildRequires:	pango-devel >= 1:1.4.0
BuildRequires:	perl-base >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.4.1
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	shared-mime-info
Requires:	alsa-lib >= 1.0.5
Requires:	glib2 >= 1:2.6.4
Requires:	gtk+2 >= 2:2.12.12
Requires:	libart_lgpl >= 2.3.8
Requires:	libgnomecanvas >= 2.4.0
Requires:	pango >= 1:1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BEAST (the Bedevilled Audio System) is a GTK+/GNOME based front-end to
BSE (the Bedevilled Sound Engine). BSE is a shared library that comes
with the necessary framework to simulate audio synthesis (modular
synthesis) in realtime and allow for song composition.

%description -l pl.UTF-8
System dźwięku BEAST (Bedevilled Audio System) to oparty na GTK+/GNOME
frontend dla silnika dźwięku BSE (Bedevilled Sound Engine). BSE to
biblioteka współdzielona, która przychodzi wraz ze szkieletem
potrzebnym do symulacji syntezy dźwięku (syntezy modularnej) w czasie
rzeczywistym oraz umożliwienia komponowania piosenek.

%package devel
Summary:	Header files for BEAST
Summary(pl.UTF-8):	Pliki nagłówkowe dla BEAST
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6.4
Requires:	libogg-devel >= 1:1.0.0
Requires:	libvorbis-devel >= 1:1.0.0

%description devel
Header files for BEAST.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla BEAST.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-debug \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	UPDATE_MIME_DATABASE=

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bse/v%{version}/{drivers,plugins}/*.la

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
update-mime-database %{_datadir}/mime ||:
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
/sbin/ldconfig
umask 022
update-mime-database %{_datadir}/mime
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beast*
%attr(755,root,root) %{_bindir}/bsescm*
%attr(755,root,root) %{_bindir}/bsewavetool
%attr(755,root,root) %{_bindir}/sfidl
%attr(755,root,root) %{_libdir}/libbse-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbse-0.7.so.4
%dir %{_libdir}/bse
%dir %{_libdir}/bse/v%{version}
%dir %{_libdir}/bse/v%{version}/drivers
%attr(755,root,root) %{_libdir}/bse/v%{version}/drivers/bsemididevice-alsa.so
%attr(755,root,root) %{_libdir}/bse/v%{version}/drivers/bsepcmdevice-alsa.so
%dir %{_libdir}/bse/v%{version}/plugins
%attr(755,root,root) %{_libdir}/bse/v%{version}/plugins/*.so
%{_datadir}/%{name}
%{_datadir}/bse
# obsolete GNOME2-specific?
#%{_datadir}/application-registry/%{name}.applications
%{_datadir}/mime/packages/beast.xml
%{_datadir}/mime-info/bse.*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/beast*.png
%{_mandir}/man1/beast.1*
%{_mandir}/man1/bsescm.1*
%{_mandir}/man1/bsewavetool.1*
%{_mandir}/man1/sfidl.1*
%{_mandir}/man5/bse.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbse.so
%{_libdir}/libbse.la
%{_includedir}/birnet
%{_includedir}/bse
%{_includedir}/sfi
%{_pkgconfigdir}/bse.pc
