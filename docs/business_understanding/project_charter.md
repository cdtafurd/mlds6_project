# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Nachabot clasificadora

## Objetivo del Proyecto

Establecer un mecanismo eficaz para clasificar las diferentes inquietudes que se presentan en el proceso de admisión de pregrado en la Universidad Nacional de Colombia. Esto es 
importante puesto que permite responder de manera más efectiva las preguntas y problemas específicos de los aspirantes. Adicionalmente, el proceso de admisión suele ser confuso para 
los aspirantes lo que responder de manera oportuna aumentaría la satisfacción de los usuarios. Por último, optimizar los recursos tanto tecnológicos como humanos es siempre imperativo 
en cualquier organización. 

## Alcance del Proyecto

### Incluye:

- Descripción de los datos disponibles: La Dirección Nacional de Admisiones de la Universidad Nacional de Colombia ha generado un archivo excel donde define 25 temas asociados al proceso de admisión. Estos temas son:

    1. Calendario
    2. Carreras
    3. Carreras virtuales
    4. Código colegio
    5. Código de seguridad
    6. Confirmación inscripción
    7. Discapacidad
    8. Documento de identidad
    9. Homologación de asignaturas
    10. Homologación inglés
    11. Icfes válido
    12. Lista de espera
    13. Matrícula
    14. PAES/PEAMA
    15. Pago virtual
    16. Pin
    17. Proceso de admisión
    18. Pruebas
    19. Puntajes de admisión
    20. Sisben
    21. Programa generación E
    22. Aspirantes en el exterior/extranjeros
    23. Modificación de datos
    24. Reembolso
    25. Sobre otras dependencias

    Cada una de estas categorias tiene un número de preguntas y respuestas asociados a dicho tema. En total, el dataset levantado por la dependencia consta de 425 pares de preguntas y respuestas.
    En promedio cada tema tiene 17 preguntas, sin embargo temas como carreras virtuales, homologación de asignaturas, sisben, programa generación E y modificación de datos tienen menos de 3 pares de preguntas y respuestas.

- Descripción de los resultados esperados: Se espera tener un algoritmo eficiente de clasificación de las inquietudes que se generan a partir del proceso de admisión, este con el fin de que cada duda llegue al área correspondiente y responder de manera oportuna cada una de ellas
- Criterios de éxito del proyecto:
    - Precisión del modelo: El modelo debe ser capaz de clasificar correctamente los textos en las categorías correspondientes con la mayor precisión posible. Esto se puede evaluar mediante métricas como la precisión, el recall y la puntuación F1.

    - Cobertura de temas: El modelo debe ser capaz de cubrir adecuadamente los 25 temas relacionados con el proceso de admisión de la universidad. Esto implica que cada tema esté representado en el conjunto de datos de entrenamiento y que el modelo pueda identificar y clasificar adecuadamente textos relacionados con cada uno de ellos.

    - Generalización: El modelo debe ser capaz de generalizar su capacidad de clasificación a nuevos datos que no ha visto durante el entrenamiento. Esto se puede evaluar utilizando conjuntos de datos de prueba separados que contienen textos que el modelo no ha visto previamente.

    - Tiempo de respuesta: El modelo debe ser capaz de clasificar los textos en tiempo real o en un tiempo razonablemente corto, para que pueda integrarse efectivamente en el proceso de admisión y proporcionar retroalimentación oportuna a los usuarios.

    - Robustez: El modelo debe ser robusto frente a ruido en los datos, variaciones en el estilo de escritura y otros factores que puedan afectar su desempeño en situaciones del mundo real.

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 6 de mayo al 12 de mayo |
| Preprocesamiento, análisis exploratorio | 2 semanas | del 13 de mayo al 26 de mayo |
| Modelamiento y extracción de características | 2 semanas | del 27 de mayo al 9 de junio |
| Despliegue | 2 semanas | del 10 de junio al 23 de junio |
| Evaluación y entrega final | 1 semanas | del 24 de junio al 30 de junio |


## Equipo del Proyecto

- Cristián Taffur - Ingeniero líder
- Julian Velandía - Científico de Datos 
- Leonardo Puertas - Científico de Datos

## Stakeholders

- Nombre y cargo de los stakeholders del proyecto
    - Mario Alberto Perez Rodriguez - Director de la Dirección Nacional de Admisiones
    - Erick Sanchez - Lider de desarrollo DNA
- Descripción de la relación con los stakeholders: El profesor Mario Alberto y el ingeniero Erick Sanchez son personas interesadas en el proyecto con el objetivo de posteriormente utilizarlo para una implementación de un chatbot basado en inteligencia artificial. Este chatbot sería una herramienta que tendría un impacto positivo en el rendimiento de la DNA al poder utilizar los recursos funcionales de una forma más efectiva y utilizar esta herramienta como solucionadora de preguntas en primera instancia sin la necesidad de recurrir al recurso humano.

- Expectativas de los stakeholders:  Esperan que el modelo clasificador tenga un buen rendimiento con el objetivo de ser utilizado como un componente en un sistema de chatbot que sirva como asistente virtual al proceso de admisión.