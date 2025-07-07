import pandas as pd

def load_data():
    df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding= 'ISO-8859-1')
    print("✅ Data loaded:", df.shape)
    return df
