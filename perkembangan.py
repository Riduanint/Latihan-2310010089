# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class form_perkembangan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('perkembangan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formperkembangan = muatfile.load(filenya,self)
        self.aksi = crud()

        self.formperkembangan.btn_Simpan.clicked.connect(self.simpanperkembangan)
        self.formperkembangan.btn_Edit.clicked.connect(self.ubahperkembangan)
        self.formperkembangan.btn_Hapus.clicked.connect(self.hapusperkembangan)

    def simpanperkembangan(self):
        id_log = self.formperkembangan.EditLog.text()
        id_pengguna = self.formperkembangan.EditId.text()
        nomor_pohon = self.formperkembangan.EditPohon.text()
        waktu_catat = self.formperkembangan.EditWaktu.text()
        diameter = self.formperkembangan.EditDiameter.text()
        tinggi = self.formperkembangan.EditTinggi.text()
        hitung_biomassa = self.formperkembangan.EditBiomassa.text()
        hitung_minyak_min = self.formperkembangan.EditMinyakMin.text()
        hitung_minyak_max = self.formperkembangan.EditMinyakMax.text()
        self.aksi.tambahLogperkembangan(id_log, id_pengguna, nomor_pohon, waktu_catat,diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max)

    def ubahperkembangan(self):
        id_log = self.formperkembangan.EditLog.text()
        id_pengguna = self.formperkembangan.EditId.text()
        nomor_pohon = self.formperkembangan.EditPohon.text()
        waktu_catat = self.formperkembangan.EditWaktu.text()
        diameter = self.formperkembangan.EditDiameter.text()
        tinggi = self.formperkembangan.EditTinggi.text()
        hitung_biomassa = self.formperkembangan.EditBiomassa.text()
        hitung_minyak_min = self.formperkembangan.EditMinyakMin.text()
        hitung_minyak_max = self.formperkembangan.EditMinyakMax.text()
        self.aksi.gantiLogperkembangan(id_log, id_pengguna, nomor_pohon, waktu_catat,diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max)

    def hapusperkembangan(self):
        id_log = self.formperkembangan.EditLog.text()
        self.aksi.kurangLogperkembangan(id_log)
