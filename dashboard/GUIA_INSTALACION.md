# Guía de Instalación y Ejecución del Dashboard

[![HackODS UNAM](https://img.shields.io/badge/HackODS-UNAM-blue.svg)](https://www.hackods.unam.mx/) [![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/) [![uv](https://img.shields.io/badge/uv-astral-purple.svg)](https://docs.astral.sh/uv/) [![Quarto 1.4+](https://img.shields.io/badge/Quarto-1.4+-9cf.svg)](https://quarto.org/)

---

> **Sobre esta guía**
>
> Esta guía documenta **paso a paso** cómo configurar y ejecutar el dashboard interactivo del proyecto **Typers — HackODS 2026 UNAM**. Cubre desde la clonación del repositorio hasta la renderización usando **uv**
---

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

| Herramienta    | Descripción               | Enlace de Instalación                                 |
| :------------- | :------------------------ | :------------------------------------------------- |
| **Git**        | Control de versiones      | [git-scm.com](https://git-scm.com/downloads)       |
| **uv**         | Gestor de paquetes rápido | [astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |

> ⚠️ **Importante:** Con `uv`, no necesitas instalar Python manualmente ni crear tu entorno con `venv`. `uv` se encargará de descargar e instalar la versión de Python especificada en nuestro proyecto (3.14) de manera aislada automáticamente.

### Verificar las herramientas instaladas

Ejecuta los siguientes comandos para confirmar que todo está listo:

```bash
git --version        # ej. git version 2.45.0
uv --version         # ej. uv 0.4.x
```

---

## 2. Instalación paso a paso

### Paso 1 — Clonar el repositorio

Descarga el código fuente del proyecto desde GitHub:

```bash
git clone https://github.com/tu-usuario/Typers-HackODS.git
cd Typers-HackODS
```

### Paso 2 — Sincronizar el entorno con `uv`

Al utilizar `uv`, la creación del entorno virtual y la instalación de todas las dependencias exactas se hace con un solo comando:

```bash
uv sync
```

> **¿Qué hace esto?:** Esto leerá el archivo `uv.lock` e instalará los paquetes exactamente en las versiones con las que funciona el proyecto, asegurando 100% de reproducibilidad.

### Paso 3 — Verificar que los datos estén disponibles

El dashboard necesita el archivo de datos consolidado. Verifica que exista:

```bash
ls data/dataset_final_tablero.csv
```

Si el archivo **no existe**, debes ejecutar primero los scripts de limpieza y consolidación. **Utiliza `uv run`** para usar el entorno que acabas de crear:

```bash
# Ejecutar desde la raíz del proyecto
uv run jupyter execute scripts/limpieza_ingreso_promedio_PobOcupSex.ipynb
uv run jupyter execute scripts/limpieza_pobreza_poblacion_ocupada_sexo.ipynb
uv run jupyter execute scripts/limpieza_pobreza_poblacion_ocupada_formalidad.ipynb
uv run jupyter execute scripts/limpieza_laboral_jefatura_sexo.ipynb
uv run jupyter execute scripts/consolidacion_datos.ipynb
```

### Paso 4 — Verificar los assets del dashboard

El navbar del dashboard requiere dos imágenes. Confirma que estén presentes:

```bash
ls dashboard/assets/
# Debes ver:
#   logo_hackods.png
#   unam.png
```

---

## 3. Ejecutar el dashboard

### Renderizar dashboard

Para generar el archivo HTML **ejecuta este comando desde la raíz del proyecto**

```bash
uv run quarto render dashboard/index.qmd
```

Esto generará el sitio interactivo esperado.

---

## 4. Estructura del Proyecto

```
Typers-HackODS/
├── README.md
├── pyproject.toml               ← Configuración de dependencias (reemplaza requirements.txt)
├── uv.lock                      ← Archivo candado de versiones exactas 
├── .python-version              ← Establece que el entorno usará Python 3.14             ← Establece que el entorno usará 
├── LICENSE                      ← Licencia CC-BY-SA-4.0
├── data/
│   ├── dataset_final_tablero.csv    ← Datos consolidados (usa el dashboard)
│   ├── *.csv / *.xlsx / *.ods       ← Datos crudos CONEVAL / INEGI
│   └── clean_data/                  ← Datos intermedios limpios
├── scripts/
│   ├── limpieza_*.ipynb             ← Notebooks de limpieza de datos
│   └── consolidacion_datos.ipynb    ← Une todos los datasets
└── dashboard/                       ← Carpeta principal
    ├── index.qmd                    ← Código fuente del dashboard (Rúbrica T2)
    ├── GUIA_INSTALACION.md          ← Esta guía
    └── assets/
```

---

## 5. Solución de Problemas

### ❌ `ModuleNotFoundError: No module named '...'`

Asegúrate de estar corriendo el comando a través de `uv` (`uv run ...`) y de haber sincronizado tu entorno:

```bash
uv sync
```

### ❌ `FileNotFoundError: dataset_final_tablero.csv`

El archivo de datos consolidado no existe. Ejecuta los scripts de consolidación asegurándote de usar `uv run`:

```bash
uv run jupyter execute scripts/consolidacion_datos.ipynb
```

### ❌ `Las gráficas interactivas no funcionan o tira error Quarto`

Si tienes algún problema con Quarto, recuerda que `quarto-cli` ahora se instala directamente con `uv` en el proyecto. Ejecuta siempre a través de: `uv run quarto ...`

---

## 6. Referencia Rápida de Comandos

| Acción                  | Comando                                        |
| :---------------------- | :--------------------------------------------- |
| Instalar dependencias   | `uv sync`                                      |
| Correr notebook python  | `uv run jupyter execute scripts/archivo.ipynb` |
| Generar HTML final      | `uv run quarto render dashboard/index.qmd`     |

---

<p align="center">
  <strong>Typers — HackODS 2026 UNAM</strong><br>
  ODS 1: Fin de la Pobreza · ODS 5: Igualdad de Género
</p>
