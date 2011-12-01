%define name gnonlin
%define		gst_req 0.10
Name: 		%name
Version: 	0.10.17
Release: %mkrel 2
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
rm -rf %{buildroot}

%makeinstall_std
rm -f %{buildroot}%{_libdir}/gstreamer-*/*.*a

%check
make check

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-0.10/libgnl*
