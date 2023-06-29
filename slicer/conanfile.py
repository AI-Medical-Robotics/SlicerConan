from conans import ConanFile, CMake, tools
import os, subprocess, shutil
from glob import glob

class SlicerConan(ConanFile):
    name = "slicer"
    version = "5.2.2"
    license = "BSD-3-Clause"
    url = "https://www.slicer.org/"
    description = "3D Slicer is an open source-source software platform for medical image informatics, image processing, and three-dimensional visualization."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/Slicer/Slicer.git")
        self.run("cd Slicer && git checkout v5.2.2")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="Slicer")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="Slicer")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
