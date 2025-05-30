import numpy as np
X_seen= np.load('X_seen.npy', encoding='bytes', allow_pickle=True)
#(40 x N_i x D): 40 feature matrices. X_seen[i] is the N_i x D feature matrix of seen class i
Xtest=  np.load('Xtest.npy' , encoding='bytes', allow_pickle=True)
# #(6180, 4096): feature matrix of the test data.
Ytest=np.load('Ytest.npy' , encoding='bytes', allow_pickle=True)
# #(6180, 1): ground truth labels of the test data
class_attributes_seen=np.load('class_attributes_seen.npy', encoding='bytes', allow_pickle=True)
# #(40, 85): 40x85 matrix with each row being the 85-dimensional class attribute vector of a seen class.
class_attributes_unseen=np.load('class_attributes_unseen.npy', encoding='bytes', allow_pickle=True)
# #(10, 85): 10x85 matrix with each row being the 85-dimensional class attribute vector of an  unseen class.

def mean_seen_classes(df):
  #Gives mean of seen classes
  mean= np.zeros((df.shape[0],df[0].shape[1]))
  for i in range(0,df.shape[0]):
    mean[i] = np.mean(df[i],axis=0).reshape(1,df[0].shape[1])
  return mean

def mean_unseen_classes2(at_seen,mean,at_unseen, l):
  # gives mean of unseen classes via closed form solution of linear model
  W= np.dot(at_seen.T,at_seen) + l*np.identity(at_seen.shape[1])
  W= np.linalg.inv(W)
  W1= np.dot(at_seen.T,mean)
  Wf= np.dot(W,W1)

  unseen_mean= np.dot(at_unseen,Wf)
  return unseen_mean

def predict(unseen_mean,x_test,y_test):
  #create distance matrix for (data points x mean classes)
  distances= np.zeros((x_test.shape[0],unseen_mean.shape[0]))
  for i in range(unseen_mean.shape[0]):
    # calculate squared mahalnobis distance
    dist= x_test-unseen_mean[i]
    dist2= np.square(dist)
    distances[:,i]= np.sum(dist2,axis=1).reshape(dist2.shape[0])

  # getting which class is nearest
  y_pred= np.argmin(distances,axis=1)
  y_pred= y_pred.reshape(y_pred.shape[0],1)

  correct=0
  #calculating correct predictions
  for i in range(y_test.shape[0]):
    if y_test[i] == y_pred[i]+1 :
      correct+=1

  accuracy= correct/float(y_test.shape[0])
  #returns accuracy
  return accuracy

mean= mean_seen_classes(X_seen)
lam_val= np.array( [0.01, 0.1, 1, 10, 20, 50, 100])
for l in lam_val:
  unseen_mean= mean_unseen_classes2(class_attributes_seen,mean,class_attributes_unseen,l)
  accuracy= predict(unseen_mean,Xtest,Ytest)
  print(100*accuracy)

