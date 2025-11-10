import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host ='localhost',
            user ='root',
            password ='',
            database ='sicinamons_db',
        )
    #Table Larik
    def tambahLarik(self, id_larik, id_pengguna, nama_larik, info_lokasi):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO larik (id_larik, id_pengguna, nama_larik, info_lokasi) VALUES (%s, %s, %s, %s)",
            (id_larik, id_pengguna, nama_larik, info_lokasi)
        )
        self.koneksi.commit()
        aksi.close()

    def gantiLarik(self, id_larik, id_pengguna, nama_larik, info_lokasi):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE larik SET id_pengguna = %s, nama_larik = %s, info_lokasi = %s WHERE id_larik = %s",
        (id_pengguna, nama_larik, info_lokasi, id_larik))
        self.koneksi.commit()
        aksi.close()

    def kurangLarik(self, id_larik):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM larik WHERE id_larik = %s",
        (id_larik,))
        self.koneksi.commit()
        aksi.close()

    #Table Datasensor
