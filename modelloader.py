from tensorflow import keras
import pandas as pd
from scipy.io.wavfile import read
def process_file(filename):
    arr = []
    model = keras.models.load_model('.')
    print(filename)
    data, rs = read(filename)
    file = open("input dimension for model.txt", "r")
    suitable_length_for_model = int(file.read())
    file.close()
    rs = rs.astype(float)
    rs = rs[0:suitable_length_for_model+1]
    a = pd.Series(rs)
    arr.append(a)
    df = pd.DataFrame(arr)
    X2 = df.iloc[0:, 1:]
    #print(X2)
    predictions = model.predict(X2)
    rounded = [round(x[0]) for x in predictions]

    #print("predicted value is" + str(rounded))
    if str(rounded)=='[1.0]':
        return True
    else:
        return False
# print(process_file("/home/themockingjester/PycharmProjects/multilayer_perceptron_modal_for_project_Human_Screem_Detection/venv/positive/damm_6.wav"))
#model = keras.models.load_model('.')
#print('hi')
#df = pd.read_csv('newresources.csv', index_col=0, engine = 'c')



#row_num_for_verification_of_model = 154
#X2 = df.iloc[row_num_for_verification_of_model:row_num_for_verification_of_model+1,1:]
#X2 = df.iloc[row_num_for_verification_of_model:,1:]
#predictions = model.predict(X2)

# round predictions
#rounded = [round(x[0]) for x in predictions]

#print("predicted value is"+str(rounded))
#print("actual value was"+str(list(df.iloc[row_num_for_verification_of_model:,0])))















# This code appears to define a function named `process_file` which is responsible for processing a sound file and making a prediction using a pre-trained Keras model for sound classification.

# Here's a breakdown of what the code is doing:

# 1. **Loading the Model**: The code loads a pre-trained Keras model using `keras.models.load_model('.')`. The model is assumed to be stored in the current directory with the filename `'model.h5'`.

# 2. **Reading the Sound File**: The function takes a filename as input. It uses `scipy.io.wavfile.read` to read the sound file.

# 3. **Data Processing**:
#    - It reads the length of the input expected by the model from a text file named `'input dimension for model.txt'`.
#    - It truncates or pads the sound data to match the expected input length of the model.
#    - The processed data is converted into a Pandas DataFrame.

# 4. **Making Predictions**:
#    - It extracts the features (sound data) from the DataFrame.
#    - It uses the pre-trained model to make predictions on the sound data.
#    - The predictions are rounded to obtain binary values (0 or 1).
   
# 5. **Returning Prediction**:
#    - If the rounded prediction is `[1.0]`, it returns `True`, indicating that the sound is predicted to be positive.
#    - If the rounded prediction is not `[1.0]`, it returns `False`, indicating that the sound is predicted to be negative.

# Overall, this code defines a function to process a sound file, make predictions using a pre-trained model, and return a boolean value indicating whether the sound is classified as positive or negative based on the model's prediction.