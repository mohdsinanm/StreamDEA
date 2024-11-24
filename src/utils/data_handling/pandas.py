import pandas as pd

def readdf(filepath:str, index_col:int=None, header:int = 0) -> pd.DataFrame:

    if filepath.endswith(".csv"):
        return pd.read_csv(filepath,index_col=index_col,header=header)
    elif filepath.endswith(".tsv"):
        return pd.read_csv(filepath, sep='\t',index_col=index_col,header=header)
    elif filepath.endswith(".parquet"):
        return pd.read_parquet(filepath)
    elif filepath.endswith(".xlsx"):
        return pd.read_excel()