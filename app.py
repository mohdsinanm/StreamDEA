import streamlit as st
from src.utils.streamlit_utils.utils import *
from src.core.analyze.analyze_main import start_analysis


def home_main():
    text = """
            Our web platform enables you to perform Differential Expression Analysis (DEA) on RNA-Seq count data with ease.
            Using the powerful pyDESeq module, based on the DESeq2 method, you can quickly analyze gene expression differences between experimental conditions.
            Simply upload your count matrix and metadata, and the platform will automatically process your data, identify differentially expressed genes, and provide comprehensive results, including log-fold changes, p-values, and visualizations like volcano plots and heatmaps.
            Get started today to uncover the insights hidden in your RNA-Seq data!
            """
    st.markdown("**Differential Expression Analysis (DEA) for RNA-Seq Data**")
    st.markdown(text)

def main():
    st.set_page_config(
    page_title="StreamDEA",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    )

    render_text("StreamDEA", 35,-40,-1)

    home, analyze, about = st.tabs(['Home',"Analyze","About",])

    with home:
        home_main()
    
    with analyze:
        start_analysis()


main()