import Predict
import pandas as pd
import pickle

training_input = pd.read_csv("datas_in.csv", header = 0, index_col = 0)
training_output = pd.read_csv("datas_out.csv", header = 0, index_col = 0)

nn = Predict.training(training_input[0:1000], training_output[0:1000])
pickle.dump(nn, open("nn.pickle", "wb"))
#print(Predict.predict(nn, training_input[0:1]))
