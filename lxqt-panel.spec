Name: lxqt-panel
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: Launcher panel for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel
BuildRequires: cmake(lxqt_globalkeys)
BuildRequires: cmake(lxqt_globalkeys_ui)
BuildRequires: pkgconfig(libstatgrab)

%description
Launcher panel for the LXQt desktop

%package devel
Summary: Development files for the LXQt panel
Group: Development/C

%description devel
Development files for the LXQt panel

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_sysconfdir}/lxqt/panel.conf
%{_bindir}/lxqt-panel
%{_datadir}/lxqt/lxqt-panel
%{_libdir}/lxqt-panel

%files devel
%{_includedir}/lxqt
