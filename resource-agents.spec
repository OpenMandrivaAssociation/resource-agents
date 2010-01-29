Name: resource-agents
Version: 3.0.7
Release: %mkrel 1
Summary: Fencing agents for cluster suite
Group: System/Kernel and hardware
URL: http://sources.redhat.com/cluster/wiki/
Source: ftp://sources.redhat.com/pub/cluster/releases/%{name}-%{version}.tar.gz
#Patch0: fence-agents-remove-nonexistent-subdirs.patch
License: GPLv2
Conflicts: cman < 3.0.0
BuildArch: noarch
BuildRequires: logthread-devel ccs-devel nss-devel cman-devel libvirt-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
This package contains fencing agents for use with the cman package from cluster
suite


%prep
%setup -q
#patch0 -p1

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
rm -Rf %{buildroot}
%makeinstall_std -C rgmanager/src/resources/

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/cluster/*
