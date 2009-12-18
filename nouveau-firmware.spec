
Summary:	Nouveau firmware files
Name:   	nouveau-firmware
Version:	20091212
Release:	%manbo_mkrel 1
License:	GPLv2
Group:  	System/Kernel and hardware
URL:    	http://people.freedesktop.org/~pq/nouveau-drm/
Source0: 	http://people.freedesktop.org/~pq/nouveau-drm/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
This package contains the firmware for in-kernel nouveau driver
that got merged in 2.6.33-rc1.

%prep
%setup -q -n nouveau

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/nouveau
cp -avf * %{buildroot}/lib/firmware/nouveau

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir /lib/firmware/nouveau
/lib/firmware/nouveau/*
