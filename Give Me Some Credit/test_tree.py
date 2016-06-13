import pandas as pd
from sklearn import preprocessing,linear_model,tree,neighbors
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import plot_roc
from sklearn.ensemble import GradientBoostingClassifier


raw_data = pd.read_csv('C:\Users\sm\Desktop\Give Me Some Credit\cs-training_pre.csv') 
#print raw_data
# RevolvingUtilizationOfUnsecuredLines
#clf = cluster.KMeans(n_clusters=2)
#X=np.array(dd[['responsetime','t0']])
#cls = clf.fit_predict(X)
# preprocess
raw_data = raw_data.dropna(how='any')

#print raw_data.values[:,1:]

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
#clf = GradientBoostingClassifier(n_estimators=5, learning_rate=1,max_depth=1, random_state=0)
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
#numpy.savetxt('cs-training_post.csv', processed_data, delimiter = ',')import pandas as pd
