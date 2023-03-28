Name:           kddockwidgets
Version:        1.6.0
Release:        1%{?dist}
Summary:        Qt dock widget library

License:        GPL-3.0-only
URL:            https://github.com/KDAB/KDDockWidgets
Source0:        %{url}%{version}/archive/refs/tags/v1.6.0.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel

%description
Qt dock widget library written by KDAB, suitable for replacing QDockWidget
and implementing advanced functionalities missing in Qt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n KDDockWidgets-%{version}


%build
%cmake -G Ninja
%cmake_build


%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc

%files
%license LICENSE.GPL.txt LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets.so.*

%files devel
%{_includedir}/kddockwidgets
%{_libdir}/cmake/KDDockWidgets
%{_libdir}/libkddockwidgets.so
%{_libdir}/qt5/mkspecs/modules/qt_KDDockWidgets.pri

%changelog
* Fri Mar 24 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-1
- Initial packaging.
