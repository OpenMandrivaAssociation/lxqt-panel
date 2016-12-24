%define git 0

Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	0.11.0
%if %git
Release:	1.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch0:		lxqt-panel-0.8.0-omv-settings.patch

BuildRequires:	cmake
BuildRequires:	icu-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	qmake5
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
BuildRequires:	extra-cmake-modules5
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-damage)
Suggests:	xscreensaver

%rename	razorqt-panel
%rename	razorqt-autosuspend
%rename	razorqt-appswitcher

%description
Launcher panel for the LXQt desktop.

%files
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/translations/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_sysconfdir}/xdg/lxqt/panel.conf
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
%cmake_qt5

%build
%make -C build

%install
%makeinstall_std -C build
