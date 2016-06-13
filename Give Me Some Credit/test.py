import pandas as pd
from sklearn import preprocessing,linear_model,tree,neighbors
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import plot_roc
import math


raw_data = pd.read_csv('cs-training_pre.csv')
#print raw_data.describe()
raw_data = raw_data.dropna(how='any')
print raw_data.columns


col = 'NREL'
raw_data = raw_data.sort(col)
print raw_data[col]
#raw_data.eval(col+' = log('+col+'+0.00001)')
#dummies = pd.get_dummies(raw_data[col])
#print dummies
#raw_data[col].plot(kind='bar')
print 'hello'
#raw_data['ND0'] = 1 if raw_data['ND']==0 else 0
#raw_data['ND0'] = 1 if 4>raw_data['ND']>0 else 0
n, bins, patches = plt.hist(raw_data[col], 20, normed=0, facecolor='green', alpha=0.5)
plt.show()