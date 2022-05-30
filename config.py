import pandas as pd
import numpy as np

inputfile = "input.csv"
outputfile = "out/output.csv"
outputtopfile = "out/top.csv"
configfile = "config.csv"


def _configsudahvalid():
    df_input = pd.read_csv(inputfile)
    df_config = pd.read_csv(configfile)

    column_df_input = df_input.select_dtypes(include='number').columns

    column_df_input = np.array(column_df_input)
    column_df_config = np.array(df_config["field"])

    # Cek antara config dengan input menggunakan operasi himpunan
    cek = np.setdiff1d(column_df_input, column_df_config)

    if cek.size > 0:
        raise ValueError("not valid")

    kriteria_df_config = np.array(df_config["kriteria"])
    kriteria_valid_string = np.array(["min","max"])

    # Cek didalam config apakah masih terdapat kriteria yang belum sesuai menggunakan operasi himpunan
    cek = np.setdiff1d(kriteria_df_config, kriteria_valid_string)

    if cek.size > 0:
        raise ValueError("not edited")
    
    # Cek apakah nilai weight sudah sesuai
    weight_df_config = df_config["weight"]
    total_weight = weight_df_config.sum()

    if total_weight == 0:
        print(f"Warning! :: Nilai weight kosong! sistem tidak dapat membuat ranking")

    if total_weight != 1:
        print(f"Warning! :: Nilai weight tidak sesuai = {total_weight}")
    
def _buatconfigbaru():
    df = pd.read_csv(inputfile)

    df_config = pd.DataFrame(data=None,
        columns=['field','kriteria','weight']
    )

    numeric_column_only = df.select_dtypes(include='number').columns

    for i in numeric_column_only:
        newconfig = pd.DataFrame([[i,'DEFAULT',0]],columns=['field','kriteria','weight'])
        df_config = pd.concat([df_config,newconfig])

    # Simpan ke file
    df_config.to_csv(configfile, index=False, encoding='utf-8')

def run():
    try:
        _configsudahvalid()
    except FileNotFoundError as fileerror:
        if configfile in str(fileerror):
            print("Config belum dibuat! Sistem akan membuat config baru...")

            _buatconfigbaru()

            print("Config telah dibuat! jangan lupa untuk mengedit field \"kriteria\" dan \"weight\" sesuai kebutuhan")

            exit()
        
        if inputfile in str(fileerror):
            print(f"File {inputfile} tidak ditemukan!")
            exit()

    except ValueError as programerror:
        if str(programerror) == "not valid":
            print("Config tidak sesuai dengan input! Sistem akan mengupdate config")

            _buatconfigbaru()

            print("Config telah diupdate! jangan lupa untuk mengedit field \"kriteria\" dan \"weight\" sesuai kebutuhan")

            exit()
        
        if str(programerror) == "not edited":
            print("Harap edit dan periksa field \"kriteria\" di file config! pastikan diisi dengan \"min\" atau \"max\"")
            exit()
    