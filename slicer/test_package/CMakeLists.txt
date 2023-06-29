cmake_minimum_required(VERSION 3.15)
project(slicer_unit_tests CXX)
set(CMAKE_CXX_STANDARD 20)

include(${CMAKE_BINARY_DIR}/generators/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(Slicer)
# include(${Slicer_USE_FILE})

set(SRCS
    src/test_slicer.cpp
)

message("CONAN_TARGETS = ${CONAN_TARGETS}")
message("CONAN_INCLUDE_DIRS = ${CONAN_INCLUDE_DIRS}")

add_executable(${PROJECT_NAME} ${SRCS})
target_link_libraries(${PROJECT_NAME}
CONAN_PKG::slicer
CONAN_PKG::gtest
)

target_include_directories(${PROJECT_NAME}
${GTEST_INCLUDE_DIRS}
)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME})
