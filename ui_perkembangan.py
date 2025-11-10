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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(481, 435)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 201, 311))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.EditId = QLineEdit(self.formLayoutWidget)
        self.EditId.setObjectName(u"EditId")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditId)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.EditPohon = QLineEdit(self.formLayoutWidget)
        self.EditPohon.setObjectName(u"EditPohon")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditPohon)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.EditWaktu = QLineEdit(self.formLayoutWidget)
        self.EditWaktu.setObjectName(u"EditWaktu")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.EditWaktu)

        self.EditDiameter = QLineEdit(self.formLayoutWidget)
        self.EditDiameter.setObjectName(u"EditDiameter")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.EditDiameter)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.EditTinggi = QLineEdit(self.formLayoutWidget)
        self.EditTinggi.setObjectName(u"EditTinggi")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.EditTinggi)

        self.EditBiomassa = QLineEdit(self.formLayoutWidget)
        self.EditBiomassa.setObjectName(u"EditBiomassa")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.EditBiomassa)

        self.EditMinyakMin = QLineEdit(self.formLayoutWidget)
        self.EditMinyakMin.setObjectName(u"EditMinyakMin")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.EditMinyakMin)

        self.EditMinyakMax = QLineEdit(self.formLayoutWidget)
        self.EditMinyakMax.setObjectName(u"EditMinyakMax")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.EditMinyakMax)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 320, 201, 31))
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"ID Log", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Pengguna", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nomor Pohon", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Waktu Catat", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Diameter (cm)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tinggi (m)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Hitung Biomasa", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Minyak Minimal", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Minyak Max", None))
        self.btn_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btn_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btn_Edit.setText(QCoreApplication.translate("Form", u"Edit", None))
    # retranslateUi

