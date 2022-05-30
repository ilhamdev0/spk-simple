import pandas as pd
import numpy as np
import config

# Normalizer function menggunakan MinMax scaler
def _maximizer(data):
    formula = (data - data.min()) / (data.max() - data.min())
    # mengeliminasi NaN jika ada
    hasil = np.nan_to_num(formula)
    return hasil

def _minimizer(data):
    formula = (data.max() - data) / (data.max() - data.min())
    # mengeliminasi NaN jika ada
    hasil = np.nan_to_num(formula)
    return hasil

# Output ke file dan terminal
def _output_top(df, score):
    # Hitung percentile untuk peringkat teratas
    quantile_top = score.quantile(q=0.75, interpolation='nearest')
    top = df[df["rank"] >= quantile_top]

    top.to_csv(config.outputtopfile, index=False, encoding='utf-8')

    print("\nRekomendasi Teratas:\n")
    print(top.to_string(index=False))
    print("\n")

def _output_all(score):
    df_out = pd.read_csv(config.inputfile)

    df_out["rank"] = score
    df_out = df_out.sort_values(by=["rank"], ascending=False)

    df_out.to_csv(config.outputfile, index=False, encoding='utf-8')

    _output_top(df_out, score)

def run():
    df = pd.read_csv(config.inputfile)
    df_config = pd.read_csv(config.configfile)

    for i in df_config.index:
        current_pos = df_config.loc[i]
        current_field = current_pos['field']
        current_kriteria = current_pos['kriteria']
        current_weight = current_pos['weight']

        # Normalisasi
        if current_kriteria == "min":
            current_normalized = _minimizer(df[current_field])
        elif current_kriteria == "max":
            current_normalized = _maximizer(df[current_field])
        
        # Pembobotan
        df[current_field] = current_normalized * current_weight

    score = df.sum(axis = 1, numeric_only = True)
    _output_all(score)
