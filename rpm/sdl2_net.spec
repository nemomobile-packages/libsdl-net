Summary: Simple DirectMedia Layer - Portable Network Library
Name: SDL2_net
Version: 2.0.0
Release: 2
Source: http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_net/
License: zlib
Group: System Environment/Libraries
BuildRequires: pkgconfig(sdl2)
BuildRequires: autoconf
BuildRequires: automake

%description
This is a portable network library for use with SDL.

%package devel
Summary: Simple DirectMedia Layer - Portable Network Library (Development)
Group: Development/Libraries
Requires: %{name}

%description devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to
develop SDL networked applications.

%prep
%setup -q

%build
./autogen.sh
%configure
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*

