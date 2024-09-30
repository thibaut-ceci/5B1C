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



############



def remove_column_with_one_value(DATAFRAME, ligne):

    ## Initialisation de plusieurs listes vides pour stocker les données des différentes colonnes du DATAFRAME
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

    ## Boucle sur les données de la ligne spécifiée du DATAFRAME
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
            continue

    ## Détermination de la longueur maximale parmi toutes les listes
    max_length = max(len(colonne0), len(colonne230), len(colonne5), len(colonne730),
                    len(colonne10), len(colonne123), len(colonne15), len(colonne173),
                    len(colonne20), len(colonne223), len(colonne25), len(colonne273),
                    len(colonne30))

    ## Compléter les listes avec des NaN jusqu'à la longueur maximale
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

    ## Créer un nouveau dataframe à partir des listes précédentes
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

    df = pd.DataFrame(data)

    ## Supprimer les colonnes contenant une seule valeur unique ou plus de NaN que de valeurs non-NaN
    for column_name, _ in df.items():
        if column_name == "Colonne 0" or column_name == "Colonne 230" or column_name == "Colonne 5" or column_name == "Colonne 730" or column_name == "Colonne 10" or column_name == "Colonne 123" or column_name == "Colonne 15":
            continue

        nb_nan = df[column_name].isna().sum() ## Compter le nombre de NaN dans une colonne
        nb_true_or_num = df[column_name].notna().sum() - df[column_name].isin([False]).sum() ## Compter le nombre de valeur non NaN dans la colonne

        if df[column_name].nunique() == 1 or nb_nan > nb_true_or_num:
            print("Colonne supprimée", column_name)
            df = df.drop(columns=column_name)

    return df









































def plot_colonnes(df1, df2, colonneX, colonneY, ylabel, title, plot_games = True, plot_zones = True):
    plt.figure(figsize=(10, 6), dpi=150)

    ## Boucle sur toutes le dataframe pour les victoires
    if plot_games == True:
        for index_game, _ in df1.iterrows():
            plt.plot(df1[colonneX][index_game], df1[colonneY][index_game], marker='o', label="Game de " + str(df1["Nom du joueur"][index_game]), color="green")

        # Boucle sur toutes le dataframe pour les défaites
        for index_game, _ in df2.iterrows():
            plt.plot(df2[colonneX][index_game], df2[colonneY][index_game], marker='o', label="Game de " + str(df2["Nom du joueur"][index_game]), color="red")

    try:
        df_with_mean_y_vict = moyennes(df1, plt, colonneY, label="Moyenne victoire", color="green")
        df_with_mean_y_defa = moyennes(df2, plt, colonneY, label="Moyenne défaite", color="red")
    except TypeError:
        moyenne(df1, colonneX, label = "moyenne victoire", color = "green")
        moyenne(df2, colonneX, label = "moyenne defaite", color = "red")
    
    if plot_zones == True:
        try:    
            zone(df1, colonneY, label='Zone de victoire', color='green')
            zone(df2, colonneY, label='Zone de défaite', color='red')
        except (TypeError, ValueError):
            print("Impossible d'afficher les zones !!")

    plt.title(title)
    plt.xlabel('Temps (minutes)')
    plt.ylabel(ylabel)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid()

    plt.tight_layout()
    plt.show()

    # return df_with_mean_y_defa





def moyennes(DATAFRAME, axe, ligne, label = "moyenne victoire", color = "green"):

    df = remove_column_with_one_value(DATAFRAME, ligne)

    taille = df.shape[1]

    result_all_y = []

    for index_game, _ in df.iterrows():
        result_all_y.append(df.iloc[index_game])

    df_y = pd.DataFrame.from_records(result_all_y)
    mean_row_y = pd.DataFrame([df_y.mean()], columns=df_y.columns)
    df_with_mean_y = pd.concat([df_y, mean_row_y], ignore_index=True)

    espace = np.arange(0, 32.5, 2.5)
    
    axe.plot(espace[:taille], df_with_mean_y.iloc[-1][:taille], marker='o', linestyle='--', label=label, color=color)

    return df_with_mean_y





















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

    victoire = remove_column_with_one_value(victoire, ligne)
    
    # Calcul des valeurs maximum et minimum par colonne (ignorer NaN)
    max_per_column = victoire.max(skipna=True).values
    min_per_column = victoire.min(skipna=True).values

    # Espace sur l'axe x (génération d'un espace équidistant en fonction du nombre de colonnes)
    espace = np.arange(0, len(max_per_column) * 2.5, 2.5)

    # Remplir les zones entre les courbes
    plt.fill_between(espace, min_per_column, max_per_column, color='lightblue', alpha=0.6, label='Zone de victoire')



















