import scanpy as sc
import numpy as np
import numpy as np
import seaborn as sns
import pandas as pd

def plot_pca(dds,column_name):
    sc.tl.pca(dds)
    return sc.pl.pca(dds, color = column_name, size = 200,return_fig=True)

def heat(dds,sigs):

    dds.layers['log1p'] = np.log1p(dds.layers['normed_counts'])
    dds_sigs = dds[:, sigs.index]
    grapher = pd.DataFrame(dds_sigs.layers['log1p'].T,
                       index=dds_sigs.var_names, columns=dds_sigs.obs_names)
    return sns.clustermap(grapher, z_score=0, cmap = 'RdYlBu_r')

