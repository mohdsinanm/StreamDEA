import streamlit as st
import pandas as pd
from src.core.analyze.deseq import *
# from src.utils.data_handling.pandas import *

def readfile(file, index_col:int=None, header:int = None,sep=None) -> pd.DataFrame:
    if sep:
        return pd.read_csv(file, sep=sep,index_col=index_col,header=header)
    elif file.name.endswith(".csv"):
        return pd.read_csv(file,index_col=index_col,header=header)
    elif file.name.endswith(".tsv"):
        return pd.read_csv(file, sep='\t',index_col=index_col,header=header)
    elif file.name.endswith(".parquet"):
        return pd.read_parquet(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)

def start_analysis():
    uploaded_file = st.file_uploader("Upload your count data", type=['.tsv','.csv','.parquet','.xlsx'])
    meta_upload = st.file_uploader("Upload metadata")
    count_df = readfile(uploaded_file,sep='\t',index_col=0,header=0)
    meta = readfile(meta_upload,sep=',',index_col=0,header=0)
    st.data_editor(meta)
    st.dataframe(count_df,use_container_width=True)

    if st.button("Start analysis"):
        with st.status('Running',state='running'):
            result = deseq_execute(count_df.T,meta)
    try:
        st.dataframe(result)
    except:
        pass