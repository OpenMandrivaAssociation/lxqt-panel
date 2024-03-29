#define git 0

Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	1.4.0
%if 0%{?git:1}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	https://github.com/lxqt/lxqt-panel/releases/download/%{version}/lxqt-panel-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch0:		lxqt-panel-0.8.0-omv-settings.patch
Patch1:		lxqt-panel-0.12.0-workaround-statusnotifier-crash.patch
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
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(lxqt-globalkeys)
BuildRequires:	cmake(lxqt-globalkeys-ui)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(sysstat-qt5)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(dbusmenu-qt5)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires:	cmake(lxqt-menu-data)
Requires:	lxqt-menu-data
Requires: kwindowsystem-x11 
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
%{_datadir}/lxqt/panel.conf
%{_datadir}/lxqt/panel/qeyes-types/
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_mandir}/man1/lxqt-panel.1.*
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
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name
