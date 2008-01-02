%define name xmms-cdread
%define version 0.14a
%define release %mkrel 5

Name: %{name}
Summary: Input plugin that reads audio data from CDs
Version: %{version}
Release: %{release}
Source: ftp://mud.stack.nl/pub/OuterSpace/willem/%{name}-%{version}.tar.bz2
URL: ftp://mud.stack.nl/pub/OuterSpace/willem
Patch: %{name}.patch	
Patch1:	xmms-cdread-0.14a-shuffle_list.patch
License: GPL
Group: Sound
Requires: xmms
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xmms-devel

%description
This is an alternative to the xmms audio CD plugin with advanced features.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p1
%patch1 -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=$RPM_BUILD_ROOT%{_libdir}/xmms/Input
rm -f %buildroot%{_libdir}/xmms/Input/libcdread.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS INSTALL TODO ChangeLog NEWS README
%{_libdir}/xmms/Input/libcdread.so

