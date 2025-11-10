# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sensor.ui'
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
        Form.resize(473, 454)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 211, 291))
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

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.input_id_larik = QSpinBox(self.formLayoutWidget)
        self.input_id_larik.setObjectName(u"input_id_larik")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_id_larik)

        self.input_nomor_pohon = QSpinBox(self.formLayoutWidget)
        self.input_nomor_pohon.setObjectName(u"input_nomor_pohon")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_nomor_pohon)

        self.input_nitrogen = QDoubleSpinBox(self.formLayoutWidget)
        self.input_nitrogen.setObjectName(u"input_nitrogen")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_nitrogen)

        self.input_fosfor = QDoubleSpinBox(self.formLayoutWidget)
        self.input_fosfor.setObjectName(u"input_fosfor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_fosfor)

        self.input_kalium = QDoubleSpinBox(self.formLayoutWidget)
        self.input_kalium.setObjectName(u"input_kalium")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_kalium)

        self.input_ph = QDoubleSpinBox(self.formLayoutWidget)
        self.input_ph.setObjectName(u"input_ph")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.input_ph)

        self.input_suhu = QDoubleSpinBox(self.formLayoutWidget)
        self.input_suhu.setObjectName(u"input_suhu")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.input_suhu)

        self.input_kelembaban = QDoubleSpinBox(self.formLayoutWidget)
        self.input_kelembaban.setObjectName(u"input_kelembaban")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.input_kelembaban)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 300, 211, 41))
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
        self.label.setText(QCoreApplication.translate("Form", u"IID Larik", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nomor Pohon", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nitrogen", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Fosfor", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Kaloum", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"pH Tanah", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kelembaban (%)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Suhu (C)", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

