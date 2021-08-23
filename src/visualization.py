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
                
                
                
def plot_Lift_curve(y_val, y_pred, step=0.01):
    
    #Define an auxiliar dataframe to plot the curve
    aux_lift = pd.DataFrame()
    #Create a real and predicted column for our new DataFrame and assign values
    aux_lift['real'] = y_val
    aux_lift['predicted'] = y_pred
    #Order the values for the predicted probability column:
    aux_lift.sort_values('predicted',ascending=False,inplace=True)
    
    #Create the values that will go into the X axis of our plot
    x_val = np.arange(step,1+step,step)
    #Calculate the ratio of ones in our data
    ratio_ones = aux_lift['real'].sum() / len(aux_lift)
    #Create an empty vector with the values that will go on the Y axis our our plot
    y_v = []
    
    #Calculate for each x value its correspondent y value
    for x in x_val:
        num_data = int(np.ceil(x*len(aux_lift))) #The ceil function returns the closest integer bigger than our number 
        data_here = aux_lift.iloc[:num_data,:]   # ie. np.ceil(1.4) = 2
        ratio_ones_here = data_here['real'].sum()/len(data_here)
        y_v.append(ratio_ones_here / ratio_ones)
           
   #Plot the figure
    fig, axis = plt.subplots()
    fig.figsize = (40,40)
    axis.plot(x_val, y_v, 'g-', linewidth = 3, markersize = 5)
    axis.plot(x_val, np.ones(len(x_val)), 'k-')
    axis.set_xlabel('Proportion of sample')
    axis.set_ylabel('Lift')
    plt.title('Lift Curve')
    plt.show()