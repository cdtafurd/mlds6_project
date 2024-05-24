## Definición líibrerías
from google.colab import drive
import pandas as pd
from numpy import ndarray
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

## Montar Google Drive
drive.mount('/content/drive')

## función que extrae información de los archivos preprocesados
def get_column_from_excel(path_to_excel : str, shet_name : str, column_name : str) -> ndarray:
  excel_df = pd.read_excel(path_to_excel,  shet_name)
  column_vector = excel_df[column_name].to_numpy()
  return column_vector

## Lectura de conjunto de datos de entrenamiento
path_to_excel_train = '/content/drive/MyDrive/Colab Notebooks/dataSetEntrenamiento.xlsx'
sheet_name = 'preguntas'

question_column_name = "pregunta"
answer_id_column_name = "respuesta_id"
tema_id_column_name = "tema_id"

questions_train = get_column_from_excel(path_to_excel, sheet_name, question_column_name)
answers_id_train = get_column_from_excel(path_to_excel, sheet_name, answer_id_column_name)
temas_id_train = get_column_from_excel(path_to_excel, sheet_name, tema_id_column_name)

## Conjunto de datos de prueba
path_to_excel_test = '/content/drive/MyDrive/Colab Notebooks/dataSetValidacion.xlsx'
sheet_name = 'preguntas'

question_column_name_test = "pregunta"
answer_id_column_name_test = "respuesta_id"
tema_id_column_name = "tema_id"

questions_test = get_column_from_excel(path_to_excel_train, sheet_name, question_column_name_test)
answers_id_test = get_column_from_excel(path_to_excel_train, sheet_name, answer_id_column_name_test)
temas_id_test = get_column_from_excel(path_to_excel, sheet_name, tema_id_column_name)

## Definición de función de extracción de características

## Ajusta y transforma los documentos iniciales.
def vectorize_string_vector(strings_to_vectorize : ndarray, vectorizer : CountVectorizer) -> ndarray:
  string_vectorized = vectorizer.fit_transform(questions).toarray()
  return string_vectorized

## Transformar un nuevo texto basado en el vocabulario aprendido de los textos iniciales.

def vectorize_string(string : str, vectorizer : CountVectorizer) -> ndarray:
  return vectorizer.transform([string]).toarray()

## Aplica la transfromación de los datos requerida con n-gramas
vectorizer = CountVectorizer(ngram_range=(1, 2))  # Unigramas y bigramas

## Guarda los datos de entrenamiento transformados
X_train = vectorize_string_vector(questions_train, vectorizer)

