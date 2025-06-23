from sklearn import svm
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle
x_train = pd.read_csv('pathlocation of csv', header=None).values
y_train = pd.read_csv('id_of_it  csv', header=None).values.ravel()
third_para = svm.SVC(kernel='linear',C=20.0,gamma=0.00001)
third_para.fit(x_train, y_train)
