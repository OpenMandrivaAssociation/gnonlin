%define gstapi	0.10

Summary: 	GStreamer extension library for non-linear editing
Name: 		gnonlin
Version: 	0.10.17
Release:	10
Group: 		System/Libraries
License: 	LGPLv2+
Url:		http://gnonlin.sf.net/
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/%{name}-%{version}.tar.bz2

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
%configure2_5x \
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

