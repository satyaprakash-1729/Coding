cmake_minimum_required(VERSION 2.8)
project( temp )
find_package( OpenCV REQUIRED )
add_executable( temp temp.cpp )
target_link_libraries( temp ${OpenCV_LIBS} )