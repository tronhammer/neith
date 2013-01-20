%define name Neith
%define version 0.1dev
%define unmangled_version 0.1dev
%define release 1

Summary: An open source python based command and control center for device management with uniform communication channels, still in dev!
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Creative Commons Attribution-Noncommercial-Share Alike license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: tronhammer <tron@tronnet.me>
Url: http://pypi.python.org/pypi/Neith

%description
=====
Neith
=====

Installs will eventually be done by a simplified installer in

	/bin/sh ./bin/install

neith
=====

This will be a command and control engine utilizing python.  It will be used to interface several language for learning purposes in order to better master the various paradigms used in common scenarios.


More to come!
-------------

Plans for the future

* client signatures
* PyDoc and PyPI configurations
* File listener
* Port listener
* Extendable command options
* Client lock down
* Key distribution and localization
* Encrypted traffic on both ends

Plans for utilization
_____________________

1) Maintaining contact with all owned devices in order to establish coordinated rules and effects based on state changes int he device
2) Allowing for commands to be sent from non local devices based on authentication measures executed by Neith
3) Providing a transportable communication layer that can be interacted with via a multitude of platforms and languages


%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
