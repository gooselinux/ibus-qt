Name:       ibus-qt
Version:    1.3.0
Release:    2%{?dist}.goose.1
Summary:    Qt IBus library and Qt input method plugin
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Patch0:     ibus-qt-HEAD.patch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  qt4-devel >= 4.5
BuildRequires:  dbus-devel >= 1.2
BuildRequires:  libicu-devel >= 4.0
BuildRequires:  doxygen >= 1.6
Requires:   ibus >= 1.3

%description
Qt IBus library and Qt input method plugin.

%package devel
Summary:    Development tools for ibus qt
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The ibus-qt-devel package contains the header files for ibus qt library.

%package docs
Summary:    Development documents for ibus qt
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description docs
The ibus-qt-docs package contains developer documentation for ibus qt library.

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p1

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_usr} \
    -DLIBDIR=%{_libdir}
make \
    VERBOSE=1 \
    C_DEFINES="$RPM_OPT_FLAGS" \
    CXX_DEFINES="$RPM_OPT_FLAGS" \
    %{?_smp_mflags}
make docs

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# %find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README INSTALL
%{_libdir}/libibus-qt.so.*
%{_libdir}/qt4/plugins/inputmethods/libqtim-ibus.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libibus-qt.so

%files docs
%defattr(-,root,root,-)
%doc docs/html

%changelog
* Mon Jan  1 2012 Clint Savage <herlo@gooseproject.org> - 1.3.0-2.goose.1
- Adjusted BuildRequires to qt4-devel to pull in proper dependencies

* Fri Jul 23 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.0-2
- Fix Bug 608966 - uncommitted text color is not properly set in kwrite
  Resolves: #608966

* Mon Mar 29 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Thu Dec 17 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091217-1
- Update to 1.2.0.20091217.

* Sun Dec 06 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091206-1
- Update to 1.2.0.20091206.

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0.20091014-2
- rebuild (for qt-4.6.0-rc1, f13+)

* Wed Oct 14 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091014-1
- Update to 1.2.0.20091014.

* Sat Aug 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090822-2
- Update the tarball
- Link qt immodule with libicu

* Sat Aug 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090822-1
- Update to 1.2.0.2009822
- Fix compose key problem.

* Mon Jul 27 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090728-1
- The first version.
