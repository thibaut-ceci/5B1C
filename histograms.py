import matplotlib.pyplot as plt
import pandas as pd


def open_catalog(avalanches, pos_number=0.260):
    ax = avalanches.count().sort_values().plot(kind="barh", figsize=(6, 10))

    ax.set_xlabel("Number of avalanches")
    ax.set_xlim(0, len(avalanches)+22)

    #For counting the number of values in each column
    for index, value in enumerate(avalanches.count().sort_values()):
        ax.text(value+0.1, index-pos_number, str(value))


def open_catalog_subtype(ESEC, pos_number):
    ESEC_subtype = ESEC["subtype"].value_counts().sort_values(ascending=False)

    plt.figure()
    ax = ESEC_subtype.plot(kind='barh')

    ax.set_xlabel("Number of avalanches")
    ax.set_ylabel("Subtype")
    plt.grid(False)
    ax.set_yticks(range(len(ESEC_subtype)))
    ax.set_yticklabels(ESEC_subtype.index)
    ax.set_xlim(0, ESEC_subtype.max()+16)

    #For counting the number of values in each column
    for index, value in enumerate(ESEC["subtype"].value_counts().sort_values(ascending=False)):
            ax.text(value+0.1, index-pos_number, str(value))