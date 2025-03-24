import pandas as pd
import os

class Peserta:
    def __init__(self, nama, nim, divisi):
        self.nama = nama
        self.nim = nim
        self.divisi = divisi

class daftarPeserta:
    def __init__(self, file):
        self.file = file
        if not os.path.exists(file) or os.stat(file).st_size == 0:  # Cek apakah file ada dan tidak kosong
            df = pd.DataFrame(columns=["Nama", "NIM", "Divisi"])
            df.to_csv(file, index=False)

        self.csv = pd.read_csv(file)

    def tambahPeserta(self, peserta):
        data_baru = pd.DataFrame([{"Nama": peserta.nama, "NIM": peserta.nim, "Divisi": peserta.divisi}])
        self.csv = pd.concat([self.csv, data_baru], ignore_index=True)
        self.csv.to_csv(self.file, index=False)

    def getDaftarPeserta(self):
        return self.csv
