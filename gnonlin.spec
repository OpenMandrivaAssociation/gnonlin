%define gstapi	1.0

Summary: 	GStreamer extension library for non-linear editing
Name: 		gnonlin
Version: 	1.2.0
Release:	1
Group: 		System/Libraries
License: 	LGPLv2+
Url:		http://gnonlin.sf.net/
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.xz

BuildRequires: pkgconfig(gstreamer-app-%{gstapi})
BuildRequires: pkgconfig(gstreamer-%{gstapi})	

Requires: 	gstreamer%{gstapi}-plugins-base 

%description
Gnonlin is a library built on top of GStreamer (http://gstreamer.net)
which provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static 

%make

%install
%makeinstall_std


%files
%doc AUTHORS COPYING.LIB README
%{_libdir}/gstreamer-%{gstapi}/libgnl.so

