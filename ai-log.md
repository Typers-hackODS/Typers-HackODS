# Typers - HackODS 2026 UNAM 

## AI - Log sobre el uso de inteligencia artificial en el HackODS

## Herramientas utilizadas
- Gemini 3.1 pro 
- Claude Sonnet 4.6 (claude.ai)

---
## Filosofía de uso
- El uso de IA en este proyecto fue con el fin de automatizar tareas como la limpieza de datos, y consultar dudas sobre algunos errores de codigo. 
- La seleccion de los datasets, de los indicadores y de las variables, la interpretacion de las graficas y la narrativa, asi como el diseno del tablero fueron completamente ideadas por el equipo. Cualquier tarea que requiriera pensamiento critico y creatividad fue hecha por los integrantes de nuestro equipo, mientras que algunas de las tareas tecnicas fueron delegadas a los asistentes de IA.

---
## Registro de uso


### 08-04-2026 | Claude | Limpieza de archivos .xls 
- **Tarea**: Le solicitamos realizara un script de limpieza de datos para un conjunto de archicos .xls complejos.

- **Prompt**: "Ayudame escribiendo un codigo en python que limpie estos  archivos .xls. Lo que me interesa son los indicadores 5 y 6 por genero, no me importan ni el coeficiente de variacion ni el error estandar. Necesito que cada tabla de cada indicador se guarde en un archivo .csv distinto. Quiero que la estructura de la tabla sea tal que sea facil realizar graficas de barras comparativas."

- **Resultado**: Nos proporciono el codigo en un .ipynb de limpieza `limpiar_enoe_indicadores.ipynb`, y los archivos .csv ya limpios, con las variables que requeriamos, tal como se los solicitamos.

- **Decisión**: Elegimos conservar el archivo .ipynb y los .csv

### 08-04-2026 | Gemini | Merge de distintos dataframes con informacion relevante y relacionada.
- **Tarea**: Escribir codigo para hacer un merge de varios datasets (previamente limpiados por nosotros) en un solo dataset maestro.

- **Prompt**: "Ayudame a escribir el codigo para unir estos cuatro dataframes en un solo dataframe maestro, usando como llave la fecha de cada fila. Dado que algunos dataframes tienen columnas en comun (ademas de la llave fecha), evita que en el dataframe maestro haya columnas repetidas."

- **Resultado**: Codigo de limpieza.

- **Decisión**: Modificamos la ruta para que funcionara con la estructura de nuestro proyecto.


### 09-04-2026 | Gemini | Recomendación de paleta de colores
- **Tarea**: Pedir opciones de paleta para las gráficas, considerando accesibilidad y que los colores diferenciaran bien sexo y entidad.

- **Prompt**: "Recomienda una paleta de colores adecuada para mostrar diferencias de ingreso por sexo y sector en un dashboard de datos sociales, cuidando el contraste."

- **Resultado**: Paletas con alto contraste y combinaciones accesibles.

- **Decisión**: Seleccionamos una paleta basada en la recomendación y la adaptamos a nuestro estilo visual.

### 09-04-2026 | Gemini | Sugerencias para etiquetas y leyendas claras en el tablero
- **Tarea**: Le pedimos ideas para los textos de las etiquetas, ejes y filtros del dashboard, que fueran entendibles para alguien sin conocimientos técnicos.

- **Prompt**: "Dame ejemplos de etiquetas y leyendas en español para un tablero de indicadores laborales por género y entidad, que sean claras para usuarios no técnicos y mantengan coherencia con un diseño de estilo académico."

- **Resultado**: Lista de etiquetas recomendadas y descripciones cortas para ejes, filtros y tarjetas.

- **Decisión**: Tomamos algunas como punto de partida y las ajustamos al tono y estilo visual que ya habíamos definido.

### 2026-04-09 | Gemini | Ejemplos de configuración de dashboard
- **Tarea**: Pedir una propuesta de cómo organizar las secciones del tablero antes de tomar la decisión de diseño.

- **Prompt**: "Danos una estructura de cuatro secciones para un tablero sobre empleo y pobreza por género, indicando qué tipo de gráfico iría en cada sección."

- **Resultado**: Propuesta con secciones de contexto general, brecha de ingresos, formalidad laboral y conclusiones.

- **Decisión**: Usamos esa estructura como referencia para discutir en equipo el diseño final que terminamos ajustando con más secciones

### 2026-04-09 | Gemini | Revisión estratégica de variables

- **Tarea**: Validar si las variables que ya habíamos seleccionado eran suficientes para el análisis de pobreza laboral y salarios, o si había algo más que se considera importante tomar en cuenta.

- **Prompt**: "Revisa estas variables: "porcentaje de personas en pobreza laboral", "ingreso promedio por hora", "proporción de trabajo formal", y "brecha salarial por sexo". ¿Falta alguna que aporte contexto sin cambiar lo que ya tenemos?"

- **Resultado**: Identificó las variables ocupación principal y tasa de empleo informal.

- **Decisión**: Consideramos la recomendación como sugerencia, Las consideramos pero decidimos no incluirlas, porque estaban fuera del alcance que ya habíamos definido como equipo.


### 2026-04-09 | Claude |  Control de calidad para el dataset maestro

- **Tarea**: Pedir una lista de verificaciones básicas para asegurarnos de que el dataset maestro estuviera bien antes de usarlo en el tablero.

- **Prompt**: "Dame cinco controles de calidad para verificar un dataset maestro de ENOE: duplicados, valores atípicos, nulos y consistencia de llaves."

- **Resultado**:  Lista con controles concretos: duplicados, rangos plausibles, totales por entidad, nulos y tipos de dato.

- **Decisión**: Los ejecutamos todos y documentamos los resultados en el notebook.


### 2026-04-10 | Claude |  Verificación del texto de la tarjeta "Hogares en pobreza

- **Tarea**: Asegurarnos de que el dato 39.5% estaba correctamente descrito en la tarjeta antes de publicarlo porque la definición de jefatura de hogar puede prestarse a confusión.

- **Prompt**: "La tarjeta de nuestro tablero dice: '39.5% — Porcentaje de los hogares en pobreza cuya jefatura está a cargo de una mujer.' ¿Esta redacción puede confundirse con que el 39.5% de todas las mujeres están en pobreza, o queda claro que es el porcentaje de hogares pobres con jefa mujer?"

- **Resultado**:  Identificó que la redacción es ambigua y que un lector sin contexto puede interpretarla de dos formas distintas.

- **Decisión**: Decidimos no implementar el cambio porque la correlación es ineludible y se tiene que mostrar de esa manera

### 2026-04-11 | Claude | Mejoras de estilo en el README del tablero
- **Tarea**: Pedir una revisión de estilo al texto del README para que quedara más claro y ordenado.

- **Prompt**: "Revisa este texto y propón una versión más clara y profesional para la descripción de un dashboard sobre desigualdad salarial y pobreza laboral."

- **Resultado**: Se generó una versión más fluida y ordenada del texto.

- **Decisión**: Incorporamos algunos cambios puntuales de estilo, el contenido y el mensaje son nuestros.


### NO usamos IA para
- La selección de las variables relevantes para el análisis de la pregunta central del proyecto.
- El diseño de nuestro tablero
- La narrativa del tablero
- La narrativa del tablero: La redacción de la interpretación de las graficas obtenidas fue propia.