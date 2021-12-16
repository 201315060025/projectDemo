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
        Form.resize(746, 340)
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



        # 展示信息
        self.show_info = QtWidgets.QTextBrowser(Form)
        self.show_info.setObjectName("showInfo")
        self.gridLayout.addWidget(self.show_info, 3, 0, 1, 2)

        # 文件浏览
        self.openFileBtn = QtWidgets.QPushButton(Form)
        self.openFileBtn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.openFileBtn.setObjectName("openFileBtn")
        self.openFileBtn.setText("浏览文件")
        self.gridLayout.addWidget(self.openFileBtn, 4, 0, 1, 1)

        # 解析文件
        self.anaysisFileBtn = QtWidgets.QPushButton(Form)
        self.anaysisFileBtn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.anaysisFileBtn.setObjectName("anaysisFileBtn")
        self.anaysisFileBtn.setText("开始解析")
        self.gridLayout.addWidget(self.anaysisFileBtn, 4, 1, 1, 1)





        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "指令解析工具"))
        self.edit_label.setText(_translate("Form", "源文件信息"))
        self.browser_label.setText(_translate("Form", "解析后信息"))
        self.path_target_label.setText(_translate("Form", "  path:"))