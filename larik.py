# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class form_larik(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('larik.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formlarik = muatfile.load(filenya,self)
        self.aksi = crud()

        self.formlarik.btn_Simpan.clicked.connect(self.simpanlarik)
        self.formlarik.btn_Edit.clicked.connect(self.ubahlarik)
        self.formlarik.btn_Hapus.clicked.connect(self.hapuslarik)

    def simpanlarik(self):
        id_larik = self.formlarik.EditIdLarik.text()
        id_pengguna = self.formlarik.EditId.text()
        nama_larik = self.formlarik.EditNama.text()
        info_lokasi = self.formlarik.EditLokasi.text()
        self.aksi.tambahLarik(id_larik, id_pengguna, nama_larik, info_lokasi)

    def ubahlarik(self):
        id_larik = self.formlarik.EditIdLarik.text()
        id_pengguna = self.formlarik.EditId.text()
        nama_larik = self.formlarik.EditNama.text()
        info_lokasi = self.formlarik.EditLokasi.text()
        self.aksi.gantiLarik(id_larik, id_pengguna, nama_larik, info_lokasi)

    def hapuslarik(self):
        # HARUS menggunakan EditIdLarik untuk menghapus larik
        id_larik = self.formlarik.EditIdLarik.text()
        self.aksi.kurangLarik(id_larik)
