import datetime
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns


def create_dfs(london_url, athens_url):
    london=pd.read_csv(london_url, index_col="listing_id")
    athens=pd.read_csv(athens_url, index_col="listing_id")
    london['city']='London'
    athens['city']='Athens'

    df_all=pd.concat([london, athens], axis=0)

    df_all['date'] =  pd.to_datetime(df_all['date'], infer_datetime_format=True)
    df_all['year'] = pd.DatetimeIndex(df_all['date']).year
    df_all=df_all.sort_values('year',ascending=False)
    return df_all


def plot_data(df):
    sns.histplot(data=df, x="year", hue='city',multiple="dodge", shrink=.8, discrete=True)
    # df['year'].value_counts().plot(kind='bar',title='Count of Reviews by Year')
    # plt.legend(['Athens', 'London'])
    plt.show()



if __name__ == "__main__":
    df = create_dfs('http://data.insideairbnb.com/united-kingdom/england/london/2022-09-10/visualisations/reviews.csv',
    'http://data.insideairbnb.com/greece/attica/athens/2022-09-20/visualisations/reviews.csv')
    print(df)
    plot_data(df) 