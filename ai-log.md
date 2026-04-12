# Typers - HackODS 2026 UNAM 

## AI - Log sobre el uso de inteligencia artificial en el HackODS

## Herramientas utilizadas
- Gemini
- Claude (claude.ai)

---
## Filosofía de uso
El uso de IA en este proyecto fue con el fin de automatizar tareas como la limpieza de datos, y consultar dudas sobre algunos errores de codigo. La seleccion de los datasets, de los indicadores y de las variables, la interpretacion de las graficas y la narrativa, asi como el diseno del tablero fueron completamente ideadas por el equipo. Cualquier tarea que requiriera pensamiento critico y creatividad fue hecha por los integrantes de nuestro equipo, mientras que algunas de las tareas tecnicas fueron delegadas a los asistentes de IA.

---
## Registro de uso


### 2026-04-10 | Claude | Limpieza de archivos .xls 
- **Tarea**: Le solicitamos realizara un script de limpieza de datos para un conjunto de archicos .xls complejos.

- **Prompt**: "Ayudame escribiendo un codigo en python que limpie estos  archivos .xls. Lo que me interesa son los indicadores 5 y 6 por genero, no me importan ni el coeficiente de variacion ni el error estandar. Necesito que cada tabla de cada indicador se guarde en un archivo .csv distinto. Quiero que la estructura de la tabla sea tal que sea facil realizar graficas de barras comparativas."

- **Resultado**: Nos proporciono el codigo en un .py de limpieza `limpiar_enoe_indicadores.py`, y los archivos .csv ya limpios, con las variables que requeriamos, tal como se los solicitamos.

- **Decisión**: Elegimos conservar el archivo .py y los .csv

### 2026-04-08 | Gemini | Merge de distintos dataframes con informacion relevante y relacionada.
- **Tarea**: Escribir codigo para hacer un merge de varios datasets (previamente limpiados por nosotros) en un solo dataset maestro.
- **Prompt**: "Ayudame a escribir el codigo para unir estos cuatro dataframes en un solo dataframe maestro, usando como llave la fecha de cada fila. Dado que algunos dataframes tienen columnas en comun (ademas de la llave fecha), evita que en el dataframe maestro haya columnas repetidas."
- **Resultado**: Codigo de limpieza.
- **Decisión**: Modificamos la ruta para que funcionara con la estructura de nuestro proyecto.
  
### NO usamos IA para
- La seleccion de las variables relevantes para el analisis de la pregunta central del proyecto.
- El diseno de nuestro tablero
- La narrativa del tablero: La redaccion de la interpretacion de las graficas obtenidas fue propia.