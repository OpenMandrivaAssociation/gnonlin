%define name gnonlin
%define		gst_req 0.10
Name: 		%name
Version: 	0.10.9
Release: %mkrel 5
Summary: 	GStreamer extension library for non-linear editing

Group: 		System/Libraries
License: 	LGPL
URL:		http://gnonlin.sf.net/
Source:		http://gstreamer.freedesktop.org/src/gnonlin/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: 	libgstreamer-plugins-base-devel >= %{gst_req}
BuildRequires: automake1.8 gettext-devel
Provides: gnonlin-devel
Obsoletes: gnonlin-devel

%description
Gnonlin is a library built on top of GStreamer (http://gstreamer.net)
which provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%package devel
Summary: 	Development headers for the gnonlin libraries
Group:          Development/C
Requires:       %{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to build applications with gnonlin.


%prep
%setup -q
aclocal-1.8 -I common/m4
autoconf
automake-1.8 -a -c

%build
%configure2_5x \
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \


%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-*/*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-0.10/libgnl*


