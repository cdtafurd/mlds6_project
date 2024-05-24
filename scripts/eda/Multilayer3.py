## Definición líibrerías
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

# Definición del modelo 
def train_model_2(x : ndarray, y : ndarray ) -> MLPClassifier:
  model = MLPClassifier(hidden_layer_sizes=(50), max_iter=200, verbose = True)  # Una capa oculta con 50 neuronas
  model.fit(x, y)
  return model
