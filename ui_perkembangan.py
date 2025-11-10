# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perkembangan.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 201, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.input_id_pengguna = QSpinBox(self.formLayoutWidget)
        self.input_id_pengguna.setObjectName(u"input_id_pengguna")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_id_pengguna)

        self.input_nomor_pohon = QSpinBox(self.formLayoutWidget)
        self.input_nomor_pohon.setObjectName(u"input_nomor_pohon")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_nomor_pohon)

        self.input_diameter = QDoubleSpinBox(self.formLayoutWidget)
        self.input_diameter.setObjectName(u"input_diameter")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_diameter)

        self.input_tinggi = QDoubleSpinBox(self.formLayoutWidget)
        self.input_tinggi.setObjectName(u"input_tinggi")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_tinggi)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 150, 201, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_batal = QPushButton(self.horizontalLayoutWidget)
        self.btn_batal.setObjectName(u"btn_batal")

        self.horizontalLayout.addWidget(self.btn_batal)

        self.btn_ok = QPushButton(self.horizontalLayoutWidget)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Pengguna", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nomor Pohon", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Diameter (cm)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tinggi (m)", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

