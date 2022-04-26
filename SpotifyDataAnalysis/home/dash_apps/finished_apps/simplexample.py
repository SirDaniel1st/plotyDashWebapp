import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Top100(filePath):
    # read csv data for each country into associated dataframe
    argentina = pd.read_csv(filePath)
    # drop unnamed column from each dataframe
    argentina = argentina.drop(columns=['Unnamed: 0'])
    argentina['date'] = pd.to_datetime(argentina['date'], format='%Y-%m-%d')
    argentina['year'] = pd.DatetimeIndex(argentina['date']).year
    
    ## Seasonality in Argentina based on Top 200 and Viral 50 charts respectively
    argentina_top200 = argentina[argentina['chart'] == 'top200']
    
    ### Argentina Top 200 Charts
    danceability200 = argentina_top200[['date', 'danceability']]
    danceability200.set_index('date', inplace=True)
    danceability200 = danceability200.dropna()
    danceability200_mean = danceability200.groupby('date').mean()
    
    energy200 = argentina_top200[['date', 'energy']]
    energy200.set_index('date', inplace=True)
    energy200 = energy200.dropna()
    energy200_mean = energy200.groupby('date').mean()


    key200 = argentina_top200[['date', 'key']]
    key200.set_index('date', inplace=True)
    key200 = key200.dropna()
    key200_mean = key200.groupby('date').mean()


    loud200 = argentina_top200[['date', 'loudness']]
    loud200.set_index('date', inplace=True)
    loud200 = loud200.dropna()
    loud200_mean = loud200.groupby('date').mean()

    mode200 = argentina_top200[['date', 'mode']]
    mode200.set_index('date', inplace=True)
    mode200 = mode200.dropna()
    mode200_mean = mode200.groupby('date').mean()


    speech200 = argentina_top200[['date', 'speechiness']]
    speech200.set_index('date', inplace=True)
    speech200 = speech200.dropna()
    speech200_mean = speech200.groupby('date').mean()

    acou200 = argentina_top200[['date', 'acousticness']]
    acou200.set_index('date', inplace=True)
    acou200 = acou200.dropna()
    acou200_mean = acou200.groupby('date').mean()

    instr200 = argentina_top200[['date', 'instrumentalness']]
    instr200.set_index('date', inplace=True)
    instr200 = instr200.dropna()
    instr200_mean = instr200.groupby('date').mean()

    live200 = argentina_top200[['date', 'liveness']]
    live200.set_index('date', inplace=True)
    live200 = live200.dropna()
    live200_mean = live200.groupby('date').mean()

    valence200 = argentina_top200[['date', 'valence']]
    valence200.set_index('date', inplace=True)
    valence200 = valence200.dropna()
    valence200_mean = valence200.groupby('date').mean()

    tempo200 = argentina_top200[['date', 'tempo']]
    tempo200.set_index('date', inplace=True)
    tempo200 = tempo200.dropna()
    tempo200_mean = tempo200.groupby('date').mean()

    duration200 = argentina_top200[['date', 'duration_ms']]
    duration200.set_index('date', inplace=True)
    duration200 = duration200.dropna()
    duration200_mean = duration200.groupby('date').mean()


    x_vals=[danceability200_mean.index, energy200_mean.index,key200_mean.index,loud200_mean.index, mode200_mean.index,speech200_mean.index,acou200_mean.index,instr200_mean.index,live200_mean.index,valence200_mean.index,tempo200_mean.index,duration200_mean.index]
    y_vals=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']
    return x_vals, y_vals, argentina_top200

def top50(filepath):
    # read csv data for each country into associated dataframe
    argentina = pd.read_csv(filePath)

    # drop unnamed column from each dataframe
    argentina = argentina.drop(columns=['Unnamed: 0'])
    argentina['date'] = pd.to_datetime(argentina['date'], format='%Y-%m-%d')
    argentina['year'] = pd.DatetimeIndex(argentina['date']).year
    argentina_viral50 = argentina[argentina['chart'] == 'viral50']

    danceability50 = argentina_viral50[['date', 'danceability']]
    danceability50.set_index('date', inplace=True)
    danceability50 = danceability50.dropna()
    danceability50_mean = danceability50.groupby('date').mean()

    energy50 = argentina_viral50[['date', 'energy']]
    energy50.set_index('date', inplace=True)
    energy50 = energy50.dropna()
    energy50_mean = energy50.groupby('date').mean()
    
    key50 = argentina_viral50[['date', 'key']]
    key50.set_index('date', inplace=True)
    key50 = key50.dropna()
    key50_mean = key50.groupby('date').mean()

    loud50 = argentina_viral50[['date', 'loudness']]
    loud50.set_index('date', inplace=True)
    loud50 = loud50.dropna()
    loud50_mean = loud50.groupby('date').mean()

    mode50 = argentina_viral50[['date', 'mode']]
    mode50.set_index('date', inplace=True)
    mode50 = mode50.dropna() 
    mode50_mean = mode50.groupby('date').mean()   

    speech50 = argentina_viral50[['date', 'speechiness']]
    speech50.set_index('date', inplace=True)
    speech50 = speech50.dropna()
    speech50_mean = speech50.groupby('date').mean()

    acou50 = argentina_viral50[['date', 'acousticness']]
    acou50.set_index('date', inplace=True)
    acou50 = acou50.dropna()
    acou50_mean = acou50.groupby('date').mean()

    instr50 = argentina_viral50[['date', 'instrumentalness']]
    instr50.set_index('date', inplace=True)
    instr50 = instr50.dropna()
    instr50_mean = instr50.groupby('date').mean()

    live50 = argentina_viral50[['date', 'liveness']]
    live50.set_index('date', inplace=True)
    live50 = live50.dropna()
    live50_mean = live50.groupby('date').mean()

    valence50 = argentina_viral50[['date', 'valence']]
    valence50.set_index('date', inplace=True)
    valence50 = valence50.dropna()
    valence50_mean = valence50.groupby('date').mean()

    tempo50 = argentina_viral50[['date', 'tempo']]
    tempo50.set_index('date', inplace=True)
    tempo50 = tempo50.dropna()
    tempo50_mean = tempo50.groupby('date').mean()

    duration50 = argentina_viral50[['date', 'duration_ms']]
    duration50.set_index('date', inplace=True)
    duration50 = duration50.dropna()
    duration50_mean = duration50.groupby('date').mean()

    x_vals=[danceability50_mean.index, energy50_mean.index,key50_mean.index,loud50_mean.index, mode50_mean.index,speech50_mean.index,acou50_mean.index,instr50_mean.index,live50_mean.index,valence50_mean.index,tempo50_mean.index,duration50_mean.index]
    y_vals=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']
    return x_vals, y_vals, argentina_viral50












