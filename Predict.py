from sklearn.neural_network import MLPRegressor
import pandas

max_val = [12, 31, 7, 24, 180, 360]

def training(input_layer, output_layer):
	#for i in range(0, len(max_val)):
    input_layer.loc[:, '0'] /= max_val[0]
    input_layer.loc[:, '1'] /= max_val[1]
    input_layer.loc[:, '2'] /= max_val[2]
    input_layer.loc[:, '3'] /= max_val[3]
    input_layer.loc[:, '4'] /= max_val[4]
    input_layer.loc[:, '5'] /= max_val[5]

    #print(input_layer)
    
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(50,50,50,50,50), random_state=1)
    clf.fit(input_layer, output_layer)
    return clf

def predict(clf, input_val):
    return clf.predict(input_val)


#print(predict(training([[0., 0.], [1., 1.]], [0.,1.]), [2.,2.]))

#c = training([[0., 0.], [1., 1.]], [[0.],[1.]])
#v = predict(c, [2., 2.])
#print(v)
#v = predict(c, [-1., -2.])
#print(v)
