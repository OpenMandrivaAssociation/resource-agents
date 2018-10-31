Summary:	Fencing agents for cluster suite
Name:		resource-agents
Version:	3.0.17
Release:	11
Group:		System/Kernel and hardware
License:	GPLv2
Url:		http://sources.redhat.com/cluster/wiki/
Source0:	https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(libccs)
BuildRequires:	pkgconfig(libcman)
BuildRequires:	pkgconfig(liblogthread)
BuildRequires:	pkgconfig(libvirt)
BuildRequires:	pkgconfig(nss)

%description
This package contains fencing agents for use with the cman package from cluster
suite

%prep
%setup -q

%build
./configure \
        --libdir=%{_libdir} \
        --mandir=%{_mandir} \
        --prefix=%{_prefix} \
        --sbindir=%{_sbindir} \
        --incdir=%{_includedir} \
        --without_kernel_modules \
        --disable_kernel_check \
        --nssincdir=%{_includedir}/nss \
        --nsprincdir=%{_includedir}/nspr4

%make -C rgmanager/src/resources/

%install
%makeinstall_std -C rgmanager/src/resources/

%files
%{_datadir}/cluster/*

