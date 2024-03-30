import interfaces
import pandas as pd

class CSVConfigOutput(interfaces.Output):
    def __init__(self):
        self.namafile = "config.csv"

    def save(self,data):
       data.to_csv(self.namafile, index=False, encoding='utf-8')

class CSVTopOutput(interfaces.Output):
    def __init__(self):
        self.namafile = "out/output-top.csv"

    def save(self,data):
       data.to_csv(self.namafile, index=False, encoding='utf-8')

class CSVOutput(interfaces.Output):
    def __init__(self):
        self.namafile = "out/output.csv"

    def save(self,data):
       data.to_csv(self.namafile, index=False, encoding='utf-8')

class TerminalOutput(interfaces.Output):
    def __init__(self):
        self.namafile = "out/output.csv"
    
    def save(self):
        pass
    
    def show(self):
        df = pd.read_csv(self.namafile)
        print(df)