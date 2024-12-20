# this file is made for sound_classifier_nueral.py
# positive sound mean the sound that we want to predict
# negative sound mean sound except positive sound
import time
import psutil
import numpy as np
import pandas as pd
import os,threading
from scipy.io.wavfile import read
import os

class scream():

    def adder(self):
        ################################  getting negative sounds #################################################
        files = os.listdir('negative')
        arr = []
        for i in files:
            num = float(0)  # assigning labels to negative sounds
            i = 'negative/'+i
            try:
                data, rs = read(i)
                print(psutil.virtual_memory())
            except:
                print("removed "+i)
                os.remove(i)
                continue
            try:
                rs = rs.astype(float)
                rs = np.insert(rs,0,num)
                a = pd.Series(rs)
                arr.append(a)
                self.ctr+=1
            except:
                pass
        ########################################### end ###############################################

        ############################# getting positive sounds ######################################
        files = os.listdir('positive')
        for i in files:
            num = float(1)  # assigning labels to positive sounds
            i = 'positive/' + i
            try:
                data, rs = read(i)
                print(psutil.virtual_memory())
            except:
                print("removed "+i)
                os.remove(i)
                continue
            try:
                rs = rs.astype(float)
                rs = np.insert(rs, 0, num)
                a = pd.Series(rs)
                arr.append(a)
                self.ctr+=1
            except:
                pass

        self.starting_index_not_to_be_shuffled = self.ctr


        file = open("begining index of testing files.txt","w")
        file.write(str(self.ctr))
        file.close()


        print(str(self.ctr)+" have been added ")
        time.sleep(1)
        ########################################### end ##########################

        #################### loading testing sounds #########################
        files = os.listdir('testing')
        for i in files:
            if i.startswith("1"):
                num = float(1)
            else:
                num = float(0)

            i = 'testing/' + i
            try:
                data, rs = read(i)
                print(psutil.virtual_memory())
            except:
                print("removed "+i)
                os.remove(i)
                continue
            try:
                rs = rs.astype(float)
                rs = np.insert(rs, 0, num)
                a = pd.Series(rs)
                arr.append(a)
                self.ctr += 1
            except:
                pass
        print(psutil.virtual_memory())
        ############################### end ############################
        df = pd.DataFrame(arr)
        print(psutil.virtual_memory())
        df = df.dropna(axis=1)  ### removing columns containg null or NA
        df.to_csv('resources.csv')
    def __init__(self):
        self.ctr = 0
        self.starting_index_not_to_be_shuffled = 0
        self.adder()
        start_time = time.time()
        print('started')
        self.df = pd.read_csv('resources.csv', index_col=0, engine = 'c')
        print("without shuffling dataset contains "+str(len(self.df))+" rows and "+str(len(self.df.columns))+" columns")
        self.df.iloc[:self.starting_index_not_to_be_shuffled,:] = self.df.iloc[:self.starting_index_not_to_be_shuffled,:].sample(frac=1).reset_index(drop=True) # shuffling dataframe
        print("after shuffling dataset contains " + str(len(self.df)) + " rows and " + str(len(self.df.columns)) + " columns")
        self.df.to_csv('newresources.csv') # shuffled dataset
        print(self.df)

        file = open("input dimension for model.txt","w")
        file.write(str(len(self.df.columns)-1))
        file.close()

        print("\nwhole process takes %s seconds" % (time.time()-start_time))

scream()



















# The provided code appears to be creating a dataset for a sound classification task. Here's a breakdown of what the code is doing:

# 1. **Class Definition**: The code defines a class named `scream`.

# 2. **Initializer**: The `__init__` method of the class is called when an instance of the class is created. Inside this method:
#    - The `adder` method is called to populate the dataset.
#    - The dataset is loaded from a CSV file named 'resources.csv'.
#    - The dataset is shuffled to randomize the order of the data.
#    - The shuffled dataset is saved to a new CSV file named 'newresources.csv'.
#    - The input dimension for the model is written to a text file named 'input dimension for model.txt'.

# 3. **Data Population (adder method)**: The `adder` method does the following:
#    - It initializes variables for counting data points and starting index not to be shuffled.
#    - It reads sound files from directories named 'positive', 'negative', and 'testing'.
#    - For each sound file:
#      - If the file is labeled as positive (belongs to the 'positive' directory), a label of 1 is assigned; otherwise, a label of 0 is assigned.
#      - The sound file is read using `scipy.io.wavfile.read`.
#      - The data is inserted into a Pandas Series, where the first element is the label and the remaining elements are the sound data.
#      - The Pandas Series is appended to a list.
#    - The list of Pandas Series is converted to a DataFrame.
#    - Any columns containing null or NA values are dropped from the DataFrame.
#    - The DataFrame is saved to a CSV file named 'resources.csv'.

# 4. **Output**: The code prints information about the dataset, such as the number of rows and columns before and after shuffling.

# Overall, the code appears to be reading sound files from specified directories, labeling them, and then saving the data to a CSV file for further processing, likely for training a machine learning model for sound classification.