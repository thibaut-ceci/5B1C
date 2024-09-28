import matplotlib.pyplot as plt
import pandas as pd

def moyenne(DATAFRAME, label = "moyenne victoire", color = "green"):
    result_all = []

    for i in range(len(DATAFRAME)):
        result_all.append(DATAFRAME.iloc[i, 25:28][1])

    df = pd.DataFrame.from_records(result_all)

    mean_row = pd.DataFrame([df.mean()], columns=df.columns)

    df_with_mean = pd.concat([df, mean_row], ignore_index=True)

    plt.plot(df_with_mean.iloc[-1], ['Botte','1er item','2nd item','3ème item','4ème item','5ème item','6ème item'], marker='o', linestyle='--', label=label, color=color)

def moyennes(DATAFRAME, axe, ligne, label = "moyenne victoire", color = "green"):
    result_all_x = []
    result_all_y = []

    for i in range(len(DATAFRAME)):
        result_all_x.append(DATAFRAME.iloc[i, 17:21].values[0])
        result_all_y.append(DATAFRAME.iloc[i, 17:21].values[ligne])

    df_x = pd.DataFrame.from_records(result_all_x)
    df_y = pd.DataFrame.from_records(result_all_y)

    mean_row_x = pd.DataFrame([df_x.mean()], columns=df_x.columns)
    mean_row_y = pd.DataFrame([df_y.mean()], columns=df_y.columns)

    df_with_mean_x = pd.concat([df_x, mean_row_x], ignore_index=True)
    df_with_mean_y = pd.concat([df_y, mean_row_y], ignore_index=True)

    axe.plot(df_with_mean_x.iloc[-1], df_with_mean_y.iloc[-1], marker='o', linestyle='--', label=label, color=color)
