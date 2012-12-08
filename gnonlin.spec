%define name gnonlin
%define		gst_req 0.10
Name: 		%name
Version: 	0.10.17
Release: %mkrel 3
Summary: 	GStreamer extension library for non-linear editing

Group: 		System/Libraries
License: 	LGPLv2+
URL:		http://gnonlin.sf.net/
Source:		http://gstreamer.freedesktop.org/src/gnonlin/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: 	libgstreamer-plugins-base-devel >= %{gst_req}
BuildRequires:	automake gettext-devel
BuildRequires:	libtool
BuildRequires:	gtk-doc
#gw for the checks:
BuildRequires:	gstreamer0.10-plugins-good
Obsoletes: gnonlin-devel

%description
Gnonlin is a library built on top of GStreamer (http://gstreamer.net)
which provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%prep
%setup -q

%build
%configure2_5x \
	--with-package-name='Mandriva %name package' \
	--with-package-origin='http://www.mandriva.com/'
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-*/*.*a

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-0.10/libgnl*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.17-2mdv2011.0
+ Revision: 664892
- mass rebuild

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.17-1
+ Revision: 632300
- update to new version 0.10.17

* Tue Sep 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2011.0
+ Revision: 576501
- fix build
- update to new version 0.10.16

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 0.10.15-1mdv2010.1
+ Revision: 516975
- update to new version 0.10.15

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2010.1
+ Revision: 504266
- new version
- spec file fix

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-1mdv2010.0
+ Revision: 432578
- update to new version 0.10.13

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-1mdv2010.0
+ Revision: 414760
- new version 0.10.12

* Thu Aug 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.11.3-1mdv2010.0
+ Revision: 410553
- new prerelease
- enable checks

* Sun May 24 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.11-1mdv2010.0
+ Revision: 379185
- update to new version 0.10.11

* Mon May 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.10.3-1mdv2010.0
+ Revision: 377308
- Add gtk-doc BuildRequires
- Update to new pre-release version 0.10.10.3

* Tue Nov 04 2008 Funda Wang <fwang@mandriva.org> 0.10.10-1mdv2009.1
+ Revision: 299678
- use system libtool to build
- add back customization
- New version 0.10.10

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10.9-5mdv2009.0
+ Revision: 246475
- rebuild

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.9-3mdv2008.1
+ Revision: 187389
- add Mandriva branding

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.10.9-1mdv2008.1
+ Revision: 136451
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 09 2007 Götz Waschk <waschk@mandriva.org> 0.10.9-1mdv2008.0
+ Revision: 60718
- new version

* Mon May 07 2007 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2008.0
+ Revision: 23971
- new version


* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2007.0
+ Revision: 114472
- new version

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.10.6-2mdv2007.1
+ Revision: 87905
- bot rebuild
- Import gnonlin

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2007.1
- New version 0.10.6

* Sat Jul 22 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2007.0
- New release 0.10.5

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.0
- Rebuild

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdk
- New release 0.10.4

* Wed Apr 26 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- New release 0.10.3

* Sat Apr 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- fix file list
- new source URL
- New release 0.10.1

* Thu Feb 02 2006 Götz Waschk <waschk@mandriva.org> 0.10.0.5-1mdk
- New release 0.10.0.5

* Thu Jan 12 2006 Götz Waschk <waschk@mandriva.org> 0.10.0.3-3mdk
- fix buildrequires

* Sat Dec 31 2005 Götz Waschk <waschk@mandriva.org> 0.10.0.3-2mdk
- fix buildrequires

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.10.0.3-1mdk
- drop the devel package
- gst 0.10
- New release 0.10.0.3
- use mkrel

* Thu Jun 30 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdk
- initial package

* Mon Mar 21 2005 Edward Hervey <bilboed at bilboed dot com>
- First version of spec

