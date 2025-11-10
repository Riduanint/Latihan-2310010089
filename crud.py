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

    #Table Perkembangan
    def tambahLogperkembangan(self, id_log, id_pengguna, nomor_pohon, waktu_catat, diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO logperkembangan (id_log, id_pengguna, nomor_pohon, waktu_catat, diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_log, id_pengguna, nomor_pohon, waktu_catat, diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max))
        self.koneksi.commit()
        aksi.close()

    def gantiLogperkembangan(self, id_log, id_pengguna, nomor_pohon, waktu_catat, diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "UPDATE logperkembangan SET id_pengguna = %s, nomor_pohon = %s, waktu_catat = %s, diameter = %s, tinggi = %s, hitung_biomassa = %s, hitung_minyak_min = %s, hitung_minyak_max = %s "
            "WHERE id_log = %s",
        (id_pengguna, nomor_pohon, waktu_catat, diameter, tinggi, hitung_biomassa, hitung_minyak_min, hitung_minyak_max, id_log))
        self.koneksi.commit()
        aksi.close()

    def kurangLogperkembangan(self, id_log):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM logperkembangan WHERE id_log = %s",
        (id_log,))
        self.koneksi.commit()
        aksi.close()
