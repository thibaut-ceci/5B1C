def display_params_for_catalog(pd):
    # Display all columns and rows of the DataFrame. For use it, just import pandas as pd and call this function.
    pd.set_option("display.max_rows",None)
    pd.set_option("display.max_columns",None)
    pd.set_option("display.width",None)
    pd.set_option("display.max_colwidth",None)