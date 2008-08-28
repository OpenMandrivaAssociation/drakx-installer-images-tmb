%define base_name drakx-installer-images
%define name %{base_name}-tmb
%define version 1.30
%define release %mkrel 2
%define theme	Free

%define mandriva_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' mandriva-release)

# disable empty debug rpms...
%define _enable_debug_packages  %{nil}
%define debug_package           %{nil}

Summary: DrakX installer images using kernel-tmb series
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{base_name}-%{version}.tar.bz2
Patch0:  %{name}.patch
License: GPL
Group:   Development/Other
Url:     http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%ifarch %ix86
BuildRequires: kernel-tmb-desktop586-latest >= 2.6.26.3-1mdv2009.0
%else
BuildRequires: kernel-tmb-desktop-latest >= 2.6.26.3-1mdv2009.0
%endif
%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux >= 3.51-4mdv2008.0
%endif
BuildRequires: drakx-installer-binaries >= 1.31-1mdv2009.0
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
%patch0 -p1

%build
THEME=Mandriva-%{theme} make -C images

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




