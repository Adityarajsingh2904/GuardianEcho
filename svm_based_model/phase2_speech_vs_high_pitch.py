from sklearn import svm
import pandas as pd
from sklearn.metrics import accuracy_score
x_train = pd.read_csv('speech.csv', header=None).values
y_train = pd.read_csv('id_of_it.csv', header=None).values.ravel()
second_para = svm.SVC(C=20.0,gamma=0.00001)
second_para.fit(x_train, y_train)
