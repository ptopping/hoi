index : The unique ID of each observation.
class : The true class of each observation. The classes are binary (0 or 1).
predicted_prob : The model's estimate of probability that the observation belongs to class 1.
Instructions
Using the model_outcome.csv, develop either an R or Python script to:

Manually calculate the sensitivity and specificity of the model, using a predicted_prob threshold of greater than or equal to .5.
Manually calculate the Area Under the Receiver Operating Characteristic Curve.
Visualize the Receiver Operating Characterstic Curve.
Email your finalized, completely reproducible .r or .py script to L.A. Care's Talent Acquisition Specialist, Jamessa Jones, at jjones@lacare.org.

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/screening-lacare/data_scientist_screening/blob/master/model_outcome.csv'
model = pd.read_html(url)[0]

model = model.set_index('index').drop('Unnamed: 0',axis=1)

def sensitivity(df,threshold):
    df.loc[(df['class']==True) & (df['predicted_prob']>=threshold),'TP'] = 1
    df.loc[(df['class']==True) & (df['predicted_prob']<threshold),'FN'] = 1
    return df['TP'].sum() / (df['TP'].sum() + df['FN'].sum())

def specificity(df,threshold):
    df.loc[(model['class']==False) & (df['predicted_prob']<threshold),'TN'] = 1
    df.loc[(model['class']==False) & (df['predicted_prob']>=threshold),'FP'] = 1
    return df['TN'].sum() / (df['TN'].sum() + df['FP'].sum())
  
