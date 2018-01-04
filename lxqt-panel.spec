%define git 0

Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	0.12.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	3
Source0:	https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(lxqt-globalkeys)
BuildRequires:	cmake(lxqt-globalkeys-ui)
BuildRequires:	cmake(lxqt-build-tools)
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
BuildRequires:	pkgconfig(xcb-damage)
Requires:	lxqt-l10n
Suggests:	xscreensaver

%rename	razorqt-panel
%rename	razorqt-autosuspend
%rename	razorqt-appswitcher

%description
Launcher panel for the LXQt desktop.

%files
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_sysconfdir}/xdg/lxqt/panel.conf
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_sysconfdir}/xdg/menus/lxqt-applications.menu
%{_datadir}/desktop-directories/lxqt-leave.directory
%{_datadir}/desktop-directories/lxqt-settings.directory
%{_mandir}/man1/lxqt-panel.1.*

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
%if %git
%setup -q -n %{name}-%{git}
%else
%setup -q
%endif
%apply_patches
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
