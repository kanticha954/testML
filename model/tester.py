import pickle
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

classifier = joblib.load('model.pkl')
print("Enter the following details to make the predictions:- n")

with open('../model/set_scaler.pkl', 'rb') as file:
    # Call load method to deserialze
    sc = pickle.load(file)

resistance_thumb = float(input("Enter resistance_thumb:- "))
bend_thumb = int(input("Enter bend_thumb:- "))
resistance_index = float(input("Enter resistance_index:- "))
bend_index = int(input("Enter bend_index:- "))
resistance_mid = float(input("Enter resistance_mid:- "))
bend_mid = int(input("Enter bend_mid:- "))
resistance_ring = float(input("Enter resistance_ring:- "))
bend_ring = int(input("Enter bend_ring:- "))
resistance_little = float(input("Enter resistance_little:- "))
bend_little = int(input("Enter bend_little:- "))
x = int(input("Enter X :- "))
y = int(input("Enter Y :- "))
z = int(input("Enter Z :- "))

get_data = np.array([[resistance_thumb, bend_thumb, resistance_index,
                      bend_index, resistance_mid, bend_mid,
                      resistance_ring, bend_ring,
                      resistance_little, bend_little,
                      x, y, z]])

get_data = sc.transform(get_data)
get_data.reshape(-1, 1)

print(get_data)

result = classifier.predict(get_data)
print(result)


