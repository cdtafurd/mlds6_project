# Definición de los datos

## Origen de los datos

- [ ] Especificar la fuente de los datos y la forma en que se obtuvieron.

Los datos han sido proporcionados por la Dirección Nacional de Admisiones de la Universidad Nacional de Colombia. La recolección y almacenamiento de estos datos se realizaron mediante el sistema de atención al ciudadano de la universidad, el cual gestiona solicitudes y preguntas frecuentes. Este sistema garantiza la precisión y confiabilidad de la información recopilada, asegurando que los datos reflejen de manera fiel las interacciones y necesidades de los usuarios del servicio.

## Especificación de los scripts para la carga de datos

- [ ] Especificar los scripts utilizados para la carga de los datos. 

## Referencias a rutas o bases de datos origen y destino

- [ ] Especificar las rutas o bases de datos de origen y destino para los datos.

### Rutas de origen de datos

- [ ] Especificar la ubicación de los archivos de origen de los datos:

Los archivos de origen de los datos se encuentran almacenados en el servicio de Google Drive. Esta elección de almacenamiento se debe a que los datos contienen información sensible y no cuentan con autorización para su divulgación pública. Por lo tanto, se han implementado medidas de seguridad estrictas para asegurar que el acceso a estos archivos esté restringido exclusivamente a personal autorizado, garantizando así la privacidad y protección de la información.

- [ ] Especificar la estructura de los archivos de origen de los datos.

Los datos de origen se encuentran en un archivo en formato .xlsx, que contiene aproximadamente 30 hojas de cálculo. Cada hoja está dedicada a un tema específico, relacionados con distintos aspectos del proceso de admisión y servicios estudiantiles. A continuación se detallan los temas abordados en cada hoja:

Calendario
Carreras
Carreras virtuales
Código colegio
Código de seguridad
Confirmación inscripción
Discapacidad
Documento de identidad
EPS
Homologación de asignaturas
Homologación inglés
Icfes válido
Lista de espera
Matrícula
PAES/PEAMA
Pago virtual
PIN
Proceso de admisión
Pruebas
Puntajes de admisión
SISBEN
Programa Generación E
Aspirantes en el exterior/extranjeros
Modificación de datos
Reembolso
Métodos de pago
Otras dependencias
Cada hoja de cálculo contiene dos campos principales: la pregunta del usuario y la respuesta proporcionada por el funcionario correspondiente.

Para este ejercicio inicial, se plantea la necesidad de clasificar las preguntas de acuerdo al tema al que hacen referencia. Esta clasificación permitirá asignar las consultas a la persona adecuada, optimizando así el tiempo de respuesta al usuario y mejorando la eficiencia del sistema de atención al ciudadano.

- [ ] Describir los procedimientos de transformación y limpieza de los datos.

### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
