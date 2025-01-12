#define git 0

Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	2.1.4
%if 0%{?git:1}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	https://github.com/lxqt/lxqt-panel/releases/download/%{version}/lxqt-panel-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
Patch0:		lxqt-panel-0.8.0-omv-settings.patch
Patch1:		lxqt-panel-0.12.0-workaround-statusnotifier-crash.patch
Patch2:		lxqt-panel-2.0.0-fix-plugins-that-call-into-lxqt-panel.patch
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
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(lxqt-globalkeys)
BuildRequires:	cmake(lxqt-globalkeys-ui)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(qt6xdg)
BuildRequires:	cmake(sysstat-qt6)
BuildRequires:	cmake(Qt6Widgets)
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

%rename razorqt-panel
%rename razorqt-autosuspend
%rename razorqt-appswitcher

%description
Launcher panel for the LXQt desktop.

%files -f %{name}.lang
%dir %{_libdir}/%{name}
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_datadir}/lxqt/panel/qeyes-types/
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_mandir}/man1/lxqt-panel.1.*
%dir %{_libdir}/lxqt-panel/backend
%{_libdir}/lxqt-panel/backend/libwmbackend_kwin_wayland.so
%{_libdir}/lxqt-panel/backend/libwmbackend_wlroots.so
%{_libdir}/lxqt-panel/backend/libwmbackend_xcb.so
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
rm %{buildroot}%{_datadir}/lxqt/panel.conf
