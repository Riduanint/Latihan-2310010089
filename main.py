# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from penyiraman import form_penyiraman
from larik import form_larik
from perkembangan import form_perkembangan
from sensor import form_sensor

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('main.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())
        #action
        self.formutama.actionInput_Penyiraman.triggered.connect(self.bukaPenyiraman)
        self.formutama.actionInput_Larik.triggered.connect(self.bukaLarik)
        self.formutama.actionInput_Perkembangan.triggered.connect(self.bukaPerkembangan)
        self.formutama.actionInput_Sensor.triggered.connect(self.bukaSensor)

    def bukaPenyiraman(self):
        self.formpenyiraman = form_penyiraman()
        self.formpenyiraman.show()

    def bukaLarik(self):
        self.formlarik = form_larik()
        self.formlarik.show()

    def bukaPerkembangan(self):
        self.formperkembangan = form_perkembangan()
        self.formperkembangan.show()

    def bukaSensor(self):
        self.formsensor = form_sensor()
        self.formsensor.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())
