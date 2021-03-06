# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OpenCV_Function_Demonstration\src\uisrc\ui_main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainInterface(object):
    def setupUi(self, ui_main_interface):
        ui_main_interface.setObjectName("ui_main_interface")
        ui_main_interface.resize(824, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_main_interface.sizePolicy().hasHeightForWidth())
        ui_main_interface.setSizePolicy(sizePolicy)
        ui_main_interface.setIconSize(QtCore.QSize(40, 40))
        ui_main_interface.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(ui_main_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_image_info = QtWidgets.QLabel(self.centralwidget)
        self.lb_image_info.setText("")
        self.lb_image_info.setObjectName("lb_image_info")
        self.horizontalLayout.addWidget(self.lb_image_info)
        self.btn_roi_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_roi_ok.setObjectName("btn_roi_ok")
        self.horizontalLayout.addWidget(self.btn_roi_ok)
        self.vertical_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.vertical_layout)
        self.table_view = QtWidgets.QTableView(self.centralwidget)
        self.table_view.setObjectName("table_view")
        self.horizontalLayout_2.addWidget(self.table_view)
        self.tree_widget = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_widget.setObjectName("tree_widget")
        self.tree_widget.headerItem().setText(0, "1")
        self.horizontalLayout_2.addWidget(self.tree_widget)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        ui_main_interface.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui_main_interface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        ui_main_interface.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui_main_interface)
        self.statusbar.setObjectName("statusbar")
        ui_main_interface.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ui_main_interface)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        ui_main_interface.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.act_exit = QtWidgets.QAction(ui_main_interface)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/act_quit_triggered.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon)
        self.act_exit.setObjectName("act_exit")
        self.act_load_image = QtWidgets.QAction(ui_main_interface)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/act_load_img_triggered.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_load_image.setIcon(icon1)
        self.act_load_image.setObjectName("act_load_image")
        self.menuFile.addAction(self.act_load_image)
        self.menuFile.addAction(self.act_exit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.toolBar.addAction(self.act_load_image)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_exit)

        self.retranslateUi(ui_main_interface)
        QtCore.QMetaObject.connectSlotsByName(ui_main_interface)

    def retranslateUi(self, ui_main_interface):
        _translate = QtCore.QCoreApplication.translate
        ui_main_interface.setWindowTitle(_translate("ui_main_interface", "MainWindow"))
        self.btn_roi_ok.setText(_translate("ui_main_interface", "确定感兴趣区域"))
        self.menuFile.setTitle(_translate("ui_main_interface", "文件"))
        self.menuabout.setTitle(_translate("ui_main_interface", "关于"))
        self.toolBar.setWindowTitle(_translate("ui_main_interface", "toolBar"))
        self.act_exit.setText(_translate("ui_main_interface", "退出"))
        self.act_exit.setToolTip(_translate("ui_main_interface", "exit_soft"))
        self.act_load_image.setText(_translate("ui_main_interface", "载入图片"))
import icon.rec_rc
