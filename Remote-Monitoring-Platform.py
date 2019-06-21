from PyQt5.QtCore import pyqtSlot, QIODevice, QByteArray 
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

import pychrome
from bs4 import BeautifulSoup
import requests

import datetime
import docx
import signal
import os

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
#        url = 'https://map.baidu.com/search/%E6%98%9F%E5%B7%B4%E5%85%8B/@11671891.22,4104027.879999999,4.86z?querytype=s&c=1&wd=%E6%98%9F%E5%B7%B4%E5%85%8B&da_src=shareurl&on_gel=1&l=4&gr=1&b=(5928478.313716695,1388781.7288436913;17509054.96313347,6618135.872095954)&pn=0&device_ratio=2'
        url="http://localhost:8080/"
        self.browser.load(QUrl(url))
#        self.browser.load(QUrl.fromLocalFile(
#        os.path.abspath('data/map_vue.html')))        

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

        data="Originator: "
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,"JOHNNY")

        data="Entry Date："
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        data="Phone/Mail:"
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,(soup.select("#TaPhoneNumber"))[0]['value'])

        data="Product line ："        
        doc.paragraphs[1]=Word.input_data(doc.paragraphs[1],data,(soup.select("#ProductLineDesc"))[0]['value'])

        data="Zone: "
        doc.paragraphs[1]=Word.input_data(doc.paragraphs[1],data,"N/A")

        data="Clams / PROCITS / PROMs Nr："
        doc.paragraphs[1]=Word.input_data(doc.paragraphs[1],data,"N/A")

        data="Commission No："
        doc.paragraphs[2]=Word.input_data(doc.paragraphs[2],data,(soup.select("#CommisionNumber"))[0]['value'])

        data="Handover to EI: "
        doc.paragraphs[2]=Word.input_data(doc.paragraphs[2],data,"N/A")

        data="Maintenance by Schindler："
        doc.paragraphs[2]=Word.input_data(doc.paragraphs[2],data,"N/A")

        data="Affected Component："
        doc.paragraphs[3]=Word.input_data(doc.paragraphs[3],data,"N/A") 

        data="Number of Units："
        doc.paragraphs[3]=Word.input_data(doc.paragraphs[3],data,"N/A") 

        data="Other product line affected: "
        doc.paragraphs[3]=Word.input_data(doc.paragraphs[3],data,"N/A") 
       
        doc=Word.input_table_data(doc,"City","beijing",4)

#        doc=Word.input_table_data(doc,"Machine Type",(soup.select("#Machine type"))[0]['value'],4)

        doc.save('Feedback.docx')

        doc = docx.Document('rmp info-Template.docx')
        doc=Word.input_table_data(doc,"Equipment #",(soup.select("#Equnr"))[0]['value'],4) 
        doc=Word.input_table_data(doc,"Product Line",(soup.select("#ProductLineDesc"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Address",(soup.select("#Address"))[0]['value'],4)
        doc=Word.input_table_data(doc,"City",(soup.select("#CityAndZip"))[0]['value'],4)
        doc=Word.input_table_data(doc,"CompanyCode",(soup.select("#BukrsDesc"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Controller Type",(soup.select("#ControllerTypeSwVersion"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Gateway Type",(soup.select("#GatewayType"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Serial Number",(soup.select("#SerialNumber"))[0]['value'],4)
        doc=Word.input_table_data(doc,"TM SW Version",(soup.select("#TmSwVersion"))[0]['value'],4)
        doc=Word.input_table_data(doc,"TM State",(soup.select("#TmState"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Environment",(soup.select("#Environment"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Drive Type",(soup.select("#DriveType"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Door Type",(soup.select("#DoorType"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Machine Type",(soup.select("#MachineType"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Workcenter",(soup.select("#Workcenter"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Branch",(soup.select("#Branch"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Commission #",(soup.select("#CommisionNumber"))[0]['value'],4)
        doc=Word.input_table_data(doc,"Equipment Title",(soup.select("#Description"))[0]['value'],4)


        data="Originator: "
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,"JOHNNY")

        data="Entry Date："
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        data="Phone/Mail:"
        doc.paragraphs[0]=Word.input_data(doc.paragraphs[0],data,(soup.select("#TaPhoneNumber"))[0]['value'])

        doc.save('rmp info-result.docx')

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















