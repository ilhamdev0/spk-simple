import interfaces
import pandas as pd
import numpy as np

class Config(interfaces.Config):
    def __init__(self, input: interfaces.Input, config: interfaces.Input, configoutput: interfaces.Output):
        self.input = input
        self.config = config
        self.configoutput = configoutput

    def create(self):
        header = ['field','kriteria','weight']
        
        df = pd.read_csv(self.input.namafile)

        df_config = pd.DataFrame(data=None,
            columns=header
        )

        numeric_column_only = df.select_dtypes(include='number').columns

        for i in numeric_column_only:
            newconfig = pd.DataFrame([[i,'-',0]],columns=header)
            df_config = pd.concat([df_config,newconfig])

        return df_config
    
    def verify(self, datainput, dataconfig):
        header_data_input = np.array(datainput.select_dtypes(include='number').columns)
        header_data_config = np.array(dataconfig["field"])

        # Cek header antara config dengan input, jika tidak sama maka buat config baru
        if not np.array_equal(header_data_input,header_data_config):
            data = self.create()
            self.configoutput.save(data)

            print("Config telah diupdate! harap mengedit field \"kriteria\" dan \"weight\" sesuai kebutuhan")
            exit()
        
        kriteria_config = np.array(dataconfig["kriteria"])
        kriteria_valid_string = np.array(["min","max"])

        # Cek didalam config apakah masih terdapat kriteria yang belum diedit
        if bool(np.setdiff1d(kriteria_config, kriteria_valid_string).size):
            print(f"Harap edit dan periksa field \"kriteria\" di file {self.config.namafile} ganti \"-\" dengan \"min\" atau \"max\"")
            exit()
        
        # Cek apakah nilai weight sudah sesuai
        weight_config = dataconfig["weight"]
        total_weight = weight_config.sum()

        if total_weight == 0:
            print(f"Nilai pada field \"weight\" tidak boleh kosong! sistem tidak dapat membuat ranking!")
            exit()

        if total_weight != 1:
            print(f"Warning :: Nilai weight tidak sesuai = {total_weight}")

class Logic(interfaces.Logic):
    def __init__(self, input: interfaces.Input, config: interfaces.Input, output: interfaces.Output):
        self.input = input
        self.config = config
        self.output = output
    
    def normalizer_max(self, data):
        formula = (data - data.min()) / (data.max() - data.min())
        # mengeliminasi NaN jika ada
        hasil = np.nan_to_num(formula)
        return hasil

    def normalizer_min(self, data):
        formula = (data.max() - data) / (data.max() - data.min())
        # mengeliminasi NaN jika ada
        hasil = np.nan_to_num(formula)
        return hasil
    
    def score(self):
        loadinput = self.input.open()
        temp = self.input.open()
        loadconfig = self.config.open()

        for i in loadconfig.index:
            current_pos = loadconfig.loc[i]
            current_field = current_pos['field']
            current_kriteria = current_pos['kriteria']
            current_weight = current_pos['weight']

            # Normalisasi
            if current_kriteria == "min":
                current_normalized = self.normalizer_min(temp[current_field])
            elif current_kriteria == "max":
                current_normalized = self.normalizer_max(temp[current_field])
            
            # Pembobotan
            temp[current_field] = current_normalized * current_weight

        score = temp.sum(axis = 1, numeric_only = True)

        # Merge score dan sort data
        loadinput["rank"] = score
        loadinput = loadinput.sort_values(by=["rank"], ascending=False)

        return loadinput
    
    def topscore(self, data, rank):
        quantile_top = rank.quantile(q=0.75, interpolation='nearest')
        top = data[data["rank"] >= quantile_top]

        return top