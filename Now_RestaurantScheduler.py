import pickle
import Predict
import pandas as pd
import timeNow
import currentLoc

nn = pickle.load(open("nn.pickle", "rb"))

L = timeNow.timeNow()
loc = currentLoc.getLocation();
loc[0] += 90
loc[1] += 180
L[0].extend(loc)

print("At time and location")
print(L[0])

df_in = pd.DataFrame(L)

print

#print(df_in)
print(Predict.predict(nn, df_in))


