import pandas as pd
from sklearn import preprocessing,linear_model,tree,neighbors
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import plot_roc



raw_data = pd.read_csv('cs-training_pre.csv') 
#print raw_data

# preprocess
raw_data = raw_data.dropna(how='any')
raw_data.eval("RUUL = log(RUUL+0.00001)")  # +4%
#raw_data.eval('DR = log(DR+0.00001)')
#raw_data.eval('MI= log(MI+0.01)')

#dummies = pd.get_dummies(raw_data['ND'])
#raw_data = raw_data.join(dummies)
#raw_data.drop('ND',1,inplace=True)

#visualization
#n, bins, patches = plt.hist(raw_data.values, 30, normed=1, facecolor='green', alpha=0.5)
#plt.show()

#divide data
divide = raw_data.shape[0]*2/3
train_data = raw_data.values[:divide,:]
test_data = raw_data.values[divide:,:]


#training model

#logistic regression
clf = linear_model.LinearRegression()
clf.fit (train_data[:,1:], train_data[:,0])


#decision tree
#clf = tree.DecisionTreeClassifier()
#clf.fit (train_data[:,1:], train_data[:,0])

#nearist neighbor
#n_neighbors = 15  
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights=distance)

predict = clf.predict(test_data[:,1:])>0.5 
error = predict - test_data[:,0]
print 'accuracy',sum(abs(error))/len(error)
plot_roc.plot_roc(test_data[:,0], clf.predict(test_data[:,1:]))















#raw_data.to_csv('cs-training_post.csv')
#processed_data = preprocessing.robust_scale(raw_data, axis=0, with_centering=True, with_scaling=True, copy=True)
#numpy.savetxt('cs-training_post.csv', processed_data, delimiter = ',')