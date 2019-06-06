from PyQt5.QtCore import pyqtSlot, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QWidget, QMessageBox

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

        #self.timer = QTimer(self) 
        #self.timer.timeout.connect(self.call_web) 
        # self.timer.start(10000)    

	# create a browser instance
        self.browser = pychrome.Browser(url="http://127.0.0.1:9222")
	# create a tab'
        self.tab = self.browser.new_tab()
	# start the tab 
        self.tab.start()
        # call method
        self.tab.Network.enable()

        self.pushButton.clicked.connect(self.get_equipment)

    def call_web(self,equipment):

        # call method with timeout
        self.tab.call_method('Page.navigate',url="http://rmp.global.schindler.com/Equipment/EquipmentMain/EquipmentDetails/?sapSys=ZAP&equnr="+equipment, _timeout=2)
	# wait for loading
        self.tab.wait(2)

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
    signal.signal(signal.SIGINT,signal_handler)
    w.show()
    sys.exit(app.exec_())















