import pickle
import Predict
import pandas as pd

nn = pickle.load(open("nn.pickle", "rb"))

month = float(input("What month?"))/12
date = float(input("What date?"))/31
day = float(input("What day?"))/7
hour = float(input("What hour?"))/24
lat = float(input("What lat?"))/180
lng = float(input("What lng?"))/360

df_in = pd.DataFrame([[month, date, day, hour, lat, lng]])

#print(df_in)
print(Predict.predict(nn, df_in))


