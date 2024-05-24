# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final desarrollado para clasificar preguntas relacionadas con el proceso de admisión en la Universidad Nacional de Colombia alcanzó una precisión del 85% y una precisión ponderada del 83%. Estas métricas indican un rendimiento satisfactorio en la clasificación de las preguntas en las 25 categorías definidas. La matriz de confusión y otras métricas de evaluación también reflejan una mejora significativa en comparación con el modelo baseline.

## Descripción del Problema

El problema abordado es la clasificación de preguntas relacionadas con el proceso de admisión en la Universidad Nacional de Colombia. Este problema surge debido a la gran cantidad de consultas que reciben las diferentes áreas relacionadas con el proceso de admisión. El objetivo es desarrollar un modelo que clasifique eficientemente estas preguntas para proporcionar respuestas oportunas y precisas a los aspirantes, mejorando así la satisfacción del usuario y optimizando los recursos tecnológicos y humanos.

## Descripción del Modelo

El modelo final es un Perceptrón Multicapa (MLP) con dos capas ocultas de 100 y 50 neuronas, respectivamente. Se utilizó la metodología de procesamiento de lenguaje natural (NLP) para vectorizar las preguntas con `CountVectorizer`. El modelo fue entrenado con el dataset de preguntas y respuestas proporcionado por la Dirección Nacional de Admisiones. Se realizaron varios ajustes de hiperparámetros y técnicas de preprocesamiento para optimizar el rendimiento del modelo.

## Evaluación del Modelo

Las métricas de evaluación utilizadas para el modelo final incluyen:
- Precisión (Accuracy)
- Precisión (Precision)
- Matriz de confusión
- F1 Score

| Métrica            | Valor  |
|--------------------|--------|
| Precisión (Accuracy)| 0.85   |
| Precisión (Precision) | 0.83   |
| F1 Score           | 0.84   |

![image](https://github.com/julianVelandia/Eureka/assets/52173621/b302211c-f6b8-4ce6-a706-2a0e5b363afe)


La evaluación detallada muestra que el modelo final ha mejorado significativamente en comparación con el modelo baseline, especialmente en la clasificación de temas con menos datos. La matriz de confusión indica una reducción en la confusión entre categorías, y las métricas de precisión y F1 Score confirman un rendimiento robusto del modelo.

## Conclusiones y Recomendaciones

El modelo final presenta un rendimiento sólido en la clasificación de preguntas relacionadas con el proceso de admisión. Puntos fuertes del modelo incluyen su alta precisión y capacidad para manejar categorías con pocos datos. Las limitaciones del modelo incluyen posibles mejoras en la clasificación de preguntas con formulaciones muy similares pero que pertenecen a diferentes categorías. Se recomienda:
- Continuar recolectando más datos para mejorar el entrenamiento del modelo.
- Explorar técnicas adicionales de NLP y modelos más avanzados como Transformers.
- Realizar pruebas en un entorno real para ajustar y optimizar el modelo en función del feedback recibido.

## Referencias

- Documentación de Scikit-learn para MLPClassifier
- Dataset proporcionado por la Dirección Nacional de Admisiones de la Universidad Nacional de Colombia
- Artículos y documentación sobre técnicas de procesamiento de lenguaje natural y modelos de aprendizaje automático.