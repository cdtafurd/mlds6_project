# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es un Perceptrón Multicapa (MLP) utilizado para clasificar preguntas relacionadas con el proceso de admisión en la Universidad Nacional de Colombia. El modelo fue entrenado utilizando el dataset de preguntas y respuestas proporcionado por la Dirección Nacional de Admisiones.

## Variables de entrada

- `pregunta`: Texto de la pregunta realizada por el usuario.

## Variable objetivo

- `tema_id`: Identificador del tema al que pertenece la pregunta.

## Evaluación del modelo

### Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo incluyen:
- Precisión (Accuracy)
- Precisión (Precision)
- Matriz de confusión

### Resultados de evaluación

| Métrica            | Valor  |
|--------------------|--------|
| Precisión (Accuracy)| 0.78   |
| Precisión (Precision) | 0.76   |

![image](https://github.com/julianVelandia/Eureka/assets/52173621/b302211c-f6b8-4ce6-a706-2a0e5b363afe)


## Análisis de los resultados

El modelo baseline muestra una precisión del 78%, lo cual es un buen punto de partida. Sin embargo, el modelo presenta algunas debilidades, como una precisión ligeramente más baja en la clasificación de temas con pocas preguntas en el dataset. La matriz de confusión revela que algunas categorías se confunden con otras, indicando áreas para mejora.

## Conclusiones

El rendimiento del modelo baseline es adecuado para establecer una línea base. Áreas de mejora incluyen:
- Aumentar la cantidad de datos para temas con menos preguntas.
- Ajustar los hiperparámetros del modelo.
- Probar técnicas de preprocesamiento y modelos alternativos.

## Referencias

- Documentación de Scikit-learn para MLPClassifier
- Dataset proporcionado por la Dirección Nacional de Admisiones de la Universidad Nacional de Colombia