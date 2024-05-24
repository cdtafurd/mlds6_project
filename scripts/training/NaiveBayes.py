import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

# Definición del modelo 
def train_model(x : ndarray, y : ndarray ):
  model = MultinomialNB()
  model.fit(X_train_vectors[key], y_train)
  return model