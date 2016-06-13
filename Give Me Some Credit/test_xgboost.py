import pandas as pd
import matplotlib.pyplot as plt
import plot_roc
import xgboost as xgb
import numpy


raw_data = pd.read_csv('cs-training_pre.csv') 
raw_data.eval("RUUL = log(RUUL+0.00001)")  # +4%

#raw_data = raw_data.dropna(how='any')

#print raw_data

#divide data



#training model
divide = raw_data.shape[0]*2/3
dtrain =xgb.DMatrix(raw_data.values[:divide,1:],label=raw_data.values[:divide,0])
dtest = xgb.DMatrix(raw_data.values[divide:,1:],label=raw_data.values[divide:,0])
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' ,'eval_metric':'auc','colsample_bytree':0.3,'lambda':50,'gamma':0.9}

num_round = 200
bst = xgb.train(param, dtrain, num_round)
# make prediction
preds = bst.predict(dtest)





error = preds - raw_data.values[divide:,0]
print 'accuracy',sum(abs(error))/len(error)

plot_roc.plot_roc(raw_data.values[divide:,0], preds)

##########################################33

dtrain =xgb.DMatrix(raw_data.values[:,1:],label=raw_data.values[:,0])
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:GBM' }
num_round = 12
bst = xgb.train(param, dtrain, num_round)

test_data = pd.read_csv('cs-test_pre.csv') 
dtest = xgb.DMatrix(test_data.values[:,1:])
preds = bst.predictiont(dtest)
df = pd.DataFrame({'id':range(1,len(preds)+1),'probability':preds})

df.to_csv('preds.csv')








#raw_data.to_csv('cs-training_post.csv')
#processed_data = preprocessing.robust_scale(raw_data, axis=0, with_centering=True, with_scaling=True, copy=True)
#numpy.savetxt('cs-training_post.csv', processed_data, delimiter = ',')