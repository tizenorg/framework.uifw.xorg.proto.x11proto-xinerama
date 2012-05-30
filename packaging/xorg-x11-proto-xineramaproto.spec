
Name:       xorg-x11-proto-xineramaproto
Summary:    X.Org X11 Protocol xineramaproto
Version:    1.2
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-xineramaproto.manifest 
Provides:   xineramaproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .
%reconfigure --disable-shared 

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-proto-xineramaproto.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xineramaproto.pc
%{_includedir}/X11/extensions/panoramiXproto.h


