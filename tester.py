import joblib


classifier = joblib.load('model.h5')
print("Enter the following details to make the predictions:- n")


resistance_thumb = float(intput("Enter resistance_thumb:- "))
bend_thumb = int(intput("Enter bend_thumb:- "))
resistance_index = float(intput("Enter resistance_index:- "))
bend_index = int(intput("Enter bend_index:- "))
resistance_mid = float(intput("Enter resistance_mid:- "))
bend_mid = int(intput("Enter bend_mid:- "))
resistance_ring = float(intput("Enter resistance_ring:- "))
bend_ring = int(intput("Enter bend_ring:- "))
resistance_little = float(intput("Enter resistance_little:- "))
bend_little = int(intput("Enter bend_little:- "))
x = int(intput("Enter X :- "))
y = int(intput("Enter Y :- "))
z = int(intput("Enter Z :- "))

model_pred = classifier.predict([[resistance_thumb,bend_thumb, resistance_index,
                                  bend_index, resistance_mid, bend_mid, 
                                  resistance_ring, bend_ring, 
                                  resistance_little, bend_little,
                                  x,y,z]])

if model_pred == '0':
    print("Stage 0")
elif model_pred == '1':
    print("Stage 1")
elif model_pred == '2':
    print("Stage 2")
elif model_pred == '3':
    print("Stage 3")
elif model_pred == '4':
    print("Stage 4")
elif model_pred == '5':
    print("Stage 5")
