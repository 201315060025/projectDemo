# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.qList = []

        Form.setObjectName("Form")
        Form.resize(1146, 340)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")



        self.edit_label = QtWidgets.QLabel(Form)
        self.edit_label.setObjectName("edit_label")
        self.gridLayout.addWidget(self.edit_label, 0, 0, 1, 1)


        self.browser_label = QtWidgets.QLabel(Form)
        self.browser_label.setObjectName("browser_label")
        self.gridLayout.addWidget(self.browser_label, 0, 1, 1, 1)

        self.path_target_label = QtWidgets.QLabel(Form)
        self.path_target_label.setObjectName("path_edit_label")
        self.gridLayout.addWidget(self.path_target_label, 1, 1, 1, 1)

        self.text_edit = QtWidgets.QTextEdit(Form)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 2, 0, 1, 1)

        #
        # self.text_browser = QtWidgets.QTextBrowser(Form)
        # self.text_browser.setObjectName("text_browser")
        # self.gridLayout.addWidget(self.text_browser, 1, 1, 1, 1)

        self.slm = QtCore.QStringListModel()


        self.text_browser = QtWidgets.QListView(Form)
        self.text_browser.setObjectName("text_browser")
        self.slm.setStringList(self.qList)
        self.text_browser.setModel(self.slm)

        self.gridLayout.addWidget(self.text_browser, 2, 1, 1, 1)

        # 文件浏览
        self.openFileBtn = QtWidgets.QPushButton(Form)
        self.openFileBtn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.openFileBtn.setObjectName("openFileBtn")
        self.openFileBtn.setText("浏览文件")
        self.gridLayout.addWidget(self.openFileBtn, 3, 0, 1, 1)

        # 解析文件
        self.anaysisFileBtn = QtWidgets.QPushButton(Form)
        self.anaysisFileBtn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.anaysisFileBtn.setObjectName("anaysisFileBtn")
        self.anaysisFileBtn.setText("开始解析")
        self.gridLayout.addWidget(self.anaysisFileBtn, 3, 1, 1, 1)

        #
        # self.checkPoint_label = QtWidgets.QLabel(Form)
        # self.checkPoint_label.setObjectName("checkPoint_label")
        # self.gridLayout.addWidget(self.checkPoint_label, 4, 0, 1, 1)


        # <editor des=" 断电初始化配置">
        self.checkPoint_init_config_label = QtWidgets.QLabel(Form)
        self.checkPoint_init_config_label.setLineWidth(20)
        self.checkPoint_init_config_label.setObjectName("checkPoint_init_config_label")
        self.gridLayout.addWidget(self.checkPoint_init_config_label, 5, 0, 1, 1)

        self.checkPoint_combox_start = QtWidgets.QComboBox(Form)
        self.checkPoint_combox_start.move(100, 20)
        self.checkPoint_combox_start.addItem('C')
        self.checkPoint_combox_start.addItem('C++')
        self.gridLayout.addWidget(self.checkPoint_combox_start, 6, 0, 1, 1)

        self.checkPoint_combox_end = QtWidgets.QComboBox(Form)
        self.checkPoint_combox_end.move(100, 20)
        self.checkPoint_combox_end.addItem('C')
        self.checkPoint_combox_end.addItem('C++')
        self.gridLayout.addWidget(self.checkPoint_combox_end, 6, 1, 1, 1)

        #</editor>

        # <editor des=" 断电运行配置">
        self.checkPoint_init_config_label2 = QtWidgets.QLabel(Form)
        self.checkPoint_init_config_label2.setLineWidth(20)
        self.checkPoint_init_config_label2.setObjectName("checkPoint_init_config_label2")
        self.gridLayout.addWidget(self.checkPoint_init_config_label2, 7, 0, 1, 1)

        self.checkPoint_combox_start2 = QtWidgets.QComboBox(Form)
        self.checkPoint_combox_start2.move(100, 20)
        self.checkPoint_combox_start2.addItem('C')
        self.checkPoint_combox_start2.addItem('C++')
        self.gridLayout.addWidget(self.checkPoint_combox_start2, 8, 0, 1, 1)

        self.checkPoint_combox_end2 = QtWidgets.QComboBox(Form)
        self.checkPoint_combox_end2.move(100, 20)
        self.checkPoint_combox_end2.addItem('C')
        self.checkPoint_combox_end2.addItem('C++')
        self.gridLayout.addWidget(self.checkPoint_combox_end2, 8, 1, 1, 1)
        # <editor>

        # doicker 配置信息
        self.docker_config_info = QtWidgets.QLabel(Form)
        self.docker_config_info.setLineWidth(20)
        self.docker_config_info.setObjectName("docker_config_info")
        self.gridLayout.addWidget(self.docker_config_info, 9, 0, 1, 1)

        self.docker_config_ip_info = QtWidgets.QLineEdit(Form)
        # self.docker_config_ip_info.setLineWidth(20)
        self.docker_config_ip_info.setObjectName("docker_config_ip_info")
        self.gridLayout.addWidget(self.docker_config_ip_info, 10, 0, 1, 1)

        self.docker_config_port1_info = QtWidgets.QLineEdit(Form)
        # self.docker_config_port1_info.setLineWidth(20)
        self.docker_config_port1_info.setObjectName("docker_config_port1_info")
        self.gridLayout.addWidget(self.docker_config_port1_info, 11, 0, 1, 1)

        self.docker_config_port2_info = QtWidgets.QLineEdit(Form)
        # self.docker_config_port1_info.setLineWidth(20)
        self.docker_config_port2_info.setObjectName("docker_config_port2_info")
        self.gridLayout.addWidget(self.docker_config_port2_info, 12, 0, 1, 1)

        self.docker_excute_btn = QtWidgets.QPushButton(Form)
        self.docker_excute_btn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.docker_excute_btn.setObjectName("docker_excute_btn")
        self.docker_excute_btn.setText("开始执行")
        self.docker_excute_btn.setFixedHeight(100)
        self.gridLayout.addWidget(self.docker_excute_btn, 10, 1, 3, 1)

        # 展示信息
        self.show_info_title = QtWidgets.QLabel(Form)
        self.show_info_title.setObjectName("showInfo")
        self.gridLayout.addWidget(self.show_info_title, 13, 0, 1, 2)


        # 展示信息
        self.show_info = QtWidgets.QTextBrowser(Form)
        self.show_info.setObjectName("showInfo")
        self.gridLayout.addWidget(self.show_info, 14, 0, 1, 2)








        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "指令解析工具"))
        self.edit_label.setText(_translate("Form", "源文件信息"))
        self.browser_label.setText(_translate("Form", "解析后信息"))
        # self.checkPoint_label.setText(_translate("Form", "断点启动文件"))
        self.checkPoint_init_config_label.setText(_translate("Form", "断点启动配置"))
        self.checkPoint_init_config_label2.setText(_translate("Form", "断点启动配置2"))
        self.show_info_title.setText(_translate("Form", "执行日志输出"))
        self.docker_config_info.setText(_translate("Form", "docker 配置信息"))
        self.path_target_label.setText(_translate("Form", "  path:"))