import ast

import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import warnings


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


def repair_df(df1, df2, list_columns):
    """
    Répare les colonnes spécifiées dans deux dataframes en les convertissant en liste.
    
    Entrée :
    --------
    df1 : pandas.DataFrame
        Premier dataframe à traiter.
    df2 : pandas.DataFrame
        Deuxième dataframe à traiter.
    list_columns : list
        Liste des colonnes à traiter.
    
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
            # print("Colonne supprimée", column_name)
            df = df.drop(columns=column_name)

    return df


def cs_min(df_with_mean_y_vict_4):


    ## Supprimer des avertissements
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=RuntimeWarning)


    time = np.arange(0, 25, 2.5)

    all_cs_min = []

    for i, _ in enumerate(df_with_mean_y_vict_4.iloc[-1]):
        cs_min = df_with_mean_y_vict_4.iloc[-1][i]/time[i]
        # print(cs_min)
        all_cs_min.append(cs_min)

    return np.nanmean(all_cs_min)









def plot_colonnes(df1, df2, colonneX, colonneY, ylabel, title, remove_column_with_one_value_bool, plot_games = True, plot_zones = True, plot_xlim = False):








    plt.figure(figsize=(10, 6), dpi=150)

    ## Affiche les parties
    if plot_games == True:
        ## Boucle sur tous le dataframe pour les victoires
        for index_game, _ in df1.iterrows():
            plt.plot(df1[colonneX][index_game], df1[colonneY][index_game], marker='o', label="Game de " + str(df1["Nom du joueur"][index_game]), color="green")

        ## Boucle sur tous le dataframe pour les défaites
        for index_game, _ in df2.iterrows():
            plt.plot(df2[colonneX][index_game], df2[colonneY][index_game], marker='o', label="Game de " + str(df2["Nom du joueur"][index_game]), color="red")

    ## Affiche les moyennes
    try:
        df_with_mean_y_vict = moyennes(df1, plt, colonneY, label="Moyenne victoire", color="green")
        df_with_mean_y_defa = moyennes(df2, plt, colonneY, label="Moyenne défaite", color="red")
    
    ## Utiliser l'autre code pour afficher les temps d'obtention des objets au cours des parties
    except TypeError:
        df_with_mean_y_vict_4 = moyenne(df1, colonneX, label = "Moyenne victoire", color = "green")
        df_with_mean_y_defa_4 = moyenne(df2, colonneX, label = "Moyenne defaite", color = "red")
    
    ## Afficher les zones au lieu des parties
    if plot_zones == True:
        try:    
            _, _ = zone(df1, colonneY, label='Zone de victoire', color='green', remove_column_with_one_value_bool = remove_column_with_one_value_bool)
            _, _ = zone(df2, colonneY, label='Zone de défaite', color='red', remove_column_with_one_value_bool = remove_column_with_one_value_bool)
    
        except (TypeError, ValueError):
            _, _ = zone(df1, colonneX, label='Zone de victoire', color='green', remove_column_with_one_value_bool = remove_column_with_one_value_bool)
            _, _ = zone(df2, colonneX, label='Zone de défaite', color='red', remove_column_with_one_value_bool = remove_column_with_one_value_bool)


    plt.title(title)
    plt.xlabel('Temps (minutes)')
    plt.ylabel(ylabel)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid()
    if plot_xlim == True:
        plt.xlim(0, 25)

    plt.tight_layout()
    plt.show()

    try:
        return df_with_mean_y_vict_4, df_with_mean_y_defa_4
    except UnboundLocalError:
        # print("error")
        return df_with_mean_y_vict, df_with_mean_y_defa





def moyennes(DATAFRAME, axe, ligne, label = "Moyenne victoire", color = "green"):

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





















def moyenne(DATAFRAME, ligne, label = "Moyenne victoire", color = "green"):
    
    
    
    result_all = []

    for index_game, _ in DATAFRAME.iterrows():
        result_all.append(DATAFRAME[ligne][index_game])

    df = pd.DataFrame.from_records(result_all)

    mean_row = pd.DataFrame([df.mean()], columns=df.columns)

    df_with_mean = pd.concat([df, mean_row], ignore_index=True)

    try:
        plt.plot(df_with_mean.iloc[-1], ['Botte','1er objet','2nd objet','3ème objet','4ème objet','5ème objet','6ème objet'], marker='o', linestyle='--', label = label, color = color)
    except:
        plt.plot(df_with_mean.iloc[-1], ['Botte','1er objet','2nd objet','3ème objet','4ème objet','5ème objet'], marker='o', linestyle='--', label = label, color = color)

    return df_with_mean



def zone(victoire, ligne, remove_column_with_one_value_bool, label='Zone de victoire', color='green'):
    """
    Trace une zone transparente et colorée entre les valeurs minimum et maximum de chaque colonne dans un dataframe.

    Entrée:
    -------
    victoire : pandas.DataFrame
        Dataframe contenant les données à analyser.
    ligne : int
        Ligne du dataframe à utiliser pour filtrer les colonnes avec des valeurs uniques.
    label : str
        Légende pour la zone ombrée.
    color : str
        Couleur de la zone.
    
    Sortie:
    -------
    max_per_column : list
        Contient les valeurs maximales pour chaque colonne.
    min_per_column : list
        Contient les valeurs minimales pour chaque colonne.
    """

    ## Supprimer les colonnes ne contenant qu'une seule valeur
    
    # print(victoire)
    if remove_column_with_one_value_bool == False:
        max_values = [np.nanmax(column) for column in itertools.zip_longest(*victoire["Temps numérique objets"], fillvalue=np.nan)]
        min_values = [np.nanmin(column) for column in itertools.zip_longest(*victoire["Temps numérique objets"], fillvalue=np.nan)]
        
        ## Espace sur l'axe x ou définir la zone
        espace = np.arange(0, len(max_values), 1)

        ## Création de la zone
        plt.fill_betweenx(espace, min_values, max_values, color=color, alpha=0.2, label=label)

        return max_values, min_values


    else:
        victoire = remove_column_with_one_value(victoire, ligne)
        
        # print(victoire)
        ## Calculer les valeurs maximum et minimum par colonne

        max_par_colonne = victoire.max(skipna=True).values
        min_par_colonne = victoire.min(skipna=True).values
        
        ## Espace sur l'axe x ou définir la zone
        espace = np.arange(0, len(max_par_colonne) * 2.5, 2.5)

        ## Création de la zone
        plt.fill_between(espace, max_par_colonne, min_par_colonne, color=color, alpha=0.2, label=label)

        return max_par_colonne, min_par_colonne

        

 