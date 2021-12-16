import sys
from PyQt5.QtWidgets import QApplication, QWidget
from designer import Ui_Form

from PyQt5.QtWidgets import *


class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)                                          # 1
        # self.text_edit.textChanged.connect(self.show_text_func)     # 2

        self.openFileBtn.clicked.connect(self.brownFile)
        self.anaysisFileBtn.clicked.connect(self.anaysisFileBtn_fuc)
        #
        self.text_browser.clicked.connect(self.detail_by_index_fuc)


    def brownFile(self):
        openfile_name = QFileDialog.getExistingDirectory(self,"选取文件夹","./")

        # 查找cil文件
        text_context = ""
        root_path = openfile_name
        text_context += "<b>{}</b> <br/>".format(root_path)

        cil_list = self.find_cil_file(root_path)
        if not cil_list:
            window = QWidget()
            window.resize(300, 200)
            window.move(300, 300)
            QMessageBox.critical(window,  # 父窗口QWidget
                                 '错误',  # 窗口标题
                                 "这是一个错误弹窗",  # 窗口提示信息
                                 QMessageBox.Cancel | QMessageBox.Close,
                                 # 窗口内添加按钮-QMessageBox.StandardButton，可重复添加使用 | 隔开；如果不写，会有个默认的QMessageBox.StandardButton
                                 QMessageBox.Cancel,  # 设置默认按钮（前提是已经设置有的按钮，若是没有设置，则无效）
                                 )
        else:
            for i in cil_list:
                text_context += "&nbsp;"*5 + i + "<br/>"
            self.text_edit.setText(text_context)

    def anaysisFileBtn_fuc(self):
        self.text_browser.clearMask()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']  # 添加的数组数据
        self.slm.setStringList(self.qList)
         # 将数据设置到model

    def detail_by_index_fuc(self, index):
        print(index.row())
        self.show_info.setText(self.qList[index.row()])





    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())

    def find_cil_file(self, source_f):
        # return []
        return ["008/008.cil", '009/009.ci1']



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())