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

| Fuente | Indicador | Cobertura | Periodicidad |
|:------|:---------|:----------|:-------------|
| **INEGI · [ENOE](https://www.inegi.org.mx/programas/enoe/15ymas/)** | Ingreso laboral por sexo, rango salarial, entidad | 2005 Q1 – 2025 Q4 | Trimestral |
| **CONEVAL · [ITLP](https://www.coneval.org.mx/Medicion/Paginas/ITLP-IS_pobreza_laboral.aspx)** | Pobreza laboral, formal/informal, jefatura de hogar | 2005 Q1 – 2024 Q4 | Trimestral |
| **INEGI · Cuenta Satélite TNRH** | Valor económico del trabajo no remunerado por decil y función | 2019–2023 | Anual |
| **INEGI · ENUT 2019** | Horas de trabajo no remunerado por sexo y actividad | 2019 | — |
 
Todos los datos son oficiales, públicos y están descargados en `data/`. Los scripts de limpieza y el notebook de consolidación están versionados en `scripts/`. El dataset final que alimenta el tablero es `data/dataset_final_tablero.csv`.

---

## 4. Estructura del repositorio
```
Typers-HackODS/
├── README.md                         ← Este archivo
├── LICENSE                           ← Creative Commons BY-SA 4.0
├── pyproject.toml                    ← Dependencias (reemplaza requirements.txt)
├── uv.lock                           ← Versiones exactas — reproducibilidad 100%
├── .python-version                   ← Fija Python 3.14
│
├── dashboard/                        ← Tablero Quarto
│   ├── index.qmd                     ← Código fuente del dashboard 
│   ├── _quarto.yml                   ← Configura salida en ../docs 
│   ├── styles.css                    ← Sistema de diseño (variables, tipografía, grid)
│   ├── GUIA_INSTALACION.md           ← Guía detallada paso a paso
│   └── assets/
│       ├── logo_hackods.png
│       └── unam-logo.svg
│
├── docs/                             ← Salida del render (generada automáticamente)
│   └── index.html                    ← Tablero autocontenido listo para publicar
│
├── data/
│   ├── dataset_final_tablero.csv     ← Dataset consolidado que alimenta el tablero
│   ├── *.csv / *.xlsx / *.ods        ← Datos crudos de CONEVAL e INEGI
│   └── clean_data/                   ← Datos intermedios limpios por indicador
│       ├── enoe_salarios_sexo_entidad.csv
│       ├── brecha_generacional_clean.csv
│       ├── horas_no_remuneradas_sexo_funcion.csv
│       ├── trabajo_no_remunerado_valor_decil.csv
│       └── proyecciones.csv
│
└── scripts/
    ├── limpieza_*.ipynb              ← Un notebook por fuente
    └── consolidacion_datos.ipynb     ← Une todos los datasets
```
---
## 5. Reproducción del tablero
 
> La guía detallada está en [`dashboard/GUIA_INSTALACION.md`](dashboard/GUIA_INSTALACION.md).
 
### Requisitos
 
| Herramienta | Instalación |
|:------------|:------------|
| **Git** | [git-scm.com](https://git-scm.com/downloads) |
| **uv** (Astral) | [astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
 
> `uv` instala Python 3.14 y `quarto-cli` automáticamente — no necesitas instalarlos por separado.
 
### Pasos
 
```bash
# 1. Clonar el repositorio
git clone https://github.com/hackods/Typers-HackODS.git
cd Typers-HackODS
 
# 2. Sincronizar el entorno (instala Python + dependencias + Quarto)
uv sync
 
# 3. Renderizar el tablero
uv run quarto render dashboard/index.qmd
```
 
### Referencia rápida de comandos
 
| Acción | Comando |
|:-------|:--------|
| Instalar dependencias | `uv sync` |
| Correr notebook python | `uv run jupyter execute scripts/archivo.ipynb` |
| Generar HTML final | `uv run quarto render dashboard/index.qmd` |
 
---
## 6. Licencia
 
Este trabajo está licenciado bajo **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](LICENSE)**.
---
