import sys
sys.path.append('/Users/melo/.pyenv/versions/anaconda-2.4.0/lib/python2.7/site-packages')
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.optimizers import Adagrad, Adam, SGD
from keras.utils import np_utils
from time import sleep
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
#############################################
# prepare data
#############################################
# dataframe = pandas.read_csv("iris.csv", header=None)
# dataset = dataframe.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
#############################################
# define baseline model
#############################################
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
	model.add(Dense(3, init='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)

#############################################
# V-vold validation
#############################################
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

#############################################
# print results
#############################################
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))





