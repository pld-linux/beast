Summary:	BEAST (the Bedevilled Audio System)
Summary(pl):	System d¼wiêku BEAST (Bedevilled Audio System)
Name:		beast
Version:	0.6.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://beast.gtk.org/beast-ftp/v0.6/%{name}-%{version}.tar.gz
# Source0-md5:	84e5bb136b261d47e6a15ef3539b3bcb
Source1:	%{name}.desktop
URL:		http://beast.gtk.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gtk+2-devel >=  2.4.0
BuildRequires:	guile-devel >= 1.6
BuildRequires:	libart_lgpl-devel >= 2.3.8
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libmad-devel >= 0.14.2
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BEAST (the Bedevilled Audio System) is a GTK+/GNOME based front-end to
BSE (the Bedevilled Sound Engine). BSE is a shared library that comes
with the necessary framework to simulate audio synthesis (modular
synthesis) in realtime and allow for song composition.

%description -l pl
System d¼wiêku BEAST (Bedevilled Audio System) to oparty na GTK+/GNOME
frontend dla silnika d¼wiêku BSE (Bedevilled Sound Engine). BSE to
biblioteka wspó³dzielona, która przychodzi wraz ze szkieletem
potrzebnym do symulacji syntezy d¼wiêku (syntezy modularnej) w czasie
rzeczywistym oraz umo¿liwienia komponowania piosenek.

%package devel
Summary:	Header files for Beast
Summary(pl):	Pliki nag³ówkowe dla Beast
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Beast.

%description devel -l pl
Pliki nag³ówkowe dla Beast.

%prep
%setup -q

%build
rm -f aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-devdsp \
	--enable-debug=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/bse
%dir %{_libdir}/bse/v%{version}
%dir %{_libdir}/bse/v%{version}/plugins
%{_mandir}/man1/*
%attr(755,root,root) %{_libdir}/bse/v%{version}/plugins/*.so
%{_datadir}/%{name}
%{_datadir}/bse
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/mime-info/bse.*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
%{_datadir}/mime/audio/x-bse.xml
%{_datadir}/mime/audio/x-bsewave.xml
%{_datadir}/mime/packages/beast.xml


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/bse
%{_includedir}/bsw
%{_includedir}/sfi
%{_mandir}/man3/*
%{_pkgconfigdir}/*.pc
# do we really need this?
%{_libdir}/bse/v%{version}/plugins/*.la
