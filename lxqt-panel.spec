Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	0.7.0
Release:	2
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	icu-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libstatgrab)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(lxqt-globalkeys)
BuildRequires:	pkgconfig(lxqt-globalkeys-ui)
BuildRequires:	pkgconfig(lxqtmount)
BuildRequires:	pkgconfig(qtxdg)
BuildRequires:	pkgconfig(sysstat)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)

%description
Launcher panel for the LXQt desktop.

%files
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_sysconfdir}/lxqt/panel.conf

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for the LXQt panel
Group:		Development/C

%description devel
Development files for the LXQt panel.

%files devel
%{_includedir}/lxqt

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

