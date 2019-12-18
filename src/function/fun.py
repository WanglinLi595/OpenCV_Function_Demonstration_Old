#!/usr/bin/env python
# coding=utf-8
'''
@描述: 程序中一些常用的功能
@版本: V1_0_0
@作者: LiWanglin
@创建时间: 2019.12.12
@最后编辑人: LiWanglin
@最后编辑时间: 2019.12.18
'''
import cv2

import numpy as np

from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QTreeWidgetItem, QGraphicsView, QLabel
from PyQt5.QtGui import QImage, QPixmap, QStandardItem, QPainter
from PyQt5.QtCore import QCoreApplication, QTranslator, pyqtSignal, QPoint, Qt

from enum import Enum


class ModifyQGraphicsView(QGraphicsView):
    """改进QGraphicsView类

    由于QGraphicsView类没有与mouseMoveEvent（）相关的信号，因而无法定义槽函数于此时间关联。为此，
    从QGraphicsView类集成定义一个类QGraphicsView类，实现鼠标移动事件函数mouseMoveEvent()的处理，
    并把事件转换为自定义信号，这样就可以在程序里面设计槽函数响应这些鼠标事件。

    @属性说明：
        mouse_move：定义一个鼠标移动信号

    @方法说明：
        mouseMoveEvent()：鼠标移动事件

    """
    mouse_move = pyqtSignal(QPoint)     # 定义一个鼠标移动信号
    mouse_clicked = pyqtSignal(QPoint)  # 定义一个鼠标点击信号

    def mouseMoveEvent(self, event): 
        '''鼠标移动事件

        鼠标移动事件

        @参数说明: 
            point：当前鼠标所在的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''  
        point=event.pos()          
        self.mouse_move.emit(point)    #发射信号
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        '''鼠标点击事件

        鼠标点击事件

        @参数说明: 
            point：当前鼠标所在的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''  
        if(event.button() == Qt.LeftButton):
            point = event.pos()
            self.mouse_clicked.emit(point)      #发射信号     
        super().mousePressEvent(event)


class TreeItemType(Enum):
    """节点类型枚举

    定义节点类型枚举，为了便于后面的目录树的修改

    @属性说明：
        top_item: 顶层节点
        group_item: 组节点
        function_item：函数节点

    @方法说明：
        无
    """
    top_item = 1001             # 顶层节点
    group_item = 1002           # 组节点
    function_item = 1003        # 函数节点


def dispaly_image_in_graphics_view(dispaly_image, graphics_view, image_w=None, 
                    image_h=None, dispaly_image_shape=None):
    '''在QGraphicsView显示一张图片

    在QGraphicsView显示一张图片

    @参数说明: 
        dispaly_image：要显示的图片
        graphics_view：显示图片QGraphicsView控件
        image_w：图片的宽
        image_h：图片的长
        dispaly_image_shape：图片的维度

    @返回值: 
        无

    @注意: 
        无
    '''
    # 判断是否输入图片的长和宽，如果没有，获取图片的长和宽
    if(image_h == None or image_w == None):       
        image_h, image_w = dispaly_image.shape[:2]

    # 判断是否输入图片的维度，如果没有，获取图片的维度
    if(dispaly_image_shape == None):       
        dispaly_image_shape= len(dispaly_image.shape)

    # 根据图片的维度，进行不同的处理
    if(dispaly_image_shape == 2):
        # 如果是二维灰度图片，读取方式为QImage.Format_Grayscale8
        temp_q_image = QImage(dispaly_image, image_h ,image_w, QImage.Format_Grayscale8)
    elif(dispaly_image_shape == 3):
         # 由于QImage读取方式为RGB，但opencv读取图片形式为BGR，所以要进行色彩转换
        temp_q_image = cv2.cvtColor(dispaly_image, cv2.COLOR_BGR2RGB)

        # 如果是三维灰度图片，读取方式为QImage.Format_RGB888
        temp_q_image = QImage(temp_q_image, image_h, image_w, QImage.Format_RGB888)
    
    temp_q_image_pix = QPixmap.fromImage(temp_q_image)               # 将给定图像转换为像素映射

    # 在graphics_view中显示图片
    temp_item = QGraphicsPixmapItem(temp_q_image_pix)
    temp_q_sece = QGraphicsScene()
    temp_q_sece.addItem(temp_item)  
    graphics_view.setScene(temp_q_sece)
    temp_q_sece.clearSelection()

    return temp_q_sece, temp_item


def add_tree_item(item_parent, tree_value, tree_class_text, tree_text, tree_col_num=0, tree_top=False):
    '''在目录树上添加节点

    在目录树上添加节点

    @参数说明: 
        item_parent：此节点的父节点
        tree_value：节点相对应的值
        tree_class_text：
        tree_text：设置节点文字
        tree_col_num=0：节点的行号
        tree_top：是否为首节点

    @返回值: 
        tree_item：返回此节点

    @注意: 
        无
    '''
    tree_item = QTreeWidgetItem(tree_value)     # 创建QTreeWidgetItem类
    text = QCoreApplication.translate(tree_class_text, tree_text)
    tree_item.setText(tree_col_num, text)        # 设置节点文字
    # 首节点判定
    if(tree_top==False):
        item_parent.addChild(tree_item)
    else:
        item_parent.addTopLevelItem(tree_item)
    return tree_item

def add_data_to_table_view(table_model, table_data, table_col, table_row):
    '''"在TableView添加数据

    在TableView添加数据

    @参数说明: 
        table_model：QStandardItemModel对象
        table_data；要添加的数据
        table_col：添加的行数
        table_row：添加列数

    @返回值:
        无

    @注意:
        无
    '''
    for i in range(table_col):
        for j in range(table_row): 
            temp_date = QStandardItem(str(table_data[i, j]))
            # 设置单元格居中
            temp_date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table_model.setItem(i, j, temp_date)    # 在单元格中添加数据

def draw_background_image(widget, background_image):
    '''绘制窗体的背景图片

    绘制窗体的背景图片

    @参数说明: 
        widget：要绘制的窗体
        background_image：要绘制的背景图片

    @返回值: 
        无

    @注意: 
        无
    '''
    painter = QPainter(widget)                 
    background_image = QPixmap(background_image)
    # 绘制背景图片
    painter.drawPixmap(0, 0, widget.width(), widget.height(), background_image)

def init_status_bar(statusbar, class_name="", text_left="", text_right=""):
    '''在状态栏添加标签

    在状态栏添加标签

    @参数说明: 
        statusbar：状态栏
        class_name：类名
        text_left：左状态栏标签文本
        text_right：右状态栏标签文本

    @返回值: 
        status_label_left：左状态栏标签
        status_label_left：右状态栏标签

    @注意: 
        无
    '''
    # 状态信息栏初始化
    # 状态信息栏初的左边显示
    status_label_left = QLabel()
    status_label_left.setMinimumSize(150, 20)         # 设置__status_label_left的最小尺寸
    statusbar.addWidget(status_label_left)
    text = QCoreApplication.translate(class_name, text_left)  # 设置__status_label_left的初始显示内容
    status_label_left.setText(text)

     # 状态信息栏初的右边显示
    status_label_right = QLabel()
    status_label_right.setMinimumSize(150, 20)
    statusbar.addPermanentWidget(status_label_right)
    text = QCoreApplication.translate(class_name, text_right)
    status_label_right.setText(text)

    return status_label_left, status_label_right

def select_irregular_roi(image, range_point):
    '''选取不规则的感兴趣区域

    选取不规则的感兴趣区域

    @参数说明: 


    @返回值: 


    @注意: 
        无
    '''
    # 将传进来的range_point修改为适应cv2.fillPoly参数pts的格式
    range_point_num = len(range_point)
    range_roi = np.empty([range_point_num, 2], dtype=np.int32)
    for i in  range(range_point_num):
        range_roi[i] = np.asarray(range_point[i])
         
    # 获取图像的长和宽
    image_h, image_w = image.shape[:2]

    mask = np.zeros((image_h, image_w), dtype=np.uint8)     # 生成掩膜版
    cv2.fillPoly(mask, [range_roi], (255), 8, 0)            # 确定掩膜版区域
    result = cv2.bitwise_and(image, image, mask=mask)       # 生成ROI图像
    
    return result   # 返回结果