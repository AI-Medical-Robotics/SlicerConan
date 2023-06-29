import os

from conans import ConanFile, CMake, tools
from conan.tools.layout import cmake_layout

class SlicerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.11.0"
    generators = "cmake"
    apply_env = False

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)

    def test(self):
        if not tools.cross_building(self):
            cmd = os.path.join(self.cpp.package.bindirs[0], "slicer_unit_tests")
            self.run(cmd, env="conanrun")
