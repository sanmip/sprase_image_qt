import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from mainwindow import Ui_MainWindow
import checksparse
import os
import datetime
import shutil
import operator


class UiMain(QMainWindow):
    ui = Ui_MainWindow()  # type: Ui_MainWindow
    ap_dir = ""
    out_dir = ""
    xml_file = ""

    def __init__(self):
        super().__init__()
        self.ui.setupUi(self)
        self.ui.choose_ap.clicked.connect(self.choose_ap_func)
        self.ui.choose_out.clicked.connect(self.choose_out_func)
        self.ui.choose_xml.clicked.connect(self.choose_xml_func)
        self.ui.clear_log.clicked.connect(self.clean_log_func)
        self.ui.parse_image.clicked.connect(self.parse_image_func)



    def choose_ap_func(self):
        self.ap_dir =QFileDialog.getExistingDirectory(self, "选取AP目录",  "./")
        self.ui.show_ap.setText(self.ap_dir)
        self.show_log("选择AP地址为"+self.ap_dir)

    def choose_out_func(self):
        self.out_dir = QFileDialog.getExistingDirectory(self, "选取OUT目录", "./")
        self.ui.show_out.setText(self.out_dir)
        self.show_log("选择OUT地址为" + self.out_dir)

    def choose_xml_func(self):
        self.xml_file,ok = QFileDialog.getOpenFileName(self, "选取xml文件", "./" , "XML file (*.xml);;All Files (*)")
        self.ui.show_xml.setText(self.xml_file)
        self.show_log("选择XML文件为"+ self.xml_file)

    def show_log(self,log):
        self.ui.log_Browser.append(log)

    def clean_log_func(self):
        self.ui.log_Browser.setText("")


    def check_before_parse(self):
        if not os.path.exists(self.ap_dir):
            self.show_log("AP目录不存在")
            return False
        if os.path.exists(self.out_dir):
            self.show_log("OUT目录已存在,删除其中内容")
            shutil.rmtree(self.out_dir)
            os.mkdir(self.out_dir)
        else:
            os.mkdir(self.out_dir)

        return True

    def parse_image_func(self):

        self.ui.parse_image.isDown()
        self.ui.parse_image.isChecked()

        if not self.check_before_parse():
            self.ui.parse_image.isEnabled()
            return


        logtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.show_log("保存log到:" + logtime + ".txt")

        log_file = open(logtime +".txt", 'w')
        old_stdout = sys.stdout
        sys.stdout = log_file
        checksparse.main(self.xml_file,self.ap_dir,self.out_dir+"/rawprogram_unsparse.xml",self.out_dir)
        sys.stdout = old_stdout
        log_file.close()

        for line in open(logtime+ ".txt" ,"r"):
            self.show_log(line)

        for i in os.listdir(self.ap_dir):
            if not operator.eq('system.img',i):
                print(self.ap_dir+'/'+i)
                shutil.copy(self.ap_dir+'/'+i,self.out_dir)


        self.ui.parse_image.isEnabled()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = UiMain()
    main_ui.show()
    sys.exit(app.exec_())
