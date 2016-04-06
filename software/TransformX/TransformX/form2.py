# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Marco\Desktop\TransformXSoftware\TransformX\TransformX\form2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VueDevellopeur(object):
    def setupUi(self, VueDevellopeur):
        VueDevellopeur.setObjectName(_fromUtf8("VueDevellopeur"))
        VueDevellopeur.resize(844, 750)
        VueDevellopeur.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayoutWidget = QtGui.QWidget(VueDevellopeur)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 321, 605))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Motor11Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor11Change.setMinimum(-120.0)
        self.Motor11Change.setMaximum(120.0)
        self.Motor11Change.setObjectName(_fromUtf8("Motor11Change"))
        self.gridLayout.addWidget(self.Motor11Change, 10, 2, 1, 1)
        self.LabelMotor2 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor2.setObjectName(_fromUtf8("LabelMotor2"))
        self.gridLayout.addWidget(self.LabelMotor2, 1, 0, 1, 1)
        self.LabelMotor3 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor3.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor3.setObjectName(_fromUtf8("LabelMotor3"))
        self.gridLayout.addWidget(self.LabelMotor3, 2, 0, 1, 1)
        self.LabelMotor1 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor1.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor1.setObjectName(_fromUtf8("LabelMotor1"))
        self.gridLayout.addWidget(self.LabelMotor1, 0, 0, 1, 1)
        self.LabelMotor4 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor4.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor4.setObjectName(_fromUtf8("LabelMotor4"))
        self.gridLayout.addWidget(self.LabelMotor4, 3, 0, 1, 1)
        self.LabelMotor6 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor6.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor6.setObjectName(_fromUtf8("LabelMotor6"))
        self.gridLayout.addWidget(self.LabelMotor6, 5, 0, 1, 1)
        self.LabelMotor5 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor5.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor5.setObjectName(_fromUtf8("LabelMotor5"))
        self.gridLayout.addWidget(self.LabelMotor5, 4, 0, 1, 1)
        self.LabelMotor7 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor7.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor7.setObjectName(_fromUtf8("LabelMotor7"))
        self.gridLayout.addWidget(self.LabelMotor7, 6, 0, 1, 1)
        self.LabelMotor9 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor9.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor9.setObjectName(_fromUtf8("LabelMotor9"))
        self.gridLayout.addWidget(self.LabelMotor9, 8, 0, 1, 1)
        self.LabelMotor10 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor10.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor10.setObjectName(_fromUtf8("LabelMotor10"))
        self.gridLayout.addWidget(self.LabelMotor10, 9, 0, 1, 1)
        self.LabelMotor12 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor12.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor12.setObjectName(_fromUtf8("LabelMotor12"))
        self.gridLayout.addWidget(self.LabelMotor12, 14, 0, 1, 1)
        self.LabelMotor11 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor11.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor11.setObjectName(_fromUtf8("LabelMotor11"))
        self.gridLayout.addWidget(self.LabelMotor11, 10, 0, 1, 1)
        self.Motor10Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor10Change.setMinimum(-120.0)
        self.Motor10Change.setMaximum(120.0)
        self.Motor10Change.setObjectName(_fromUtf8("Motor10Change"))
        self.gridLayout.addWidget(self.Motor10Change, 9, 2, 1, 1)
        self.LabelMotor8 = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.LabelMotor8.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelMotor8.setObjectName(_fromUtf8("LabelMotor8"))
        self.gridLayout.addWidget(self.LabelMotor8, 7, 0, 1, 1)
        self.Motor12Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor12Change.setMinimum(-120.0)
        self.Motor12Change.setMaximum(120.0)
        self.Motor12Change.setObjectName(_fromUtf8("Motor12Change"))
        self.gridLayout.addWidget(self.Motor12Change, 14, 2, 1, 1)
        self.Motor7Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor7Change.setMinimum(-120.0)
        self.Motor7Change.setMaximum(120.0)
        self.Motor7Change.setObjectName(_fromUtf8("Motor7Change"))
        self.gridLayout.addWidget(self.Motor7Change, 6, 2, 1, 1)
        self.Motor5Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor5Change.setMinimum(-120.0)
        self.Motor5Change.setMaximum(120.0)
        self.Motor5Change.setObjectName(_fromUtf8("Motor5Change"))
        self.gridLayout.addWidget(self.Motor5Change, 4, 2, 1, 1)
        self.Motor6Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor6Change.setMinimum(-120.0)
        self.Motor6Change.setMaximum(120.0)
        self.Motor6Change.setObjectName(_fromUtf8("Motor6Change"))
        self.gridLayout.addWidget(self.Motor6Change, 5, 2, 1, 1)
        self.Motor9Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor9Change.setMinimum(-120.0)
        self.Motor9Change.setMaximum(120.0)
        self.Motor9Change.setObjectName(_fromUtf8("Motor9Change"))
        self.gridLayout.addWidget(self.Motor9Change, 8, 2, 1, 1)
        self.Motor8Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor8Change.setMinimum(-120.0)
        self.Motor8Change.setMaximum(120.0)
        self.Motor8Change.setObjectName(_fromUtf8("Motor8Change"))
        self.gridLayout.addWidget(self.Motor8Change, 7, 2, 1, 1)
        self.Motor2Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor2Change.setMinimum(-120.0)
        self.Motor2Change.setMaximum(120.0)
        self.Motor2Change.setObjectName(_fromUtf8("Motor2Change"))
        self.gridLayout.addWidget(self.Motor2Change, 1, 2, 1, 1)
        self.Motor3Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor3Change.setMinimum(-120.0)
        self.Motor3Change.setMaximum(120.0)
        self.Motor3Change.setObjectName(_fromUtf8("Motor3Change"))
        self.gridLayout.addWidget(self.Motor3Change, 2, 2, 1, 1)
        self.MotorChange = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.MotorChange.setMinimum(-120.0)
        self.MotorChange.setMaximum(120.0)
        self.MotorChange.setObjectName(_fromUtf8("MotorChange"))
        self.gridLayout.addWidget(self.MotorChange, 0, 2, 1, 1)
        self.Motor4Change = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.Motor4Change.setMinimum(-120.0)
        self.Motor4Change.setMaximum(120.0)
        self.Motor4Change.setObjectName(_fromUtf8("Motor4Change"))
        self.gridLayout.addWidget(self.Motor4Change, 3, 2, 1, 1)
        self.colorPanel = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.colorPanel.setMaximumSize(QtCore.QSize(16777215, 31))
        self.colorPanel.setObjectName(_fromUtf8("colorPanel"))
        self.gridLayout.addWidget(self.colorPanel, 15, 0, 1, 1)
        self.ColorCombo = QtGui.QComboBox(self.gridLayoutWidget)
        self.ColorCombo.setObjectName(_fromUtf8("ColorCombo"))
        self.gridLayout.addWidget(self.ColorCombo, 15, 2, 1, 1)
        self.LabelMotorControl = QtGui.QTextBrowser(VueDevellopeur)
        self.LabelMotorControl.setGeometry(QtCore.QRect(40, 10, 251, 41))
        self.LabelMotorControl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.LabelMotorControl.setFrameShape(QtGui.QFrame.WinPanel)
        self.LabelMotorControl.setFrameShadow(QtGui.QFrame.Raised)
        self.LabelMotorControl.setObjectName(_fromUtf8("LabelMotorControl"))
        self.horizontalLayoutWidget = QtGui.QWidget(VueDevellopeur)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 670, 821, 71))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.GetCurrentPosition_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.GetCurrentPosition_btn.setObjectName(_fromUtf8("GetCurrentPosition_btn"))
        self.horizontalLayout.addWidget(self.GetCurrentPosition_btn)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(VueDevellopeur)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 10, 471, 451))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../Visual Studio 2015/Projects/PythonApplication3/PythonApplication3/TransformX.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.Changementdeforme = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Changementdeforme.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        self.Changementdeforme.setFont(font)
        self.Changementdeforme.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Changementdeforme.setObjectName(_fromUtf8("Changementdeforme"))
        self.verticalLayout_2.addWidget(self.Changementdeforme)
        self.DebutEnregistrementBoutton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.DebutEnregistrementBoutton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        self.DebutEnregistrementBoutton.setFont(font)
        self.DebutEnregistrementBoutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DebutEnregistrementBoutton.setObjectName(_fromUtf8("DebutEnregistrementBoutton"))
        self.verticalLayout_2.addWidget(self.DebutEnregistrementBoutton)
        self.EnregistrerPosition = QtGui.QPushButton(self.verticalLayoutWidget)
        self.EnregistrerPosition.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        self.EnregistrerPosition.setFont(font)
        self.EnregistrerPosition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnregistrerPosition.setObjectName(_fromUtf8("EnregistrerPosition"))
        self.verticalLayout_2.addWidget(self.EnregistrerPosition)
        self.FinEnregistrementBoutton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.FinEnregistrementBoutton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.FinEnregistrementBoutton.setFont(font)
        self.FinEnregistrementBoutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FinEnregistrementBoutton.setObjectName(_fromUtf8("FinEnregistrementBoutton"))
        self.verticalLayout_2.addWidget(self.FinEnregistrementBoutton)
        self.CommandPrompt = QtGui.QTextBrowser(VueDevellopeur)
        self.CommandPrompt.setGeometry(QtCore.QRect(380, 540, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CommandPrompt.setFont(font)
        self.CommandPrompt.setObjectName(_fromUtf8("CommandPrompt"))
        self.LabelVitesse = QtGui.QTextBrowser(VueDevellopeur)
        self.LabelVitesse.setGeometry(QtCore.QRect(369, 506, 301, 31))
        self.LabelVitesse.setMaximumSize(QtCore.QSize(16777215, 31))
        self.LabelVitesse.setObjectName(_fromUtf8("LabelVitesse"))
        self.Vitessenum = QtGui.QDoubleSpinBox(VueDevellopeur)
        self.Vitessenum.setGeometry(QtCore.QRect(690, 510, 111, 22))
        self.Vitessenum.setMinimum(-120.0)
        self.Vitessenum.setMaximum(120.0)
        self.Vitessenum.setObjectName(_fromUtf8("Vitessenum"))
        self.label_2 = QtGui.QLabel(VueDevellopeur)
        self.label_2.setGeometry(QtCore.QRect(14, 15, 821, 721))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("logo.jpg")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(VueDevellopeur)
        self.comboBox.setGeometry(QtCore.QRect(360, 470, 381, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.spinBox = QtGui.QSpinBox(VueDevellopeur)
        self.spinBox.setGeometry(QtCore.QRect(770, 470, 51, 22))
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.LabelMotorControl.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.CommandPrompt.raise_()
        self.LabelVitesse.raise_()
        self.Vitessenum.raise_()
        self.comboBox.raise_()
        self.spinBox.raise_()

        self.retranslateUi(VueDevellopeur)
        QtCore.QMetaObject.connectSlotsByName(VueDevellopeur)
        VueDevellopeur.setTabOrder(self.LabelMotor2, self.LabelMotor3)
        VueDevellopeur.setTabOrder(self.LabelMotor3, self.LabelMotor4)
        VueDevellopeur.setTabOrder(self.LabelMotor4, self.LabelMotor5)
        VueDevellopeur.setTabOrder(self.LabelMotor5, self.LabelMotor6)
        VueDevellopeur.setTabOrder(self.LabelMotor6, self.LabelMotor7)
        VueDevellopeur.setTabOrder(self.LabelMotor7, self.LabelMotor8)
        VueDevellopeur.setTabOrder(self.LabelMotor8, self.LabelMotor9)
        VueDevellopeur.setTabOrder(self.LabelMotor9, self.LabelMotor10)
        VueDevellopeur.setTabOrder(self.LabelMotor10, self.LabelMotor11)
        VueDevellopeur.setTabOrder(self.LabelMotor11, self.LabelMotor12)
        VueDevellopeur.setTabOrder(self.LabelMotor12, self.Motor11Change)

    def retranslateUi(self, VueDevellopeur):
        VueDevellopeur.setWindowTitle(_translate("VueDevellopeur", "Form", None))
        self.LabelMotor2.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 2</span></p></body></html>", None))
        self.LabelMotor3.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 3</span></p></body></html>", None))
        self.LabelMotor1.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 1</span></p></body></html>", None))
        self.LabelMotor4.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 4</span></p></body></html>", None))
        self.LabelMotor6.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 6</span></p></body></html>", None))
        self.LabelMotor5.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 5</span></p></body></html>", None))
        self.LabelMotor7.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 7</span></p></body></html>", None))
        self.LabelMotor9.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 9</span></p></body></html>", None))
        self.LabelMotor10.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 10</span></p></body></html>", None))
        self.LabelMotor12.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 12</span></p></body></html>", None))
        self.LabelMotor11.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 11</span></p></body></html>", None))
        self.LabelMotor8.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 8</span></p></body></html>", None))
        self.colorPanel.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Motor 12</span></p></body></html>", None))
        self.LabelMotorControl.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Controle des moteurs</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("VueDevellopeur", "Changer la position", None))
        self.GetCurrentPosition_btn.setText(_translate("VueDevellopeur", "Recuperer les positions", None))
        self.pushButton.setText(_translate("VueDevellopeur", "Relacher les moteurs", None))
        self.Changementdeforme.setText(_translate("VueDevellopeur", "Changement de forme", None))
        self.DebutEnregistrementBoutton.setText(_translate("VueDevellopeur", "Début de l’Enregistrement de la\n"
" position des moteurs", None))
        self.EnregistrerPosition.setText(_translate("VueDevellopeur", "Enregistrer la position", None))
        self.FinEnregistrementBoutton.setText(_translate("VueDevellopeur", "Fin du mouvement", None))
        self.LabelVitesse.setHtml(_translate("VueDevellopeur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Vitesse de déplacement</span></p></body></html>", None))

