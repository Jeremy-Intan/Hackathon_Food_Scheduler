from sklearn.neural_network import MLPClassifier

def training(input_layer, output_layer):
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
	clf.fit(input_layer, output_layer)
	return clf

def predict(clf, input_val):
	return clf.predict([input_val])


#print(predict(training([[0., 0.], [1., 1.]], [0.,1.]), [2.,2.]))

c = training([[0., 0.], [1., 1.]], [[0.],[1.]])
v = predict(c, [2., 2.])
print(v)
v = predict(c, [-1., -2.])
print(v)
