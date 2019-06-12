from PyQt5.QtCore import pyqtSlot, QIODevice, QByteArray 
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

import pychrome
from bs4 import BeautifulSoup
import requests

import docx
import signal

from Ui_FormMonitor import Ui_Form 
from change_paragraph import Word 
from PyQt5.QtCore import QTimer

class Window(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.switch=0
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.set_origin_pic) 
        self.timer.start(100)    

	# create a browser instance
        self.browser = pychrome.Browser(url="http://127.0.0.1:9222")
	# create a tab'
        self.tab = self.browser.new_tab()
	# start the tab 
        self.tab.start()
        # call method
        self.tab.Network.enable()

        self.browser = QWebEngineView()
        url = 'https://www.baidu.com'
        self.browser.load(QUrl(url))
        
        self.gridLayout_5.addWidget(self.browser)

        self.pushButton.clicked.connect(self.get_equipment)
        self.pushButton_2.clicked.connect(self.search)

    def call_web(self,equipment):

        # call method with timeout
        self.tab.call_method('Page.navigate',url="http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr="+equipment, _timeout=2)
	# wait for loading
        self.tab.wait(1)

        html = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

        soup = BeautifulSoup(((html['result'])['value']),"html.parser")

        #print(soup)
        print(soup.select("#ProductLineDesc"))
        print(type((soup.select("#ProductLineDesc"))[0]['value']))
        print(soup.title)	
        self.textBrowser_Product_Line.setText((soup.select("#ProductLineDesc"))[0]['value'])

        doc = docx.Document('Field Problem Feedback-Template.docx')

        data="Product line ："

        word_Product_Line=Word
        doc.paragraphs[1]=word_Product_Line.input_data(doc.paragraphs[1],data,(soup.select("#ProductLineDesc"))[0]['value'])
        
        doc.save('Feedback.docx')

        # stop the tab (stop handle events and stop recv message from chrome)

    def get_equipment(self):
        equipment = self.textEdit.toPlainText()
        print(equipment)
        self.call_web(equipment)
          
    def set_origin_pic(self):
        pic=QtGui.QPixmap(":/qrc/china.PNG")
        pic=pic.scaled(QSize(800,450),Qt.KeepAspectRatio)
        self.label.setPixmap(pic)      
        self.timer.stop()  

    def search(self):

        if self.switch==0 :
            pic1=QtGui.QPixmap(":/qrc/shanghai.PNG")
            pic1=pic1.scaled(QSize(800,450),Qt.KeepAspectRatio)
            self.label.setPixmap(pic1)
            self.switch=1
        elif self.switch==1 :
            pic1=QtGui.QPixmap(":/qrc/detail.PNG")
            pic1=pic1.scaled(QSize(800,450),Qt.KeepAspectRatio);
            self.label.setPixmap(pic1)
            self.switch=2
        elif self.switch==2 :
            pic1=QtGui.QPixmap(":/qrc/china.PNG")
            pic1=pic1.scaled(QSize(800,450),Qt.KeepAspectRatio)
            self.label.setPixmap(pic1)
            self.switch=0 
   


def signal_handler(signal,frame):
    print('You pressed Ctrl+C!')
#    tab.stop()
    sys.exit(0)


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = Window()
    w.setFixedSize(850,600)
    signal.signal(signal.SIGINT,signal_handler)
    w.show()
    sys.exit(app.exec_())















