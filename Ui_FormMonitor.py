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
        Form.resize(991, 755)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.web = QtWidgets.QTabWidget(Form)
        self.web.setObjectName("web")
        self.tab_Equipment = QtWidgets.QWidget()
        self.tab_Equipment.setObjectName("tab_Equipment")
        self.label_7 = QtWidgets.QLabel(self.tab_Equipment)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_Equipment)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.label_8.setObjectName("label_8")
        self.textBrowser_Product_Line = QtWidgets.QTextBrowser(self.tab_Equipment)
        self.textBrowser_Product_Line.setGeometry(QtCore.QRect(110, 60, 221, 31))
        self.textBrowser_Product_Line.setObjectName("textBrowser_Product_Line")
        self.textEdit = QtWidgets.QTextEdit(self.tab_Equipment)
        self.textEdit.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_Equipment)
        self.pushButton.setGeometry(QtCore.QRect(370, 10, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.web.addTab(self.tab_Equipment, "")
        self.web1 = QtWidgets.QWidget()
        self.web1.setObjectName("web1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.web1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.web.addTab(self.web1, "")
        self.gridLayout.addWidget(self.web, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.web.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RMP"))
        self.label_7.setText(_translate("Form", "Equipment #"))
        self.label_8.setText(_translate("Form", "Product Line"))
        self.textBrowser_Product_Line.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10000021</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Generate Feedback.docx"))
        self.web.setTabText(self.web.indexOf(self.tab_Equipment), _translate("Form", "Equipment"))
        self.web.setTabText(self.web.indexOf(self.web1), _translate("Form", "web"))

import resources_rc
