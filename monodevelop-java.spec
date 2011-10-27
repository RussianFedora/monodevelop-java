Summary:        MonoDevelop java Addin
Name:           monodevelop-java
Version:        2.8.1
Release:        1%{?dist}.R
License:        GPLv2+
Group:          Development/Tools
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
URL:            http://www.monodevelop.com

BuildRequires:  mono-devel >= 2.6
BuildRequires:  monodevelop-devel >= 2.8.1
BuildRequires:  mono-addins-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gnome-desktop-sharp-devel
BuildRequires:  gettext
Requires:       monodevelop >= 2.8.1


%description
Java Addin for MonoDevelop.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig
Group:          Development/Libraries

%description devel
Development package for %{name}

%prep
%setup -q
##sed magic to get rid of all of the silly $prefix/lib stuff
find . -name Makefile -or -name Makefile.in -or -name Makefile.am -or -name configure -or -name configure.in -or -name \*.pc.in \
       -or -name \*.in -or -name \*.xml -or -name Makefile.include -or -name \*.make \
       | while read f ;
         do
           sed -i -e 's!$(prefix)/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!@prefix@/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!/usr/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!${exec_prefix}/lib/!%{_libdir}/!' "$f" ;
         done

%build
%{_configure} --prefix=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libdir}/monodevelop/AddIns/JavaBinding/JavaBinding*
%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/monodevelop-java.pc

%changelog
* Thu Oct 27 2011 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.1-1.R
- Update to 2.8.1
