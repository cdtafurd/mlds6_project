# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos para el proyecto "Nachabot".

## Resumen general de los datos

### Descripción General

- **Número total de observaciones:** 425
- **Número total de variables:** 3 (Pregunta, Respuesta, Categoría)
- **Tipos de variables:** 
  - Pregunta: Texto
  - Respuesta: Texto
  - Categoría: Texto

### Distribución de las Variables

- **Preguntas y Respuestas:** Cada registro contiene una pregunta y su correspondiente respuesta.
- **Categorías:** Hay 25 categorías diferentes de acuerdo con el tema de la pregunta.

### Presencia de Valores Faltantes

- **Pregunta:** 0 valores faltantes
- **Respuesta:** 0 valores faltantes
- **Categoría:** 0 valores faltantes

## Resumen de calidad de los datos

### Valores Faltantes

- **Cantidad y porcentaje de valores faltantes:**
  - Pregunta: 0 (0%)
  - Respuesta: 0 (0%)
  - Categoría: 0 (0%)

### Valores Extremos y Errores

- **Valores Extremos:** No se identificaron valores extremos en las variables de texto.
- **Errores:** Se identificaron errores tipográficos en las preguntas y respuestas, los cuales fueron corregidos durante el preprocesamiento.

## Variable objetivo

### Descripción

- **Variable Objetivo:** Categoría
- **Descripción:** La categoría a la que pertenece cada pregunta.

## Variables individuales


### Pregunta

- **Estadísticas Descriptivas:**
  - Longitud media: 120 caracteres
  - Longitud mínima: 10 caracteres
  - Longitud máxima: 500 caracteres

- **Transformaciones Aplicadas:** 
  - Normalización del texto
  - Eliminación de caracteres especiales

### Respuesta

- **Estadísticas Descriptivas:**
  - Longitud media: 200 caracteres
  - Longitud mínima: 15 caracteres
  - Longitud máxima: 1000 caracteres

- **Transformaciones Aplicadas:**
  - Normalización del texto
  - Eliminación de caracteres especiales

### Categoría

- **Estadísticas Descriptivas:**
  - Número de categorías: 25
  - Número promedio de preguntas por categoría: 17


## Ranking de variables

- **Correlación:** La variable "Categoría" se analizó en relación con la longitud de las preguntas y respuestas.
- **Análisis de Componentes Principales (PCA):** No se aplicó debido a la naturaleza de las variables.
- **Importancia de Variables en Modelos de Aprendizaje Automático:**
  - Modelos utilizados: Random Forest, XGBoost
  - Variables más importantes: Longitud de la pregunta, palabras clave en la pregunta

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
