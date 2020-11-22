# cartographer_ros

#### Description
Cartographer is a system that provides real-time simultaneous localization and mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations.

![输入图片说明](https://images.gitee.com/uploads/images/2020/1115/102934_7759d85d_1226697.png "屏幕截图_600.png")

video demo run in openeuler see: https://www.bilibili.com/video/BV1Rf4y1B73u

#### Software Architecture
Software architecture description

Cartographer can be seen as two separate, but related subsystems. The first one is local SLAM (sometimes also called frontend or local trajectory builder). Its job is to build a succession of submaps. Each submap is meant to be locally consistent but we accept that local SLAM drifts over time

W. Hess, D. Kohler, H. Rapp, and D. Andor, Real-Time Loop Closure in 2D LIDAR SLAM, in Robotics and Automation (ICRA), 2016 IEEE International Conference on. IEEE, 2016. pp. 1271–1278.

#### Installation

1. Dowload RPM

wget http://121.36.3.168:82/home:/davidhan:/branches:/openEuler:/Mainline/standard_aarch64/aarch64/cartographer_ros-1.0.0-0.oe1.aarch64.rpm 

2. Install RPM

sudo  rpm -ivh cartographer_ros-1.0.0-0.oe1.aarch64.rpm 

#### Instructions

Exit the cartographer_ros file under the /opt/ros/melodic/devel_isolated/ directory , Prove that the software installation is successful

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
