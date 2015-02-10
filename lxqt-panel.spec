%define git 0
Summary:	Launcher panel for the LXQt desktop
Name:		lxqt-panel
Version:	0.9.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	3
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch0:		lxqt-panel-0.8.0-omv-settings.patch
BuildRequires:	cmake
BuildRequires:	icu-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libstatgrab)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(lxqt-globalkeys)
BuildRequires:	cmake(lxqt-globalkeys-ui)
BuildRequires:	cmake(lxqtmount)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(sysstat-qt5)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	extra-cmake-modules5
BuildRequires:	desktop-file-utils
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
%{_sysconfdir}/qt5

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
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

# workaround
sed -i -e 's/Comment\[ru_RU\].*//' -e 's/Name\[ru_RU\].*//' %{buildroot}%{_datadir}/lxqt/lxqt-panel/mount.desktop
sed -i -e 's/Comment\[de\].*//' -e 's/Name\[de\].*//' %{buildroot}%{_datadir}/lxqt/lxqt-panel/networkmonitor.desktop

for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
	# Exclude category as been Service 
	desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done
