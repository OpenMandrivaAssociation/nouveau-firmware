Summary:	Nouveau firmware files
Name:		nouveau-firmware
Version:	20091212
Release:	5
License:	GPLv2
Group:		System/Kernel and hardware
URL:		http://people.freedesktop.org/~pq/nouveau-drm/
Source0:	http://people.freedesktop.org/~pq/nouveau-drm/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This package contains the firmware for in-kernel nouveau driver
that got merged in 2.6.33-rc1.

%prep
%setup -q -n nouveau

%install
mkdir -p %{buildroot}/lib/firmware/nouveau
cp -avf * %{buildroot}/lib/firmware/nouveau

%files
%dir /lib/firmware/nouveau
/lib/firmware/nouveau/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 20091212-2mnb2
+ Revision: 666623
- mass rebuild

* Fri Dec 18 2009 Thomas Backlund <tmb@mandriva.org> 20091212-1mnb2
+ Revision: 479928
- initial release 2009-12-12
- Created package structure for nouveau-firmware.

