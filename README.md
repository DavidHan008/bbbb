# cartographer_ros

#### 介绍
cartographer是一个可跨多个平台和传感器配置在2D和3D中提供实时同时定位和地图绘制（SLAM）。该项目提供了ROS集成
![输入图片说明](https://images.gitee.com/uploads/images/2020/1115/103111_d513f3f4_1226697.png "屏幕截图_600.png")

在opeuler上运行cartographer的demo参见:https://www.bilibili.com/video/BV1Rf4y1B73u

#### 软件架构
软件架构说明

cartographer可以看作是两个独立但相关的子系统。第一个是本地SLAM（有时也称为前端或本地轨迹构建器）。它的工作是建立一系列子图。每个子图都应该在本地保持一致，避免local SLAM随时间漂移

参考论文:
W. Hess, D. Kohler, H. Rapp, and D. Andor, Real-Time Loop Closure in 2D LIDAR SLAM, in Robotics and Automation (ICRA), 2016 IEEE International Conference on. IEEE, 2016. pp. 1271–1278.

#### 安装教程

1. 下载rpm包

wget http://121.36.3.168:82/home:/davidhan:/branches:/openEuler:/Mainline/standard_aarch64/aarch64/cartographer_ros-1.0.0-0.oe1.aarch64.rpm

2. 安装rpm包

sudo rpm -ivh cartographer_ros-1.0.0-0.oe1.aarch64.rpm

#### 使用说明

安装完成以后，在/opt/ros/melodic/devel_isolated/目录下有cartographer_ros/文件夹证明安装成功

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
