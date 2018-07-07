Name:          click
Version:        1.0
Release:        1%{?dist}
Summary:        Click is a simplified packaging format

License:        Custom
URL:            https://ubports.io
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  vala
Requires:       libgee
Requires: 	json-glib


%description
Click is a simplified packaging format.

%prep
%setup -q -n %{name}-%{version}/click


%build
./autogen.sh

./configure --prefix=/usr --disable-packagekit

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%defattr(-,root,root)
/usr/lib/click/libclickpreload.so
/usr/lib/girepository-1.0/Click-0.4.typelib
/usr/lib/systemd/system/click-system-hooks.service
/usr/lib/systemd/user/click-user-hooks.service
/usr/lib/libclick-0.4.so.0.4.0
/usr/lib/python3.6/site-packages/click_package/osextras.py
/usr/lib/python3.6/site-packages/click_package/paths.py
/usr/lib/python3.6/site-packages/click_package/framework.py
/usr/lib/python3.6/site-packages/click_package/__init__.py
/usr/lib/python3.6/site-packages/click_package/build.py
/usr/lib/python3.6/site-packages/click_package/json_helpers.py
/usr/lib/python3.6/site-packages/click_package/arfile.py
/usr/lib/python3.6/site-packages/click_package/tests/test_build.py
/usr/lib/python3.6/site-packages/click_package/tests/test_paths.py
/usr/lib/python3.6/site-packages/click_package/tests/test_chroot.py
/usr/lib/python3.6/site-packages/click_package/tests/test_framework.py
/usr/lib/python3.6/site-packages/click_package/tests/test_static.py
/usr/lib/python3.6/site-packages/click_package/tests/test_query.py
/usr/lib/python3.6/site-packages/click_package/tests/__init__.py
/usr/lib/python3.6/site-packages/click_package/tests/test_database.py
/usr/lib/python3.6/site-packages/click_package/tests/test_hooks.py
/usr/lib/python3.6/site-packages/click_package/tests/config.py
/usr/lib/python3.6/site-packages/click_package/tests/test_scripts.py
/usr/lib/python3.6/site-packages/click_package/tests/helpers.py
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_scripts.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_paths.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_framework.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/config.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/gimock.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_database.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_arfile.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/helpers.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_build.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_hooks.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_query.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_user.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/gimock_types.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_install.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_static.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_chroot.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/__pycache__/test_osextras.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/test_user.py
/usr/lib/python3.6/site-packages/click_package/tests/gimock_types.py
/usr/lib/python3.6/site-packages/click_package/tests/test_osextras.py
/usr/lib/python3.6/site-packages/click_package/tests/test_install.py
/usr/lib/python3.6/site-packages/click_package/tests/gimock.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_signatures.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_build.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_chroot.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_contents.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_info.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_frameworks.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_list.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/__init__.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_buildsource.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/helpers.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_verify.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_contents.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_list.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_frameworks.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_build_core_apps.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_buildsource.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_signatures.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/helpers.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_build.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_install.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_chroot.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_info.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/__pycache__/test_hook.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_hook.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_build_core_apps.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_install.py
/usr/lib/python3.6/site-packages/click_package/tests/integration/test_verify.py
/usr/lib/python3.6/site-packages/click_package/tests/test_arfile.py
/usr/lib/python3.6/site-packages/click_package/__pycache__/install.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/paths.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/framework.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/chroot.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/preinst.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/osextras.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/arfile.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/versions.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/json_helpers.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/__pycache__/build.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/preinst.py
/usr/lib/python3.6/site-packages/click_package/versions.py
/usr/lib/python3.6/site-packages/click_package/chroot.py
/usr/lib/python3.6/site-packages/click_package/commands/list.py
/usr/lib/python3.6/site-packages/click_package/commands/hook.py
/usr/lib/python3.6/site-packages/click_package/commands/desktophook.py
/usr/lib/python3.6/site-packages/click_package/commands/info.py
/usr/lib/python3.6/site-packages/click_package/commands/register.py
/usr/lib/python3.6/site-packages/click_package/commands/framework.py
/usr/lib/python3.6/site-packages/click_package/commands/__init__.py
/usr/lib/python3.6/site-packages/click_package/commands/build.py
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/install.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/buildsource.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/pkgdir.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/register.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/unregister.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/framework.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/chroot.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/contents.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/verify.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/hook.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/list.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/info.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/desktophook.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/__pycache__/build.cpython-36.pyc
/usr/lib/python3.6/site-packages/click_package/commands/unregister.py
/usr/lib/python3.6/site-packages/click_package/commands/buildsource.py
/usr/lib/python3.6/site-packages/click_package/commands/pkgdir.py
/usr/lib/python3.6/site-packages/click_package/commands/chroot.py
/usr/lib/python3.6/site-packages/click_package/commands/contents.py
/usr/lib/python3.6/site-packages/click_package/commands/install.py
/usr/lib/python3.6/site-packages/click_package/commands/verify.py
/usr/lib/python3.6/site-packages/click_package/install.py
/usr/lib/python3.6/site-packages/click-0.4.47+ubports-py3.6.egg-info/dependency_links.txt
/usr/lib/python3.6/site-packages/click-0.4.47+ubports-py3.6.egg-info/top_level.txt
/usr/lib/python3.6/site-packages/click-0.4.47+ubports-py3.6.egg-info/SOURCES.txt
/usr/lib/python3.6/site-packages/click-0.4.47+ubports-py3.6.egg-info/requires.txt
/usr/lib/python3.6/site-packages/click-0.4.47+ubports-py3.6.egg-info/PKG-INFO
/usr/lib/pkgconfig/click-0.4.pc
/usr/include/click-0.4/click.h
/usr/etc/click/databases/10_core.conf
/usr/etc/click/databases/99_default.conf
/usr/etc/click/databases/20_custom.conf
/usr/etc/init/click-system-hooks.conf
/usr/etc/schroot/click/fstab
/usr/share/man/man1/dh_click.1.gz
/usr/share/upstart/sessions/click-user-hooks.conf
/usr/share/gir-1.0/Click-0.4.gir
/usr/share/debhelper/autoscripts/postinst-click
/usr/share/debhelper/autoscripts/prerm-click
/usr/share/perl5/vendor_perl/Debian/Debhelper/Sequence/click.pm
/usr/bin/dh_click
/usr/bin/click

%changelog
* Sat Jul  7 2018 abhishek9650 <abhishek.mudgal.59@gmail.com>
- 
