import streamlit as st
import pandas as pd
from src.core.analyze.deseq import *
from src.utils.data_handling.pandas import *
from src.core.analyze.plots import *
import plotly.graph_objects as go
import numpy as np
import plotly


def validate_experiment(count_df, meta):
    if set(count_df.columns.tolist()) == set(meta.index.tolist()):
        print( meta.iloc[:,0].tolist())
        if np.nan not in meta.iloc[:,0].tolist():
            return True
        else:
            st.error(f"There is Null values in the column {meta.columns[0]}, Please Fill it before proceeding")
            return False
    else:
        st.error(f"Your sample names in count matrix and meta data are not matching, Please check")
        return False



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
    col_l, col_r = st.columns([1,1])
    uploaded_file = col_l.file_uploader("Upload your count data", type=['.tsv','.csv','.parquet','.xlsx'])
    meta_upload = col_r.file_uploader("Upload metadata")
    

    if uploaded_file:
        st.session_state['count_df'] = readfile(uploaded_file,index_col=0,header=0)
    if meta_upload:
        st.session_state['meta']= readfile(meta_upload,index_col=0,header=0)

    if st.button("Load demo data"):
        st.session_state['count_df'] = readdf("test/COUNT.tsv",index_col=0)
        st.session_state['meta']= readdf("test/col.tsv",index_col=0)

    col_a, col_b = st.columns([3,7])
    try:
        col_a.caption("Metadata")
        col_a.dataframe( st.session_state['meta'],use_container_width=True)
        col_b.caption("Count matrix")
        col_b.dataframe(st.session_state['count_df'],use_container_width=True)
        exp_val = validate_experiment(st.session_state['count_df'], st.session_state['meta'])
    except:
        pass
    if st.button("Start analysis"):
        try:
            if { "meta", "count_df"}.issubset(set(st.session_state.keys())):
                if exp_val:
                    with st.status('Running',state='running'):
                        st.session_state['result'], st.session_state['dds'] = deseq_execute(st.session_state['count_df'].T.fillna(0), st.session_state['meta'])
                else:
                    st.error("Please resolve the errors")
            else:
                st.error("Please upload metadata and count matrix")
        except:
            pass
    try:
        
        fig = plot_pca(st.session_state['dds'],st.session_state['meta'].columns[0])
        col_a, col_b, col_c = st.columns([1,6,1])

       

        # plotly_fig = plotly.tools.mpl_to_plotly(fig)

        # # Update layout to adjust size and margins
        # plotly_fig.update_layout(
        #     width=1000,  # Set the desired width
        #     height=600,  # Set the desired height
        #     margin=dict(l=100, r=300, t=100, b=100)  # Adjust margins (left, right, top, bottom)
        # )
        col_b.plotly_chart(fig,use_container_width=True)

        with st.expander("Heatmap"):
            col_a, col_b = st.columns([1,1])
            lfc = col_a.number_input("LogFC cutoff", value=0.5)
            pval = col_b.number_input("P-adjusted",value=0.05)
            sigs = st.session_state['result'][(st.session_state['result'].padj < pval) & (abs(st.session_state['result'].log2FoldChange) > lfc)]
            plt = heat(st.session_state['dds'],sigs)
            st.pyplot(plt)
    except Exception as e:
        print(e)
    try:
        st.dataframe(st.session_state['result'],use_container_width=True)
    except:
        pass