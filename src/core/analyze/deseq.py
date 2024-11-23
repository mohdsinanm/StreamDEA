import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats

def deseq_execute(counts_df,meta):

    print(meta)
    print(counts_df)
    genes_to_keep = counts_df.columns[counts_df.sum(axis=0) >= 10]
    counts_df = counts_df[genes_to_keep]

    inference = DefaultInference(n_cpus=8)
    dds = DeseqDataSet(
        counts=counts_df,
        metadata=meta,
        design_factors="condition",
        refit_cooks=True,
        inference=inference,
        # n_cpus=8, # n_cpus can be specified here or in the inference object
    )
    dds.deseq2()

    print(dds)

    print(dds.varm["dispersions"])

    print(dds.varm["LFC"])

    stat_res = DeseqStats(dds, inference=inference)

    stat_res.summary()
    # stat_res.results_df.to_csv("lfc_tbl.tsv",sep='\t')
    return stat_res.results_df
    # stat_res.summary(lfc_null=0.1, alt_hypothesis="greaterAbs")
    # stat_res.plot_MA(s=20)

    # stat_res.lfc_shrink(coeff="condition_SMA_vs_CONTROL")
