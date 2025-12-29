import numpy as np
import pandas as pd

def clean_data(df, dropna=True):
    """
    Merges date and time into a single datetime column and removes the original date and time columns.
    changes other columns to numeric.
    deletes NaN values, optional 
    """
    
    df_ = df.copy()
    
    df_.insert(loc = 0, column = "Datetime", 
                value = pd.to_datetime(df["Date"] + ' ' + df["Time"],
                format='%d/%m/%Y %H:%M:%S') )
    
    df_ = df_.drop(columns=["Date", "Time"])
    
    print(df_.head())
    for col in df_.columns:
        if col != "Datetime":
            df_[col] = pd.to_numeric(df_[col], errors='coerce')
            
    if dropna==True:
        return df_.dropna()
    else:   
        return df_   
    