%define name gnonlin
%define		gst_req 0.10
Name: 		%name
Version: 	0.10.11
Release: %mkrel 1
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
Obsoletes: gnonlin-devel

%description
Gnonlin is a library built on top of GStreamer (http://gstreamer.net)
which provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x \
	--with-package-name='Mandriva %name package' \
	--with-package-origin='http://www.mandriva.com/'
%make LIBTOOL=%_bindir/libtool

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std LIBTOOL=%_bindir/libtool
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-*/*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-0.10/libgnl*
