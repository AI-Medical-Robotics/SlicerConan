# SlicerConan
3D Slicer custom extension with conan managing packages


## Default Conan Profile

We use the bash command **conan profile show default**:

~~~bash
ubuntu@ubuntu-XPS-15-9510:~/git/jopen_source/SlicerConan/slicer$ conan profile show default
Configuration for profile default:

[settings]
os=Linux
arch=x86_64
compiler=gcc
compiler.version=11.3
compiler.libcxx=libstdc++11
build_type=Debug
[options]
[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
[build_requires]
[env]
~~~
