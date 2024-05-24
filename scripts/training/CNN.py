import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

# Definición del modelo 
def train_model(x : ndarray, y : ndarray):
  # Definición del modelo CNN
  model = Sequential()
  model.add(Embedding(input_dim=len(questions) + 1, output_dim=50, input_length=X.shape[1]))
  model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
  model.add(GlobalMaxPooling1D())
  model.add(Dense(units=10, activation='relu'))
  model.add(Dense(units=3, activation='softmax'))

  # Compilar el modelo
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  model.fit(X, y, epochs=10, batch_size=10)
  return model