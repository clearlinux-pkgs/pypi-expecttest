#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-expecttest
Version  : 0.1.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/8e/e6/584ea2be6cf46a7f86991353c8c7de8321327a50c9a3e6cd120abc904c3f/expecttest-0.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/e6/584ea2be6cf46a7f86991353c8c7de8321327a50c9a3e6cd120abc904c3f/expecttest-0.1.3.tar.gz
Summary  : No summary provided
Group    : Development/Tools
License  : MIT
Requires: pypi-expecttest-license = %{version}-%{release}
Requires: pypi-expecttest-python = %{version}-%{release}
Requires: pypi-expecttest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# expecttest [![PyPI version](https://badge.fury.io/py/expecttest.svg)](https://badge.fury.io/py/expecttest)

%package license
Summary: license components for the pypi-expecttest package.
Group: Default

%description license
license components for the pypi-expecttest package.


%package python
Summary: python components for the pypi-expecttest package.
Group: Default
Requires: pypi-expecttest-python3 = %{version}-%{release}

%description python
python components for the pypi-expecttest package.


%package python3
Summary: python3 components for the pypi-expecttest package.
Group: Default
Requires: python3-core
Provides: pypi(expecttest)

%description python3
python3 components for the pypi-expecttest package.


%prep
%setup -q -n expecttest-0.1.3
cd %{_builddir}/expecttest-0.1.3
pushd ..
cp -a expecttest-0.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405971
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-expecttest
cp %{_builddir}/expecttest-0.1.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-expecttest/f3691350b31505bc67cb17e117547c91280a1875
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-expecttest/f3691350b31505bc67cb17e117547c91280a1875

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
