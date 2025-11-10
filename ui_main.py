# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionInput_Larik = QAction(MainWindow)
        self.actionInput_Larik.setObjectName(u"actionInput_Larik")
        self.actionInput_Sensor = QAction(MainWindow)
        self.actionInput_Sensor.setObjectName(u"actionInput_Sensor")
        self.actionInput_Penyiraman = QAction(MainWindow)
        self.actionInput_Penyiraman.setObjectName(u"actionInput_Penyiraman")
        self.actionInput_Perkembangan = QAction(MainWindow)
        self.actionInput_Perkembangan.setObjectName(u"actionInput_Perkembangan")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMain_Window = QMenu(self.menubar)
        self.menuMain_Window.setObjectName(u"menuMain_Window")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain_Window.menuAction())
        self.menuMain_Window.addSeparator()
        self.menuMain_Window.addAction(self.actionInput_Larik)
        self.menuMain_Window.addAction(self.actionInput_Sensor)
        self.menuMain_Window.addAction(self.actionInput_Penyiraman)
        self.menuMain_Window.addAction(self.actionInput_Perkembangan)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInput_Larik.setText(QCoreApplication.translate("MainWindow", u"Input Data Larik", None))
        self.actionInput_Sensor.setText(QCoreApplication.translate("MainWindow", u"Input Data Sensor", None))
        self.actionInput_Penyiraman.setText(QCoreApplication.translate("MainWindow", u"Input Log Penyiraman", None))
        self.actionInput_Perkembangan.setText(QCoreApplication.translate("MainWindow", u"Input Log Perkembangan", None))
        self.menuMain_Window.setTitle(QCoreApplication.translate("MainWindow", u"HALAMAN UTAMA", None))
    # retranslateUi

