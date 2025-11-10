# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'penyiraman.ui'
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
        Form.resize(400, 346)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 251, 251))
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

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.input_id_larik = QSpinBox(self.formLayoutWidget)
        self.input_id_larik.setObjectName(u"input_id_larik")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_id_larik)

        self.input_id_pengguna = QSpinBox(self.formLayoutWidget)
        self.input_id_pengguna.setObjectName(u"input_id_pengguna")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_id_pengguna)

        self.input_durasi_detik = QSpinBox(self.formLayoutWidget)
        self.input_durasi_detik.setObjectName(u"input_durasi_detik")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.input_durasi_detik)

        self.input_jumlah_air = QDoubleSpinBox(self.formLayoutWidget)
        self.input_jumlah_air.setObjectName(u"input_jumlah_air")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.input_jumlah_air)

        self.input_jumlah_kalium = QDoubleSpinBox(self.formLayoutWidget)
        self.input_jumlah_kalium.setObjectName(u"input_jumlah_kalium")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_jumlah_kalium)

        self.input_jumlah_fosfor = QDoubleSpinBox(self.formLayoutWidget)
        self.input_jumlah_fosfor.setObjectName(u"input_jumlah_fosfor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_jumlah_fosfor)

        self.input_jumlah_nitrogen = QDoubleSpinBox(self.formLayoutWidget)
        self.input_jumlah_nitrogen.setObjectName(u"input_jumlah_nitrogen")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_jumlah_nitrogen)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 260, 251, 41))
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
        self.label.setText(QCoreApplication.translate("Form", u"ID Larik", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID Pengguna", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Jumlah Nitrogen (ml)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Jumlah Fosfor (ml)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Jumlah Kalium (ml)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Jumlah Air (ml)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Durasi (detik)", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

