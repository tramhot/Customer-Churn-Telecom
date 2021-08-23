import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_bar_chart(x_feature, y_feature, dataset):
    #Plot sales per country
    plt.figure(figsize=(8,8))
    ax = sns.barplot(x=x_feature, y=y_feature, data=dataset)
    plt.xticks(rotation='vertical')
    ax.grid(b=True, which='major', color='#d3d3d3', linewidth=1.0)
    ax.grid(b=True, which='minor', color='#d3d3d3', linewidth=0.5)
    plt.show()
    
    
def plot_dist(feature):
    df = train.copy()
    plt.subplots(figsize=(8,8))
    try:
        sns.distplot( df.loc[df.churn=='no', feature] , color="dodgerblue", label="Stay")
    except RuntimeError as re:
        if str(re).startswith("RuntimeError: Selected KDE bandwidth is 0. Cannot estiamte density."):
            sns.distplot(df.loc[df.churn=='no', feature] , color="dodgerblue", label="Stay", kde_kws={'bw': 0.1})
        else:
            raise re
            
    try:
        sns.distplot( df.loc[df.churn=='yes', feature] , color="orange", label="Go")
    except RuntimeError as re:
        if str(re).startswith("RuntimeError: Selected KDE bandwidth is 0. Cannot estiamte density."):
            sns.distplot(df.loc[df.churn=='yes', feature] , color="orange", label="Go", kde_kws={'bw': 0.1})
        else:
            raise re


    plt.title(f'{feature} Histogram')
    plt.legend()
    
    
def plot_boxplot(serie):
    plt.figure(figsize=(8, 8))
    sns.boxplot(y=serie)
    plt.show()
    
    
def plot_multi_boxplot(serie_1, serie_2, dataframe, order = None, figsize = (8,8)):
    plt.figure(figsize=figsize, )
    ax = sns.boxplot(x = serie_1, y = serie_2, data = dataframe, order = order)
    plt.setp(ax.get_xticklabels(), rotation=90)
    plt.show()

def box_plot_numeric(df, columns, gridspec_kw={'wspace':1},figsize=(12,8),target=None,**args):
    if not target:
        f, axes = plt.subplots(1,
                               columns 
                               ,gridspec_kw=gridspec_kw,figsize=figsize)
        for i,col in enumerate(columns):
            sns.boxplot(y=df[col],orient='v',ax=axes[i],**args)
    else:
        f, axes = plt.subplots(1,len(columns),gridspec_kw=gridspec_kw,figsize=figsize)
        for i,col in enumerate(columns):
            sns.boxplot(y=df[col],x=target,data=df ,orient='v',ax=axes[i],**args)
            
            
def histogram_and_density(df, columns,gridspec_kw={'hspace':0.2,'wspace':0.2},figsize=(8,14),target=None,**args):
    """ 
        figsize: figure size pass to matplotlib.pyplot subplots function
        **args: Additional arguments to pass to seaborn distribution plot function 
    """
    if not target:
        f, axes = plt.subplots(len(columns),gridspec_kw=gridspec_kw,figsize=figsize)
        for i,col in enumerate(columns):
            sns.distplot(a=df[col].dropna(),ax=axes[i],**args)
    else:
        unique = df[target].unique()
        f, axes = plt.subplots(len(columns),len(unique),gridspec_kw=gridspec_kw,figsize=figsize)
        for j, value in enumerate(unique):
            for i,col in enumerate(columns):
                sns.distplot(a=df[df[target] == value][col].dropna().rename(col+' with '+target+' = '+value),ax=axes[i,j],**args)