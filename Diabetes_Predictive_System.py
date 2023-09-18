# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open(r"C:\Users\subit\trainedModel.sav",'rb'))


# input_data = (1,85,66,29,0,26.6,0.351,31)
input_data = (6,148,72,35,0,33.6,0.627,50)
#traform list to numpy array
input_data_array = np.asarray(input_data)

# reshape the array
input_data_reshapped = input_data_array.reshape(1,-1)



prediction = loaded_model.predict(input_data_reshapped)
print(prediction)
if prediction[0] == 0:
    print('Person does not have diabetes')
else:
    print('Person have diabetes')


