import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
import streamlit as st


def deseq_execute(counts_df,meta):

    print(meta)
    print(counts_df)
    genes_to_keep = counts_df.columns[counts_df.sum(axis=0) >= 10]
    counts_df = counts_df[genes_to_keep]

    inference = DefaultInference(n_cpus=8)
    dds = DeseqDataSet(
        counts=counts_df,
        metadata=meta,
        design_factors=meta.columns[0],
        refit_cooks=True,
        inference=inference,
        # n_cpus=8, # n_cpus can be specified here or in the inference object
    )
    st.info("Starting DESeq2")
    dds.deseq2()
    st.success("DESeq2 completed")
    st.text(dds)
    st.caption("Dispersions")
    st.text(dds.varm["dispersions"])
    st.caption("LFC")
    st.text(dds.varm["LFC"])
    st.info("Running Wald tests")
    stat_res = DeseqStats(dds, inference=inference)
    stat_res.summary()
    st.success("Completed Wald tests")
    # stat_res.results_df.to_csv("lfc_tbl.tsv",sep='\t')
   
    return stat_res.results_df, dds
    # stat_res.summary(lfc_null=0.1, alt_hypothesis="greaterAbs")
    # stat_res.plot_MA(s=20)

    # stat_res.lfc_shrink(coeff="condition_SMA_vs_CONTROL")
