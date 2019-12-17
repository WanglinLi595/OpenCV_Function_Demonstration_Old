#!/usr/bin/env python
# coding=utf-8
'''
@描述: 程序的主函数
@版本: V1_0_0
@作者: LiWanglin
@创建时间: 2019.12.12
@最后编辑人: LiWanglin
@最后编辑时间: 2019.12.15
'''
import sys
from PyQt5.QtWidgets import QApplication
from uicla.main_interface import MainInterface


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainInterface()      # 创建主界面类
    form.show()                 # 显示主界面
    sys.exit(app.exec_())
    