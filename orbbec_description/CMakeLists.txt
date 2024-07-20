cmake_minimum_required(VERSION 3.5)
project(orbbec_description)

find_package(ament_cmake REQUIRED)

# Install files
install(DIRECTORY 
        launch 
        meshes
        urdf
        rviz
        DESTINATION share/${PROJECT_NAME})

install(DIRECTORY
        meshes 
        DESTINATION share/${PROJECT_NAME})

ament_package()
