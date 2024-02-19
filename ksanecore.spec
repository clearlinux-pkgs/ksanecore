#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko.becker@kde.org)
#
Name     : ksanecore
Version  : 23.08.5
Release  : 21
URL      : https://download.kde.org/stable/release-service/23.08.5/src/ksanecore-23.08.5.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.5/src/ksanecore-23.08.5.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.5/src/ksanecore-23.08.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: ksanecore-lib = %{version}-%{release}
Requires: ksanecore-license = %{version}-%{release}
Requires: ksanecore-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : sane-backends-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
# KSaneCore
## Introduction
KSaneCore is a library that provides a Qt interface for the SANE library for scanner hardware.

%package dev
Summary: dev components for the ksanecore package.
Group: Development
Requires: ksanecore-lib = %{version}-%{release}
Provides: ksanecore-devel = %{version}-%{release}
Requires: ksanecore = %{version}-%{release}

%description dev
dev components for the ksanecore package.


%package lib
Summary: lib components for the ksanecore package.
Group: Libraries
Requires: ksanecore-license = %{version}-%{release}

%description lib
lib components for the ksanecore package.


%package license
Summary: license components for the ksanecore package.
Group: Default

%description license
license components for the ksanecore package.


%package locales
Summary: locales components for the ksanecore package.
Group: Default

%description locales
locales components for the ksanecore package.


%prep
%setup -q -n ksanecore-23.08.5
cd %{_builddir}/ksanecore-23.08.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708366881
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708366881
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksanecore
cp %{_builddir}/ksanecore-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ksanecore/48425c0d29eec28e01be25cae932f6dce8e4e278 || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksanecore/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksanecore/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/ksanecore/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ksanecore/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ksanecore/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/ksanecore-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ksanecore/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ksanecore
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KSaneCore/DeviceInformation
/usr/include/KSaneCore/Interface
/usr/include/KSaneCore/Option
/usr/include/KSaneCore/deviceinformation.h
/usr/include/KSaneCore/interface.h
/usr/include/KSaneCore/ksanecore_export.h
/usr/include/KSaneCore/ksanecore_version.h
/usr/include/KSaneCore/option.h
/usr/lib64/cmake/KSaneCore/KSaneCoreConfig.cmake
/usr/lib64/cmake/KSaneCore/KSaneCoreConfigVersion.cmake
/usr/lib64/cmake/KSaneCore/KSaneCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KSaneCore/KSaneCoreTargets.cmake
/usr/lib64/libKSaneCore.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKSaneCore.so.23.08.5
/usr/lib64/libKSaneCore.so.1
/usr/lib64/libKSaneCore.so.23.08.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksanecore/48425c0d29eec28e01be25cae932f6dce8e4e278
/usr/share/package-licenses/ksanecore/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/ksanecore/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ksanecore/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/ksanecore/b9c8ec07abddb6bfbe08cb87aa8f68c2c2a1152f
/usr/share/package-licenses/ksanecore/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ksanecore.lang
%defattr(-,root,root,-)

