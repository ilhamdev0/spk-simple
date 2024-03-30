import interfaces
import pandas as pd

class CSVInput(interfaces.Input):
    def __init__(self):
        self.namafile = "input.csv"

    def filetidakada(self):
        pesan = f"File {self.namafile} tidak ditemukan!"
        print(pesan)

    def open(self):
        try:
            df = pd.read_csv(self.namafile)
            return df
        except FileNotFoundError as fileerror:
            self.filetidakada()
            return []

class CSVConfig(interfaces.Input):
    def __init__(self):
        self.namafile = "config.csv"

    def filetidakada(self):
        pesan = f"File {self.namafile} tidak ditemukan!"
        print(pesan)

    def open(self):
        try:
            df = pd.read_csv(self.namafile)
            return df
        except FileNotFoundError as fileerror:
            self.filetidakada()
            return []