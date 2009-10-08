%define base_name drakx-installer-images
%define name %{base_name}-tmb
%define version 1.44
%define release %mkrel 1
%define theme	Free

# version of kernel-tmb-desktop(586) we build against
%define kernver 2.6.31.3-1mdv

%ifarch %ix86
%define install_kernel kernel-tmb-desktop586-%kernver
%else
%define install_kernel kernel-tmb-desktop-%kernver
%endif

%define mandriva_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' mandriva-release)

# disable empty debug rpms...
%define _enable_debug_packages  %{nil}
%define debug_package           %{nil}

Summary: DrakX installer images using kernel-tmb series
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: %{base_name}-%{version}.tar.bz2
Patch0:  %{base_name}-dmraid45.patch
Patch1:  %{base_name}-tmb-binaries.patch
License: GPL
Group:   Development/Other
Url:     http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux >= 3.72
%endif
BuildRequires: %install_kernel kernel-firmware
BuildRequires: drakx-installer-binaries-tmb >= 1.42-2
BuildRequires: ldetect-lst >= 0.1.199
BuildRequires: mandriva-theme-%{theme}
BuildRequires: pcmciautils
BuildRequires: perl-XML-Parser

BuildRequires: cdrkit-genisoimage
BuildRequires: mkdosfs-with-dir
BuildRequires: mknod-m600
BuildRequires: mtools
Buildrequires: busybox
Buildrequires: ka-deploy-source-node

%description
images needed to build Mandriva installer (DrakX) using kernel-tmb series

%prep
%setup -q -n %{base_name}-%{version} 
%patch0 -p1 -b .dmraid45
%patch1 -p1 -b .binaries


%build
THEME=Mandriva-%{theme} make -C images KERNELS="%{install_kernel}"

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
make -C images install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name




