Name: resource-agents
Version: 3.0.17
Release: 4
Summary: Fencing agents for cluster suite
Group: System/Kernel and hardware
URL: http://sources.redhat.com/cluster/wiki/
Source: https://fedorahosted.org/releases/c/l/cluster/resource-agents-%{version}.tar.gz
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.17-2mdv2011.0
+ Revision: 669420
- mass rebuild

* Wed Oct 13 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.17-1mdv2011.0
+ Revision: 585433
- update to new version 3.0.17

* Tue Sep 07 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.16-1mdv2011.0
+ Revision: 576590
- update to new version 3.0.16

* Tue May 04 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.11-1mdv2010.1
+ Revision: 542054
- update to new version 3.0.11

* Fri Jan 29 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.7-1mdv2010.1
+ Revision: 497878
- update to new version 3.0.7

* Mon Jan 04 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.6-1mdv2010.1
+ Revision: 486173
- update to new version 3.0.6

* Wed Dec 02 2009 Buchan Milne <bgmilne@mandriva.org> 3.0.5-1mdv2010.1
+ Revision: 472568
- update to new version 3.0.5

* Fri Nov 20 2009 Buchan Milne <bgmilne@mandriva.org> 3.0.4-1mdv2010.1
+ Revision: 467614
- update to new version 3.0.4

* Wed Oct 14 2009 Buchan Milne <bgmilne@mandriva.org> 3.0.3-1mdv2010.0
+ Revision: 457381
- New version 3.0.3
- import resource-agents


