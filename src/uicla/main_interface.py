#!/usr/bin/env python
# coding=utf-8
'''
@描述: UI主界面功能实现
@版本: V1_0_0
@作者: LiWanglin
@创建时间: 2019.12.12
@最后编辑人: LiWanglin
@最后编辑时间: 2019.12.15
'''

import cv2

import numpy as np

from uisrc.ui_main_interface import UiMainInterface

from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QGraphicsPixmapItem, 
                            QTreeWidgetItem, QAbstractItemView, QHeaderView)
from PyQt5.QtCore import (QCoreApplication, QTranslator, pyqtSlot, QItemSelectionModel, Qt, pyqtSignal,
                            QPoint, QEvent)
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem

from enum import Enum

import threading

from function import fun


class MainInterface(QMainWindow):
    """

    @属性说明：
        __file_name_dir：用来保存图片文件的绝对路径
        __preprocessing_image：用来保存通过cv2读取图片的数据
        __preprocessing_image_h：用来保存预处理图片的长
        __preprocessing_image_w：用来保存预处理图片的宽
        __preprocessing_image_shape：用来保存预处理图片的维度
        class_name：用来保存类名

    @方法说明：
        __init_tree_widget()：初始化目录树
        paintEvent(): 绘制背景图
        on_act_load_image_triggered()：载入图片
    """
    _translate = QCoreApplication.translate   # 类属性，起代替作用

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainInterface()
        self.ui.setupUi(self)

        self.__file_name_dir = ""               # 用来保存图片文件的绝对路径
        self.__preprocessing_image = ""         # 用来保存通过cv2读取图片的数据
        self.__preprocessing_image_h = 0        # 用来保存预处理图片的长
        self.__preprocessing_image_w = 0        # 用来保存预处理图片的宽
        self.__preprocessing_image_shape = []   # 用来保存预处理图片的维度
        self.class_name = "MainInterface"       # 用来保存类名
        self.__image_roi = []                   # 用来保存杆兴趣区域
        self.graphcis_view = fun.ModifyQGraphicsView(self)  # 创建graphcis_view，用来显示图片
 
        self.ui.vertical_layout.addWidget(self.graphcis_view)        # 对graphcis_view进行布局

        # 设置主界面标题
        text = self._translate(self.class_name, "OpenCV函数演示")
        self.setWindowTitle(text)

        self.showMaximized()                   # 设置窗口初始显示为全屏显示

        text1 = "暂无处理图片，请添加处理图片"
        text2 = "暂无处理结果" 
        # 初始化状态栏
        self.status_label_left, status_label_right = fun.init_status_bar(self.ui.statusbar, 
                                self.class_name, text1, text2)
        
        self.ui.act_exit.triggered.connect(self.close)       # 绑定退出按钮与关闭窗口函数

        self.__init_tree_widget()                # 初始化目录树

    
    def __init_tree_widget(self):
        """初始化目录树

        初始化目录树，在目录树上添加节点

        @参数说明：
            无
        
        @返回值：
            无

        @注意：
            无
        """
        self.ui.tree_widget.clear()             # 初始化目录树

        text = self._translate("MainInterface", "函数")
        self.ui.tree_widget.setHeaderLabel(text)          # 设置目录树头标签

        text = "OpenCV函数"
        # 添加顶层节点
        self.tree_top_item = fun.add_tree_item(self.ui.tree_widget, fun.TreeItemType.top_item.value, 
                        self.class_name, text, tree_top=True)
        text = "OpenCV入门函数"
        # 添加组节点
        self.tree_group_item = fun.add_tree_item(self.tree_top_item, fun.TreeItemType.group_item.value, 
                        self.class_name, text)
        # 添加函数节点
        text = "cv.imread()"
        self.tree_fun_item = fun.add_tree_item(self.tree_group_item, fun.TreeItemType.function_item.value, 
                        self.class_name, text)

    def paintEvent(self, event):
        '''绘制背景图

        Qt默认事件，绘制背景图

        @参数说明: 
            event：事件

        @返回值: 
            无

        @注意: 
            无
        '''
        fun.draw_background_image(self, "background_image/background_2.jpg")
        # TODO:应添加到fun.draw_background_image()函数里面
        super().paintEvent(event)        # 执行父辈的paintEvent()函数，以便父辈执行内建的一些操作 

    @pyqtSlot()
    def on_act_load_image_triggered(self):
        '''载入图片

        载入一张要处理的图片。将其显示在graphics_view，将其数据显示在table_view

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        text = self._translate(self.class_name, "正在进行图片加载，请稍等")
        self.status_label_left.setText(text)

        text1 = self._translate("MainInterface", "载入图片")
        text2 = self._translate("MainInterface", "图片文件(*.bmp *.jpg *.png)")
        # 获取文件的绝对路径
        self.__file_name_dir = QFileDialog.getOpenFileName(self, text1, ".", text2)[0]

        if(self.__file_name_dir == ""):   # 未读取图片路径提示
            text1 = self._translate("MainInterface", "错误提示")
            text2 = self._translate("MainInterface", "未获得图片路径")
            QMessageBox.critical(self, text1, text2)
            return None

        # 使用cv2读取图片
        self.__preprocessing_image = cv2.imread(self.__file_name_dir, cv2.IMREAD_UNCHANGED)

        # 获取图片信息
        # 获取预处理图片的维度
        print(self.__preprocessing_image.shape)
        self.__preprocessing_image_shape = len(self.__preprocessing_image.shape)
        # 获取图片的长和宽
        self.__preprocessing_image_h, self.__preprocessing_image_w = self.__preprocessing_image.shape[:2]
        
        # 设置tab_view的行数列数
        self.item_model = QStandardItemModel(self.__preprocessing_image_h, self.__preprocessing_image_w, self)
        self.select_model = QItemSelectionModel(self.item_model)
        self.ui.table_view.setModel(self.item_model)             #数据模型
        self.ui.table_view.setSelectionModel(self.select_model)  # 选择模型
        one_more = QAbstractItemView.ExtendedSelection      # 选择模式
        self.ui.table_view.setSelectionMode(one_more)       # 可多选
        item_or_row = QAbstractItemView.SelectItems         # 项选则模式
        self.ui.table_view.setSelectionBehavior(item_or_row)    # 单元格选择
        self.ui.table_view.setAlternatingRowColors(True)        # 设置交替行颜色
        # 根据数据调节单元格大小
        self.ui.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # TODO:使用多线程同时绘图和显示图片数据， 暂时有问题 
        # th_1 = threading.Thread(target=fun.add_data_to_table_view, args=(self.item_model, self.__preprocessing_image, 
        #                                     self.__preprocessing_image_h, self.__preprocessing_image_w))
        # th_2 = threading.Thread(target=fun.dispaly_image_in_graphics_view, args=(self.__preprocessing_image, self.graphcis_view))
        
        # # 开始执行多线程任务
        # th_1.start()
        # th_2.start()

        # 在TableVIew中添加数据
        fun.add_data_to_table_view(self.item_model, self.__preprocessing_image, 
                                          self.__preprocessing_image_h, self.__preprocessing_image_w)

        # 在GraphicsView绘制图像
        self.scen, self.gr_temp_item = fun.dispaly_image_in_graphics_view(self.__preprocessing_image, self.graphcis_view)
        self.graphcis_view.mouse_move.connect(self.slot_mouse_move)   #鼠标移动
        self.graphcis_view.mouse_clicked.connect(self.slot_mouse_clicked)
        # 要想实现mouseMoveEvent，则需要先设置setMouseTrack(true)，直接得到监听事件。
        # 若是setMouseTrack(false),只有鼠标按下才会有mouseMove监听事件响应。
        self.graphcis_view.setMouseTracking(True)       

        text = self._translate(self.class_name, "图片加载成功")
        self.status_label_left.setText(text) 

    def slot_mouse_move(self, point):
        '''获取图片坐标点

        当鼠标移动到图片上时，能过显示图片当前的坐标点，并且显示相对应的像素点

        @参数说明: 
            point：当前鼠标的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''
        point = self.graphcis_view.mapToScene(point)          # 将视图中的一个坐标变换为场景的坐标
        point = self.gr_temp_item.mapFromScene(point)          # 将场景中的一个点映射本图形项的坐标系
        
        # 判断是否在显示图片区域内，如果在，显示相对应的坐标和像素点
        if(point.x() < self.__preprocessing_image_w and point.y() < self.__preprocessing_image_h 
            and point.x() >= 0 and point.y() >= 0):         
            pix = str(self.__preprocessing_image[int(point.x()), int(point.y())])       # 获取像素点
            text = self._translate(self.class_name, "坐标：")
            # ui.lb_image_info显示图片的坐标点和像素值
            self.ui.lb_image_info.setText(text + "(%d, %d)" % (point.x(), point.y()) + "  " + pix)
        else:
            self.ui.lb_image_info.setText("")           # 鼠标不在图片里面时，ui.lb_image_info.什么都不显示

    def slot_mouse_clicked(self, point):
        '''显示鼠标点击时确定的ROI

        显示鼠标点击时确定的ROI

        @参数说明: 
            point：当前鼠标的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''
        point = self.graphcis_view.mapToScene(point)          # 将视图中的一个坐标变换为场景的坐标
        point = self.gr_temp_item.mapFromScene(point)          # 将场景中的一个点映射本图形项的坐标系

        temp_point = [int(point.x()), int(point.y())]          # 将传进来的point转化为列表形式

        self.__image_roi.append(temp_point)         # 将传进来的点，添加到 __image_roi里面  
        # TODO:显示点击的点
        if(len(self.__image_roi) > 1):              # 将点连成线,显示选取范围
            result = cv2.line(self.__preprocessing_image, tuple(self.__image_roi[-1]), 
                        tuple(self.__image_roi[-2]), (255, 255, 255), 2)
            fun.dispaly_image_in_graphics_view(result, self.graphcis_view)

    @pyqtSlot()
    def on_btn_roi_ok_clicked(self):
        '''确定ROI

        确定ROI

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        if(len(self.__image_roi) > 2):                  # 要大于两个点才会有确定ROI区域
            # 确定感兴趣区域
            result = fun.select_irregular_roi(self.__preprocessing_image, self.__image_roi)
            # 在self.graphcis_view重新绘图
            fun.dispaly_image_in_graphics_view(result, self.graphcis_view)
            # 跟新item_model显示数据
            fun.add_data_to_table_view(self.item_model, result, self.__preprocessing_image_h, self.__preprocessing_image_w)
            self.__image_roi = []
        else: 
            return
