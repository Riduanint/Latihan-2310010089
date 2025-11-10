# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'larik.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_FormLarik(object):
    def setupUi(self, FormLarik):
        if not FormLarik.objectName():
            FormLarik.setObjectName(u"FormLarik")
        FormLarik.resize(505, 361)
        self.formLayoutWidget = QWidget(FormLarik)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 211, 142))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.EditNama = QLineEdit(self.formLayoutWidget)
        self.EditNama.setObjectName(u"EditNama")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditNama)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.EditLokasi = QLineEdit(self.formLayoutWidget)
        self.EditLokasi.setObjectName(u"EditLokasi")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.EditLokasi)

        self.EditId = QLineEdit(self.formLayoutWidget)
        self.EditId.setObjectName(u"EditId")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditId)

        self.EditIdLarik = QLineEdit(self.formLayoutWidget)
        self.EditIdLarik.setObjectName(u"EditIdLarik")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditIdLarik)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.horizontalLayoutWidget = QWidget(FormLarik)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 180, 211, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Hapus = QPushButton(self.horizontalLayoutWidget)
        self.btn_Hapus.setObjectName(u"btn_Hapus")

        self.horizontalLayout.addWidget(self.btn_Hapus)

        self.btn_Simpan = QPushButton(self.horizontalLayoutWidget)
        self.btn_Simpan.setObjectName(u"btn_Simpan")

        self.horizontalLayout.addWidget(self.btn_Simpan)

        self.btn_Edit = QPushButton(self.horizontalLayoutWidget)
        self.btn_Edit.setObjectName(u"btn_Edit")

        self.horizontalLayout.addWidget(self.btn_Edit)


        self.retranslateUi(FormLarik)

        QMetaObject.connectSlotsByName(FormLarik)
    # setupUi

    def retranslateUi(self, FormLarik):
        FormLarik.setWindowTitle(QCoreApplication.translate("FormLarik", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormLarik", u"ID Pengguna", None))
        self.label_2.setText(QCoreApplication.translate("FormLarik", u"Nama Larik", None))
        self.label_3.setText(QCoreApplication.translate("FormLarik", u"Info Lokasi", None))
        self.label_4.setText(QCoreApplication.translate("FormLarik", u"ID Larik", None))
        self.btn_Hapus.setText(QCoreApplication.translate("FormLarik", u"Hapus", None))
        self.btn_Simpan.setText(QCoreApplication.translate("FormLarik", u"Simpan", None))
        self.btn_Edit.setText(QCoreApplication.translate("FormLarik", u"Edit", None))
    # retranslateUi

