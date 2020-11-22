Name:		cartographer_ros
Version:	1.0.0
Release:	0
Summary:	This is ROS melodic cartographer Package
License:	GPL
URL:		https://github.com/ros-gbp/cartographer-release/archive/release/melodic/cartographer/
Source0:	https://github.com/ros-gbp/cartographer-release/archive/release/melodic/cartographer/1.0.0.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	lz4-devel
BuildRequires:	bzip2-devel
BuildRequires:	python-devel
BuildRequires:	python-setuptools
#Requires:  python-empy
BuildRequires:	openssl-devel
BuildRequires:	curl-devel
BuildRequires:	curl
#BuildRequires:	gcc-gfortran
#BuildRequires:	openblas-devel
#BuildRequires:	sqlite-devel
#BuildRequires:	fftw-devel
BuildRequires:	boost-devel
BuildRequires:	uuid-devel
BuildRequires:	uuid
BuildRequires:	libuuid-devel
#BuildRequires:	uuid-devel
#BuildRequires:	python3-devel
#BuildRequires:	boost-python3-devel

BuildRequires:  gmock-devel
BuildRequires:  suitesparse-devel
BuildRequires:  lua-devel
BuildRequires:  protobuf-devel
BuildRequires:  cairo-devel
BuildRequires:  gflags-devel
BuildRequires:  freeglut-devel
BuildRequires:  libXt-devel
BuildRequires:  tinyxml-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXaw-devel
BuildRequires:  assimp-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  libatomic
BuildRequires:  python2-qt5-devel
BuildRequires:  lz4-devel
BuildRequires:  sphinx

%description
This is ROS melodic ros_comm Package.

%prep
%setup
#cd catkin-0.7.26/




#%build

#pwd
#mkdir build/
#cd build/ && cmake ..



%install
pwd
 
#mkdir -p build/
#cd build/
#cmake ..
#cd ..

cd src/
cd 3rdparty/ 

cd empy-3.3.4/
python setup.py install --user
cd ..

cd six-1.15.0/
python setup.py install --user
cd ..

cd setuptools_scm-4.1.2/
python setup.py install --user
cd ..

cd python-dateutil-2.8.1/
python setup.py install --user
cd ..

cd pyparsing-2.4.7/
python setup.py install --user
cd ..

cd docutils-0.16/
python setup.py install --user
cd ..

cd catkin_pkg-0.4.22/
python setup.py install --user
cd ..

#for std_msgs
cd PyYAML-5.3.1/
python setup.py install --user
cd ..

cd distro-1.5.0/
python setup.py install --user
cd ..

cd rospkg-1.2.8/
python setup.py install --user
cd ..



cd console_bridge/
mkdir build/
cd build/
cmake ..
make 
make install
cd ..
cd ..

cd poco/
mkdir cmake-build/
mkdir cmake-release/
cd cmake-build/
cmake ..
make install
cd ..
cd ..


cd tinyxml2/
mkdir build
cd build
cmake ..
make install
cd ..
cd ..


cd urdfdom_headers/
mkdir build
cd build
cmake ..
make install
cd ..
cd ..

cd eigen-3.3.7/
mkdir build
cd build
cmake ..
make install
cd ..
cd ..

cd orocos_kdl/
mkdir build
cd build
cmake ..
make install
cp -r  ../../eigen-3.3.7/build/eigen/include/eigen3/* orocos_kdl/include/
cd ..
cd ..


cd abseil-cpp/
mkdir build
mkdir install
cd build
cmake ..
make install

cd ..
cd install 
ls -FR

cd ..
cd ..



cd glog/
mkdir build
mkdir install
cd build
cmake ..
make install
cd ..
cd ..



cd ceres-solver-1.13.0/
mkdir build
mkdir install
cd build
cmake ..
make install

cd ..
cd install 
ls -FR

cd ..
cd ..


cd ticpp/
mkdir build
cd build
cmake ..
make -j8
cd ..
cd ..



cd urdfdom/
mkdir build
mkdir install
cd build
cmake ..
make install
cd ..
cd ..


cd flann-1.9.1/
mkdir build
mkdir install
cd build
cmake ..
make install
cd ..
cd ..


#cd VTK/
#mkdir build
#mkdir install
#cp -r ExternalData/ build/  
#cd build
#cmake ..
#make install
#cd ..
#cd ..



cd pcl/
mkdir build
mkdir install
cd build
cmake ..
make install

cd ..
cd ..


cd ogre/
#mkdir build
mkdir install
cd build
cmake ..
make install
cd ..
cd ..










# 3rdparty
cd ..
cd ..



#compile
./src/catkin/bin/catkin_make_isolated

cat /home/abuild/rpmbuild/BUILD/cartographer_ros-1.0.0/devel_isolated/cartographer/share/cartographer/cartographer-config.cmake


#install
mkdir -p %{buildroot}/opt/ros/melodic/
cp -r devel_isolated/* %{buildroot}/opt/ros/melodic/

echo %{buildroot}


%files
#%defattr(-,root,root)
#/opt/ros/melodic/*
/opt/ros/melodic/*
#/usr/lib/share/catkin/cmake/*

%changelog
* Thu May 28 2020 openEuler Buildteam <buildteam@openeuler.org> - 19.4-1
- Package init

