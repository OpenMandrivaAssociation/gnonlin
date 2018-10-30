%define gstapi	1.0

Summary: 	GStreamer extension library for non-linear editing
Name: 		gnonlin
Version: 	1.4.0
Release:	3
Group: 		System/Libraries
License: 	LGPLv2+
Url:		http://gnonlin.sf.net/
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/%{name}-%{version}.tar.xz

BuildRequires: 	gstreamer%{gstapi}-plugins-good
BuildRequires:	gstreamer%{gstapi}-tools
BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires: 	pkgconfig(gstreamer-plugins-base-%{gstapi})

%description
Gnonlin is a library built on top of GStreamer (http://gstreamer.net)
which provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-package-name='Mandriva %{name} package' \
	--with-package-origin='http://www.mandriva.com/'
%make

%install
%makeinstall_std

#%check
#make check

%files
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-%{gstapi}/libgnl.so

