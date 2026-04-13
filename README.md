# Typers - HackODS 2026 UNAM


[![HackODS UNAM](https://img.shields.io/badge/HackODS-UNAM-blue.svg)](https://www.hackods.unam.mx/) [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![Quarto](https://img.shields.io/badge/Quarto-Dashboard-9cf.svg)](https://quarto.org/)

---

## 1. Datos del equipo

- **Equipo:** Typers
- **Integrantes:**
    - Enrique Emiliano Cano García
    - Valentina Ayelen Cruz Mendoza
    - Valeria Vianey Rodríguez Barrera

- **ODS elegidos:**
    - **ODS 1:** Fin de la pobreza
    - **ODS 5:** Igualdad de género

---

## 2. Descripción del Problema

**Pregunta Central**

¿Cuál es el impacto de la brecha salarial de género en la tasa de pobreza laboral a nivel nacional en México?

**Coherencia Narrativa**

El proyecto analiza la intersección empírica entre la desigualdad de género y la precariedad económica extrema en el país. La premisa narrativa sostiene que la pobreza laboral no es un fenómeno neutral, sino que está fuertemente impulsado por una estructura salarial discriminatoria. Las mujeres en México enfrentan un doble impacto: menores ingresos promedio frente a sus pares masculinos y una alta concentración en el sector informal. A través de este análisis de datos, se demuestra cómo esta brecha de ingresos empuja a las mujeres por debajo de la Línea de Pobreza Extrema por Ingresos (canasta alimentaria), evidenciando que el ODS 1 (Fin de la pobreza) es inalcanzable sin antes erradicar la disparidad salarial establecida en el ODS 5 (Igualdad de género).

**Potencial Impacto**

Este tablero proporciona herramientas para la visualización y el conocimiento público al cuantificar a nivel nacional cómo la brecha de género condena a más mujeres a la pobreza laboral, el proyecto visibiliza un fallo sistémico. Demuestra con datos oficiales que la simple inserción laboral de la mujer en la economía mexicana no garantiza su subsistencia básica si persisten la informalidad y la desigualdad salarial, orientando el debate público hacia reformas estructurales urgentes en materia de equidad de ingresos y formalización.

---

## 3. Selección, calidad y metadatos de los datos

### Diccionario de Datos y Metadatos

| Dataset / Archivo | Fuente | Fecha de Descarga | Licencia de Origen | Descripción de Variables Clave |
| :--- | :--- | :--- | :--- | :--- |
| **ITLP - Porcentaje de pobreza laboral nacional** | CONEVAL ([Lineas de pobreza por ingresos](https://www.coneval.org.mx/Medicion/MP/Paginas/Lineas-de-Pobreza-por-Ingresos.aspx), [Cuadros de ITLP e indicadores](https://www.coneval.org.mx/Medicion/Paginas/ITLP-IS_pobreza_laboral.aspx)) | 6 de abril de 2026 | Libre Uso Gubernamental | `Trimestre`: Periodo de evaluación.<br>`Porcentaje`: Proporción de la población con ingreso laboral inferior a la LPEI. |
| **ENOE - Población ocupada por nivel de ingresos** | INEGI ([Tabulados básicos y de indicadores de género](https://www.inegi.org.mx/programas/enoe/15ymas/)) | 6 de abril de 2026 | Uso Libre INEGI | `Sexo`: Hombre / Mujer.<br>`Nivel_Ingresos`: Agrupación en Salarios Mínimos.<br>`Condicion_Formalidad`: Empleo formal / informal. |

---

## 4. Estructura del repositorio
* `datos/`: Contiene los archivos crudos (.csv / .xlsx) extraídos de CONEVAL e INEGI.
* `scripts/`: Código en Python empleado para la limpieza, cruce y estandarización de las bases de datos.
* `dashboard/`: Archivo fuente `.qmd` que contiene el prototipo del tablero, la estructura narrativa en Markdown y la generación de las visualizaciones interactivas.
