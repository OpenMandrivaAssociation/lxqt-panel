#define git 0

Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	2.3.1
%if 0%{?git:1}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	https://github.com/lxqt/lxqt-panel/releases/download/%{version}/lxqt-panel-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
BuildRequires:	cmake(ECM)
BuildRequires:	icu-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libstatgrab)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(lxqt-globalkeys)
BuildRequires:	cmake(lxqt-globalkeys-ui)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(qt6xdg)
BuildRequires:	cmake(sysstat-qt6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(dbusmenu-lxqt)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-damage)
BuildRequires:	cmake(lxqt-menu-data)
BuildRequires:	cmake(LayerShellQt)
Requires:	lxqt-menu-data
Requires: kf6-kwindowsystem-backend-x11 
Suggests:	xscreensaver

Requires:	%{name}-backend = %{EVRD}
Requires:	(%{name}-kwin = %{EVRD} if kwin)
Requires:	(%{name}-wayfire = %{EVRD} if wayfire)
Requires:	(%{name}-wlroots = %{EVRD} if %{mklibname wlroots})
Requires:	(%{name}-xcb = %{EVRD} if xlibre)

%rename razorqt-panel
%rename razorqt-autosuspend
%rename razorqt-appswitcher

%patchlist
lxqt-panel-0.8.0-omv-settings.patch
lxqt-panel-0.12.0-workaround-statusnotifier-crash.patch
lxqt-panel-2.0.0-fix-plugins-that-call-into-lxqt-panel.patch
lxqt-panel-compile.patch

%description
Launcher panel for the LXQt desktop.

%package kwin
Summary:	KWin Wayland backend for the LXQt desktop
Requires:	%{name} = %{EVRD}
Requires:	kwin
Provides:	%{name}-backend = %{EVRD}

%description kwin
KWin Wayland backend for the LXQt desktop

%files kwin
%{_libdir}/lxqt-panel/backend/libwmbackend_kwin_wayland.so

%package wayfire
Summary:	Wayfire backend for the LXQt desktop
Requires:	%{name} = %{EVRD}
Requires:	wayfire
Provides:	%{name}-backend = %{EVRD}

%description wayfire
Wayfire backend for the LXQt desktop

%files wayfire
%{_libdir}/lxqt-panel/backend/libwmbackend_wayfire.so

%package wlroots
Summary:	WLRoots backend for the LXQt desktop
Requires:	%{name} = %{EVRD}
Requires:	%{mklibname wlroots}
Provides:	%{name}-backend = %{EVRD}

%description wlroots
WLRoots backend for the LXQt desktop

%files wlroots
%{_libdir}/lxqt-panel/backend/libwmbackend_wlroots.so

%package xcb
Summary:	Xcb (X11) backend for the LXQt desktop
Requires:	%{name} = %{EVRD}
Provides:	%{name}-backend = %{EVRD}

%description xcb
Xcb (X11) backend for the LXQt desktop

%files xcb
%{_libdir}/lxqt-panel/backend/libwmbackend_xcb.so

%files -f %{name}.lang
%dir %{_libdir}/%{name}
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_datadir}/lxqt/panel/qeyes-types/
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_mandir}/man1/lxqt-panel.1.*
%dir %{_libdir}/lxqt-panel/backend
%{_datadir}/applications/lxqt-panel.desktop
%dir %lang(arn) %{_datadir}/lxqt/translations/lxqt-panel

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
%autosetup -p1 -n %{name}-%{?git:%{git}}%{!?git:%{version}}
%cmake -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

# We get this from distro-release
rm %{buildroot}%{_sysconfdir}/xdg/lxqt/panel.conf
