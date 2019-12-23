![](https://img.shields.io/badge/version-v1.0-orange)
![](https://img.shields.io/badge/author-LWL-brightgreen)
[![](https://img.shields.io/badge/license-MIT-green)](https://github.com/WanglinLi595/OpenCV_Function_Demonstration/blob/master/LICENSE)

# OpenCV函数演示
## 项目简介：
此项目是为了清晰的演示OpenCV图像处理的过程。通过一个个的OpenCV函数演示，让人清楚的明白OpenCV函数的使用。另外在观察图片时，不仅能看到图片的本身，更能看到图片所对应的数据，更加直白反应图像处理的结果。

## 项目特点
- 以OpenCV为主要研究对象
- 使用PyQt5，清楚显示出图像处理时，其内部数据的变化

## 项目安装及使用指南
- 如果使用Anaconda作为Python开发环境，则只需安装PyQt5和python-opencv即可
- 如果只使用pip作为安装环境，在项目的根目录下打开终端，使用：pip install -r requirements.txt 安装依赖包  
  
    使用指南请查看docs目录下的文件.
  
## 项目目录结构
```
dist/       编译出来的发布版
src/        源码文件
    background_image/    项目程序中要用到的背景图片
    function/            项目程序中要使用到的函数
    icon/                项目程序中要用到的图标和图标资源文件 
    test_image/          项目程序中要用到的测试文件
    uicla/               保存由Qt Designer生成的ui文件以及ui文件经过pyuic编译的py文件
    uisrc/               保存创建具体UI界面的类
    main.py              项目程序中的主函数
docs/       文档
.gitignore：告诉git不要上传到 GitHub上的文件
LICENSE：授权协议 
README.md 自述文件，整个项目的简介、使用方法等
requirements.txt：记录项目所有的依赖包及其版本号
```
## 版本说明
- 目前版本：V1_0_0
- 主要任务：  
    完成整个程序的框架
- 版本历史更改说明：
```  
    暂无
```

## 其他说明
### 依赖包版本说明
本项目程序中，所用到的python版本为：3.6，所用的python-opencv版本为：4.1.2。  
其余具体的依赖包以及其版本号详情，请查看requirements.txt文件。

### 作者
黎旺林  联系邮箱：<1156494696@qq.com>

### 许可证
本开源项目使用MIT许可证，具体说明请查看LICENSE文件。