# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(873, 490)
        MainWindow.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 161, 107);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 6, 0, 1, 3)

        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 224, 196);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 20px ;")

        self.gridLayout.addWidget(self.input, 7, 0, 1, 3)

        self.btn_copy_to_clipboard = QPushButton(self.centralwidget)
        self.btn_copy_to_clipboard.setObjectName(u"btn_copy_to_clipboard")
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setPointSize(13)
        font.setBold(True)
        self.btn_copy_to_clipboard.setFont(font)
        self.btn_copy_to_clipboard.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 210, 120);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 10px ;")

        self.gridLayout.addWidget(self.btn_copy_to_clipboard, 10, 2, 1, 1)

        self.l_breaker = QRadioButton(self.centralwidget)
        self.l_breaker.setObjectName(u"l_breaker")
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(13)
        self.l_breaker.setFont(font1)
        self.l_breaker.setStyleSheet(u"color: rgb(255, 184, 43);")

        self.gridLayout.addWidget(self.l_breaker, 4, 0, 1, 1)

        self.p_breaker = QRadioButton(self.centralwidget)
        self.p_breaker.setObjectName(u"p_breaker")
        self.p_breaker.setFont(font1)
        self.p_breaker.setStyleSheet(u"color: rgb(255, 184, 43);")

        self.gridLayout.addWidget(self.p_breaker, 5, 0, 1, 1)

        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 224, 196);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 20px ;")

        self.gridLayout.addWidget(self.output, 9, 0, 1, 3)

        self.btn_line_breaker = QPushButton(self.centralwidget)
        self.btn_line_breaker.setObjectName(u"btn_line_breaker")
        self.btn_line_breaker.setFont(font)
        self.btn_line_breaker.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 210, 120);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 10px ;")

        self.gridLayout.addWidget(self.btn_line_breaker, 8, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 184, 43);")

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.titr = QLabel(self.centralwidget)
        self.titr.setObjectName(u"titr")
        font3 = QFont()
        font3.setFamilies([u"Dosis ExtraBold"])
        font3.setPointSize(25)
        font3.setBold(True)
        self.titr.setFont(font3)
        self.titr.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 210, 120);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 20px ;")

        self.gridLayout.addWidget(self.titr, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Text Editor", None))
        self.btn_copy_to_clipboard.setText(QCoreApplication.translate("MainWindow", u"Copy to ClipBoard", None))
        self.l_breaker.setText(QCoreApplication.translate("MainWindow", u"Remove line breaks only", None))
        self.p_breaker.setText(QCoreApplication.translate("MainWindow", u"Remove line breaks and paragraph breaks", None))
        self.btn_line_breaker.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Text without Line Breaks", None))
        self.titr.setText(QCoreApplication.translate("MainWindow", u"   Remove Line Breaks", None))
    # retranslateUi

