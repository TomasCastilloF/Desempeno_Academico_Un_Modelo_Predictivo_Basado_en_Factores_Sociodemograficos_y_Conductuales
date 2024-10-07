<h3 align="center">Desempeño Académico de Estudiantes: Un Modelo Predictivo Basado en Factores Sociodemográficos y Conductuales</h1>
Haremos un modelo para una institución portuguesa, que identifique a aquellos alumnos que presentan un bajo desempeño académico, medido en el promedio final del año escolar. Para ello, te envían un archivo con registros sociodemográficos y conductuales de los alumnos de dos escuelas para perfilar a los estudiantes. El objetivo es crear un modelo predictivo que permita saber si los estudiantes aprobarán o reprobarán el año académico.

### Descripción de la Base de Datos
Para realizar el modelamiento, debes emplear el archivo students.csv . Las variables que componen la base de datos son las siguientes:
| Atributo  | Descripción  |
|-----------|--------------|
| `school`  | Escuela del estudiante. (binaria: 'GP' - Gabriel Pereira o 'MS' - Mousinho da Silveira). |
| `sex`     | Sexo del estudiante. (binaria: 'F' - Mujer o 'M' - Hombre). |
| `age`     | Edad del estudiante. (numérica: de 15 a 22). |
| `address` | Ubicación de la casa del estudiante. (binaria: 'U' - urbana o 'R' - rural). |
| `famsize` | Tamaño de la familia. (binaria: 'LE3' - less or equal to 3 or 'GT3' - greater than 3). |
| `Pstatus` | Estado cohabitacional de los padres. (binaria: 'T' - cohabitando juntos o 'A' - viviendo separados). |
| `Medu`    | Nivel educacional de la madre. (numérica: 0 - ninguno, 1 - educación básica (4to), 2 - de 5to a 9, 3 - educación media, o 4 - educación superior). |
| `Fedu`    | Nivel educacional del padre. (numérica: 0 - ninguno, 1 - educación básica (4to), 2 - de 5to a 9, 3 - educación media, o 4 - educación superior). |
| `Mjob`    | Ocupación de la madre. (nominal: 'teacher' profesora, 'health' relacionada a salud, 'services' (e.g. administración pública o policía), 'at_home' en casa u 'other' otra). |
| `job`     | Ocupación del padre (nominal: 'teacher' profesor, 'health' relacionado a salud, 'services' (e.g. administración pública o policía), 'at_home' en casa u 'other' otra). |
| `reason`  | Razón para escoger la escuela (nominal: 'home' cercano a casa, 'reputation' reputación de la escuela, 'course' preferencia de cursos u 'other' otra). |
| `guardian`| Apoderado del estudiante (nominal: 'mother' madre, 'father' padre u 'other' otro). |
| `traveltime` | Tiempo de viaje entre hogar y colegio. 1: menos de 15 min, 2: de 15 a 30 min, 3: de 30 min. a 1 hora, 4: más de 1 hora. |
| `studytime` | Horas semanales dedicadas al estudio. 1: menos de 2 horas, 2: de 2 a 5 horas, 3: de 5 a 10 horas, 4: más de 10 horas. |
| `failures` | Número de clases reprobadas. (numérica: n si 1<=n<3, de lo contrario 4). |
| `schoolsup` | Apoyo educacional del colegio. (binaria: sí o no). |
| `famsup`  | Apoyo educacional familiar. (binaria: sí o no). |
| `paid`    | Clases particulares pagadas (matemáticas o portugués). (binaria: sí o no). |
| `activities` | Actividades extracurriculares. (binaria: sí o no). |
| `nursery` | Asistió a guardería infantil. (binaria: sí o no). |
| `higher`  | Desea proseguir estudios superiores. (binaria: sí o no). |
| `internet` | Acceso a internet desde el hogar. (binaria: sí o no). |
| `romantic` | Relación romántica. (binaria: sí o no). |
| `famrel`  | Calidad de las relaciones familiares. (numérica: de 1 - muy malas a 5 - excelentes). |
| `freetime` | Tiempo libre fuera del colegio. (numérica: de 1 - muy poco a 5 - mucho). |
| `goout`   | Salidas con amigos. (numérica: de 1 - muy pocas a 5 - muchas). |
| `Dalc`    | Consumo de alcohol en día de semana. (numérica: de 1 - muy bajo a 5 - muy alto). |
| `Walc`    | Consumo de alcohol en fines de semana. (numérica: de 1 - muy bajo a 5 - muy alto). |
| `health`  | Estado de salud actual. (numérica: de 1 - muy malo a 5 - muy bueno). |
| `absences` | Cantidad de ausencias escolares. (numérica: de 0 a 93). |
| `G1`      | Notas durante el primer semestre. (numérica: de 0 a 20). |
| `G2`      | Notas durante el segundo semestre. (numérica: de 0 a 20). |
| `G3`      | Promedio final. (numérica: de 0 a 20). |

### Aspectos adicionales a considerar
-	Considera que la nota mínima de aprobación y promoción es 12.
-	El área de bienestar estudiantil sugiere inspeccionar una batería de preguntas asociadas a aspectos ambientales del alumno (de famrel a health) y ver si éstas se pueden abstraer en categorías latentes.
-	La base de datos presenta una serie de anomalías. En la escuela no tienen buenas prácticas sobre cómo ingresar datos, por lo que existen datos perdidos que están registrados bajo tres categorías: nulidade, sem validade, zero. De manera adicional, hay 3 variables numéricas que se registraron como strings, cuya interpretación en pandas devuelve una estructura de datos genérica. Finalmente, la base está con un encoding distinto al normal y los delimitadores son distintos.
-	Para simplificar el análisis y su posterior inclusión en un modelo predictivo, se sugiere recodificar las variables binarias como 0 y 1. El procedimiento también debe aplicarse para aquellas variables nominales con más de dos categorías siguiendo la misma lógica.
-	En la parte de modelación descriptiva, se deben generar modelos utilizando todos los predictores por cada una de las notas registradas en G3.
-	Para la parte de modelación predictiva, se debe generar un modelo para predecir si el estudiante aprobará o reprobará el año.
