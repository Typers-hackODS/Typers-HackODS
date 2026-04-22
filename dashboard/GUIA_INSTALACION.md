# 📊 Guía de Instalación y Ejecución del Dashboard

[![HackODS UNAM](https://img.shields.io/badge/HackODS-UNAM-blue.svg)](https://www.hackods.unam.mx/) [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![Quarto 1.4+](https://img.shields.io/badge/Quarto-1.4+-9cf.svg)](https://quarto.org/)

---

> **📖 Sobre esta guía**
>
> Esta guía documenta **paso a paso** cómo configurar y ejecutar el dashboard interactivo del proyecto **Typers — HackODS 2026 UNAM**. Cubre desde la clonación del repositorio hasta la visualización del dashboard en tu navegador. Sigue cada sección en orden para garantizar una instalación exitosa.

---

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

| Herramienta    | Versión Mínima | Descripción               | Enlace de Descarga                                 |
| :------------- | :------------- | :------------------------ | :------------------------------------------------- |
| **Git**        | 2.30+          | Control de versiones      | [git-scm.com](https://git-scm.com/downloads)       |
| **Python**     | 3.10+          | Intérprete de Python      | [python.org](https://www.python.org/downloads/)    |
| **Quarto CLI** | 1.4+           | Motor de renderizado      | [quarto.org](https://quarto.org/docs/get-started/) |
| **pip**        | 21.0+          | Gestor de paquetes Python | Incluido con Python                                |

> ⚠️ **Importante:** **Quarto** no viene incluido con Python ni con pip. Es una herramienta independiente que debes descargar e instalar desde su [sitio oficial](https://quarto.org/docs/get-started/). Verifica la instalación con `quarto --version` en tu terminal.

### Verificar las herramientas instaladas

Ejecuta los siguientes comandos para confirmar que todo está listo:

```bash
git --version        # ej. git version 2.45.0
python3 --version    # ej. Python 3.14.3
quarto --version     # ej. 1.9.36
pip --version        # ej. pip 25.x
```

---

## 2. Instalación paso a paso

### Paso 1 — Clonar el repositorio

Descarga el código fuente del proyecto desde GitHub:

```bash
git clone https://github.com/tu-usuario/Typers-HackODS.git
cd Typers-HackODS
```

### Paso 2 — Crear el entorno virtual de Python

Es fundamental usar un entorno virtual para aislar las dependencias del proyecto:

```bash
# Crear el entorno virtual
python3 -m venv .venv
```

```bash
# Activar el entorno virtual

# Linux / macOS:
source .venv/bin/activate

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Windows (CMD):
.venv\Scripts\activate.bat
```

> 💡 **Tip:** Sabrás que el entorno está activo cuando veas `(.venv)` al inicio de tu línea de terminal.

### Paso 3 — Instalar las dependencias de Python

Instala todos los paquetes listados en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Las dependencias instaladas son:

| Paquete      | Uso                                                     |
| :----------- | :------------------------------------------------------ |
| `pandas`     | Manipulación y análisis de datos tabulares              |
| `numpy`      | Operaciones numéricas y estadísticas                    |
| `matplotlib` | Gráficos estáticos (scripts de limpieza)                |
| `seaborn`    | Visualizaciones estadísticas (scripts de limpieza)      |
| `jupyter`    | Kernel de Jupyter para ejecutar código Python en Quarto |
| `ipykernel`  | Conexión entre Jupyter y el motor de Quarto             |
| `plotly`     | Gráficas interactivas del dashboard                     |

### Paso 4 — Verificar que los datos estén disponibles

El dashboard necesita el archivo de datos consolidado. Verifica que exista:

```bash
ls data/dataset_final_tablero.csv
```

Si el archivo **no existe**, debes ejecutar primero los scripts de limpieza y consolidación:

```bash
# Ejecutar desde la raíz del proyecto con el entorno virtual activado
jupyter execute scripts/limpieza_ingreso_promedio_PobOcupSex.ipynb
jupyter execute scripts/limpieza_pobreza_poblacion_ocupada_sexo.ipynb
jupyter execute scripts/limpieza_pobreza_poblacion_ocupada_formalidad.ipynb
jupyter execute scripts/limpieza_laboral_jefatura_sexo.ipynb
jupyter execute scripts/consolidacion_datos.ipynb
```

### Paso 5 — Verificar los assets del dashboard

El navbar del dashboard requiere dos imágenes. Confirma que estén presentes:

```bash
ls dashboards/assets/
# Debes ver:
#   logo_hackods.png
#   unam.png
```

---

## 3. Ejecutar el dashboard

### 📦 Renderizar dashboard

Para generar el archivo HTML autocontenido

```bash
cd dashboards
quarto render dashboard.qmd
```

Esto genera `dashboard.html` en la misma carpeta. El archivo es **completamente autocontenido** (`embed-resources: true`) — puedes abrirlo directamente en cualquier navegador sin necesidad de un servidor.

---

## 4. Estructura del Proyecto

```
Typers-HackODS/
├── README.md
├── requirements.txt
├── LICENSE
├── data/
│   ├── dataset_final_tablero.csv    ← Datos consolidados (usa el dashboard)
│   ├── *.csv / *.xlsx / *.ods       ← Datos crudos CONEVAL / INEGI
│   └── clean_data/                  ← Datos intermedios limpios
├── scripts/
│   ├── limpieza_*.ipynb             ← Notebooks de limpieza de datos
│   └── consolidacion_datos.ipynb    ← Une todos los datasets
└── dashboards/
    ├── dashboard.qmd                ← Código fuente del dashboard
    ├── GUIA_INSTALACION.md          ← Esta guía
    └── assets/
        ├── logo_hackods.png
        └── unam.png
```

---

## 5. Solución de Problemas

### ❌ `ModuleNotFoundError: No module named '...'`

Asegúrate de tener el entorno virtual activado y las dependencias instaladas:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### ❌ `FileNotFoundError: dataset_final_tablero.csv`

El archivo de datos consolidado no existe. Ejecuta los scripts de consolidación:

```bash
source .venv/bin/activate
jupyter execute scripts/consolidacion_datos.ipynb
```

### ❌ `quarto: command not found`

Quarto CLI no está instalado o no está en el PATH del sistema. Descárgalo desde [quarto.org/docs/get-started](https://quarto.org/docs/get-started/).

### ❌ `No module named 'jupyter_client'` o problemas con el kernel

```bash
source .venv/bin/activate
pip install jupyter ipykernel
python -m ipykernel install --user --name=python3
```

### ❌ Las imágenes del navbar no aparecen

Asegúrate de ejecutar `quarto preview` **desde la carpeta `dashboards/`**, ya que las rutas a los assets son relativas:

```bash
cd dashboards
quarto preview dashboard.qmd
```

---

## 6. Referencia Rápida de Comandos

| Acción                  | Comando                                        |
| :---------------------- | :--------------------------------------------- |
| Activar entorno virtual | `source .venv/bin/activate`                    |
| Instalar dependencias   | `pip install -r requirements.txt`              |
| Generar HTML final      | `cd dashboards && quarto render dashboard.qmd` |

---

<p align="center">
  <strong>Typers — HackODS 2026 UNAM</strong><br>
  ODS 1: Fin de la Pobreza · ODS 5: Igualdad de Género
</p>
