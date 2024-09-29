import ast

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def display_parameters(pd):
    """
    Affiche toutes les colonnes et lignes du DataFrame.
    """
    pd.set_option("display.max_rows",None)      ## Afficher toutes les lignes
    pd.set_option("display.max_columns",None)   ## Afficher toutes les colonnes
    pd.set_option("display.width",None)         ## Ajuster la largeur
    pd.set_option("display.max_colwidth",None)  ## Display entire content of each column


def convert_to_list(broken_list):
    """
    Convertir une chaîne en liste si possible.
    
    Entrée :
    --------
    broken_list : str
        Chaîne à convertir.
    
    Sortie :
    --------
    list
        Liste convertie ou chaîne d'origine en cas d'échec de la conversion.
    """
     
    ## Répare la liste
    try:
        return ast.literal_eval(broken_list)
    
    ## Renvoie la liste d'origine en cas d'erreur
    except (ValueError, SyntaxError):
        return broken_list


def repair_list_in_df(df1, df2, list_columns):
    """
    Répare les colonnes spécifiées dans deux dataframes en les convertissant en liste.
    
    Entrée :
    --------
    df1 : pandas.DataFrame
        Premier dataframe à traiter.
    df2 : pandas.DataFrame
        Deuxième dataframe à traiter.
    
    Sortie :
    --------
    df1 : pandas.DataFrame
        Premier dataframe réparé.
    df2 : pandas.DataFrame
        Deuxième dataframe réparé.
    """
    
    for col in list_columns:
        df1[col] = df1[col].apply(convert_to_list)
        df2[col] = df2[col].apply(convert_to_list)

    return df1, df2


def plot_colonnes(df1, df2, colonne, ylabel, plot_games = True):
    plt.figure(figsize=(10, 6), dpi=150)

    ## Boucle sur toutes le dataframe pour les victoires
    if plot_games == True:
        for index_game, _ in df1.iterrows():
            plt.plot(df1["Temps numérique"][index_game], df1[colonne][index_game], marker='o', label="Game de " + str(df1["Nom du joueur"][index_game]), color="green")

        ## Boucle sur toutes le dataframe pour les défaites
        for index_game, _ in df2.iterrows():
            plt.plot(df2["Temps numérique"][index_game], df2[colonne][index_game], marker='o', label="Game de " + str(df2["Nom du joueur"][index_game]), color="red")

    moyennes(df1, plt, colonne, label="moyenne victoire", color="green")
    moyennes(df2, plt, colonne, label="moyenne défaite", color="red")

    zone(df1, colonne, label='Zone de victoire', color='green')
    zone(df2, colonne, label='Zone de défaite', color='red')

    plt.title('Évolution des kills au cours des parties')
    plt.xlabel('Temps (minutes)')
    plt.ylabel(ylabel)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid()

    plt.tight_layout()
    plt.show()









def moyennes(DATAFRAME, axe, ligne, label = "moyenne victoire", color = "green"):

    colonne0 = []
    colonne230 = []
    colonne5 = []
    colonne730 = []
    colonne10 = []
    colonne123 = []
    colonne15 = []
    colonne173 = []
    colonne20 = []
    colonne223 = []
    colonne25 = []
    colonne273 = []
    colonne30 = []

    for game in DATAFRAME[ligne]:
        try:
            colonne0.append(game[0])
            colonne230.append(game[1])
            colonne5.append(game[2])
            colonne730.append(game[3])
            colonne10.append(game[4])
            colonne123.append(game[5])
            colonne15.append(game[6])
            colonne173.append(game[7])
            colonne20.append(game[8])
            colonne223.append(game[9])
            colonne25.append(game[10])
            colonne273.append(game[11])
            colonne30.append(game[12])
        except IndexError:
            #("Pas de kill")
            continue

    max_length = max(len(colonne0), len(colonne230), len(colonne5), len(colonne730),
                    len(colonne10), len(colonne123), len(colonne15), len(colonne173),
                    len(colonne20), len(colonne223), len(colonne25), len(colonne273),
                    len(colonne30))

    # Compléter les listes avec des NaN jusqu'à la longueur maximale
    colonne0 += [np.nan] * (max_length - len(colonne0))
    colonne230 += [np.nan] * (max_length - len(colonne230))
    colonne5 += [np.nan] * (max_length - len(colonne5))
    colonne730 += [np.nan] * (max_length - len(colonne730))
    colonne10 += [np.nan] * (max_length - len(colonne10))
    colonne123 += [np.nan] * (max_length - len(colonne123))
    colonne15 += [np.nan] * (max_length - len(colonne15))
    colonne173 += [np.nan] * (max_length - len(colonne173))
    colonne20 += [np.nan] * (max_length - len(colonne20))
    colonne223 += [np.nan] * (max_length - len(colonne223))
    colonne25 += [np.nan] * (max_length - len(colonne25))
    colonne273 += [np.nan] * (max_length - len(colonne273))
    colonne30 += [np.nan] * (max_length - len(colonne30))

    data = {
        'Colonne 0': colonne0,
        'Colonne 230': colonne230,
        'Colonne 5': colonne5,
        'Colonne 730': colonne730,
        'Colonne 10': colonne10,
        'Colonne 123': colonne123,
        'Colonne 15': colonne15,
        'Colonne 173': colonne173,
        'Colonne 20': colonne20,
        'Colonne 223': colonne223,
        'Colonne 25': colonne25,
        'Colonne 273': colonne273,
        'Colonne 30': colonne30,
    }

    # Créer le DataFrame
    df = pd.DataFrame(data)

    for column_name, _ in df.items():
        if column_name == "Colonne 0":
            continue

        if df[column_name].nunique() == 1:
            #print("Colonne supprimée", column_name)
            df = df.drop(columns=column_name)



    taille = df.shape[1]
    taille

    result_all_x = []
    result_all_y = []

    for index_game, _ in df.iterrows():
        result_all_x.append(DATAFRAME["Temps numérique"][index_game])
        result_all_y.append(df.iloc[index_game])

    df_x = pd.DataFrame.from_records(result_all_x)
    df_y = pd.DataFrame.from_records(result_all_y)

    mean_row_x = pd.DataFrame([df_x.mean()], columns=df_x.columns)
    mean_row_y = pd.DataFrame([df_y.mean()], columns=df_y.columns)

    df_with_mean_x = pd.concat([df_x, mean_row_x], ignore_index=True)
    df_with_mean_y = pd.concat([df_y, mean_row_y], ignore_index=True)

    axe.plot(df_with_mean_x.iloc[-1][:taille], df_with_mean_y.iloc[-1][:taille], marker='o', linestyle='--', label=label, color=color)























def moyenne(DATAFRAME, ligne, label = "moyenne victoire", color = "green"):
    result_all = []

    for index_game, _ in DATAFRAME.iterrows():
        result_all.append(DATAFRAME[ligne][index_game])

    df = pd.DataFrame.from_records(result_all)

    mean_row = pd.DataFrame([df.mean()], columns=df.columns)

    df_with_mean = pd.concat([df, mean_row], ignore_index=True)

    try:
        plt.plot(df_with_mean.iloc[-1], ['Botte','1er item','2nd item','3ème item','4ème item','5ème item','6ème item'], marker='o', linestyle='--', label = label, color = color)
    except:
        plt.plot(df_with_mean.iloc[-1], ['Botte','1er item','2nd item','3ème item','4ème item','5ème item'], marker='o', linestyle='--', label = label, color = color)





def zone(victoire, ligne, label='Zone de victoire', color='green'):
    
    max_length = max(len(lst) for lst in victoire[ligne])
    max_per_column = [max(lst[i] for lst in victoire[ligne] if i < len(lst)) for i in range(max_length)]

    max_length = max(len(lst) for lst in victoire[ligne])
    min_per_column = [min(lst[i] for lst in victoire[ligne] if i < len(lst)) for i in range(max_length)]

    espace = np.arange(0, 32.5, 2.5)

    # Remplir les zones entre les courbes 
    plt.fill_between(espace, min_per_column, max_per_column,color=color, alpha=0.1,label=label)



















