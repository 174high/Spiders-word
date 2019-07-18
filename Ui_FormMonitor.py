# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FormMonitor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1029, 769)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.web = QtWidgets.QTabWidget(Form)
        self.web.setObjectName("web")
        self.tab_Equipment = QtWidgets.QWidget()
        self.tab_Equipment.setObjectName("tab_Equipment")
        self.label_7 = QtWidgets.QLabel(self.tab_Equipment)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.tab_Equipment)
        self.textEdit.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_Equipment)
        self.pushButton.setGeometry(QtCore.QRect(370, 10, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_Equipment)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 221, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.tab_Equipment)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.label_9.setObjectName("label_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_Equipment)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 70, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.web.addTab(self.tab_Equipment, "")
        self.web1 = QtWidgets.QWidget()
        self.web1.setObjectName("web1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.web1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.web.addTab(self.web1, "")
        self.summary = QtWidgets.QWidget()
        self.summary.setObjectName("summary")
        self.process_log = QtWidgets.QPushButton(self.summary)
        self.process_log.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.process_log.setObjectName("process_log")
        self.event_view = QtWidgets.QTableView(self.summary)
        self.event_view.setGeometry(QtCore.QRect(190, 10, 421, 451))
        self.event_view.setObjectName("event_view")
        self.process_event = QtWidgets.QPushButton(self.summary)
        self.process_event.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.process_event.setObjectName("process_event")
        self.event_summary = QtWidgets.QPushButton(self.summary)
        self.event_summary.setGeometry(QtCore.QRect(30, 170, 131, 31))
        self.event_summary.setObjectName("event_summary")
        self.log_summary = QtWidgets.QPushButton(self.summary)
        self.log_summary.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.log_summary.setObjectName("log_summary")
        self.download_excel = QtWidgets.QPushButton(self.summary)
        self.download_excel.setGeometry(QtCore.QRect(30, 220, 131, 31))
        self.download_excel.setObjectName("download_excel")
        self.web.addTab(self.summary, "")
        self.gridLayout.addWidget(self.web, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.web.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RMP"))
        self.label_7.setText(_translate("Form", "Equipment #"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10000021</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Generate one equipment file"))
        self.pushButton_2.setText(_translate("Form", "Generate cube equipment files"))
        self.label_9.setText(_translate("Form", "Portfolio"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A-Ningbo Vanke Guanshanwang 20 units Core landing door</p></body></html>"))
        self.web.setTabText(self.web.indexOf(self.tab_Equipment), _translate("Form", "Equipment"))
        self.web.setTabText(self.web.indexOf(self.web1), _translate("Form", "web"))
        self.process_log.setText(_translate("Form", "process  log"))
        self.process_event.setText(_translate("Form", "process  event"))
        self.event_summary.setText(_translate("Form", "event summary"))
        self.log_summary.setText(_translate("Form", "log summary"))
        self.download_excel.setText(_translate("Form", "download_excel"))
        self.web.setTabText(self.web.indexOf(self.summary), _translate("Form", "summary"))

import resources_rc
