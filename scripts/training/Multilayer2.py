## Definición líibrerías
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

# Definición del modelo 
def train_model_2(x : ndarray, y : ndarray ) -> MLPClassifier:
  model = MLPClassifier(hidden_layer_sizes=(60,10), max_iter=200, verbose = True)  # Dos capas ocultas 1ra con 100 neuronas segunda con 10 neuronas
  model.fit(x, y)
  return model
