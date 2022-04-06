import pandas as pd
from baselines.scripts_python.python_packages.CITMI.citmi import PCTMI, TPCTMI, TPCMCITMI
# from baselines.scripts_python.python_packages.CITMI.citmi_simple import PCTMI


def pctmi(data, sig_level=0.05, nlags=5, verbose=True):
    citmi = PCTMI(data, sig_lev=sig_level, lag_max=nlags, p_value=True, rank_using_p_value=False, verbose=verbose,
               num_processor=-1, graphical_optimization=False)

    g_array = citmi.fit()
    g_df = pd.DataFrame(g_array, columns=data.columns, index=data.columns, dtype=int)
    return g_df


def tpctmi(data, sig_level=0.05, nlags=5, verbose=True):
    citmi = TPCTMI(data, sig_lev=sig_level, lag_max=nlags, p_value=True, rank_using_p_value=False, verbose=verbose,
               num_processor=-1, graphical_optimization=False)
    g_dict = citmi.fit()
    # g_df = pd.DataFrame(g_array, columns=data.columns, index=data.columns, dtype=int)
    return g_dict


def tpcmcitmi(data, sig_level=0.05, nlags=5, verbose=True):
    citmi = TPCMCITMI(data, sig_lev=sig_level, lag_max=nlags, p_value=True, rank_using_p_value=False, verbose=verbose,
               num_processor=-1, graphical_optimization=False)
    g_dict = citmi.fit()
    # g_df = pd.DataFrame(g_array, columns=data.columns, index=data.columns, dtype=int)
    return g_dict



if __name__ == "__main__":
    import os
    structure = "diamond"
    print(os.getcwd())
    path = "../../data/simulated_ts_data/"+str(structure)+"/data_"+str(0)+".csv"
    data = pd.read_csv(path, delimiter=',', index_col=0)
    data = data.loc[:1000]
    print(data)
    df = pctmi(data, sig_level=0.05, nlags=5, verbose=True)
    print(df)

