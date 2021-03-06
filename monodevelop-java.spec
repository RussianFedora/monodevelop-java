Name:           monodevelop-java
Version:        2.8.8.4
Release:        2%{?dist}
Summary:        MonoDevelop java Addin
Summary(ru):    Дополнение Java для MonoDevelop

License:        GPLv2+
Group:          Development/Tools
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
URL:            http://www.monodevelop.com

BuildRequires:  mono-devel >= 2.6
BuildRequires:  monodevelop-devel >= %{version}
BuildRequires:  mono-addins-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gnome-desktop-sharp-devel
BuildRequires:  gettext
Requires:       monodevelop >= %{version}


%description
Java Addin for MonoDevelop.

%description -l ru
Биндинги Java для MonoDevelop.

%package devel
Summary:        Development files for %{name}
Summary(ru):    Файлы разработки для %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release} pkgconfig
Group:          Development/Libraries

%description devel
Development package for %{name}

%description devel -l ru
Пакет разработки для %{name}

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
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_libdir}/monodevelop/AddIns/JavaBinding/JavaBinding*
%doc COPYING

%files devel
%{_libdir}/pkgconfig/monodevelop-java.pc

%changelog
* Mon Feb 25 2013 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.8.4-2.R
- Fresh build

* Sat Aug 18 2012 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.8.4-1.R
- Update to 2.8.8.4

* Tue Jan 24 2012 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.5-1.R
- Update to 2.8.5

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.1-2.R
- Added description in russian language

* Thu Oct 27 2011 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.1-1.R
- Update to 2.8.1
