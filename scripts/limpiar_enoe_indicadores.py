"""
Limpieza de archivos ENOE - Indicadores de Género
Extrae los indicadores 5 y 6 de cada trimestre y los guarda en CSV
listos para graficar con barras comparativas.

Uso:
    python limpiar_enoe_indicadores.py

Los archivos .xls deben estar en el mismo directorio que este script.
Los CSV resultantes se guardan también en el mismo directorio.

Requiere:
    - LibreOffice instalado (para convertir .xls → .xlsx internamente)
    - pandas, openpyxl
"""

import subprocess
import os
import pandas as pd
import re

# ── Configuración ─────────────────────────────────────────────────────────────

ARCHIVOS_XLS = [
    "enoe_indicadores_genero_2025_trim1.xls",
    "enoe_indicadores_genero_2025_trim2.xls",
    "enoe_indicadores_genero_2025_trim3.xls",
    "enoe_indicadores_genero_2025_trim4.xls",
]

HOJA = "Nacional_Indicadores"

# Columnas de interés: Total (6), Hombres (7), Mujeres (8)
COL_TOTAL   = 6
COL_HOMBRES = 7
COL_MUJERES = 8

# ── Utilidades ────────────────────────────────────────────────────────────────

def convertir_xls_a_xlsx(ruta_xls: str) -> str:
    """
    Convierte un .xls a .xlsx usando LibreOffice en el mismo directorio.
    Si ya existe el .xlsx, lo reutiliza.
    Devuelve la ruta del .xlsx generado.
    """
    directorio = os.path.dirname(os.path.abspath(ruta_xls))
    nombre_base = os.path.splitext(os.path.basename(ruta_xls))[0]
    ruta_xlsx = os.path.join(directorio, nombre_base + ".xlsx")

    if not os.path.exists(ruta_xlsx):
        print(f"  Convirtiendo {os.path.basename(ruta_xls)} → xlsx ...")
        resultado = subprocess.run(
            ["soffice", "--headless", "--convert-to", "xlsx",
             "--outdir", directorio, ruta_xls],
            capture_output=True, text=True, timeout=120,
        )
        if resultado.returncode != 0:
            raise RuntimeError(
                f"Error al convertir {ruta_xls}:\n{resultado.stderr}"
            )
    return ruta_xlsx


def extraer_trimestre(ruta_xls: str, df_raw: pd.DataFrame) -> str:
    """
    Detecta el trimestre desde la celda de encabezado (fila 4, col COL_TOTAL).
    Ejemplo de celda: "I TRIMESTRE  2025"  ->  "T1_2025"
    Si falla, lo infiere del nombre del archivo.
    """
    celda = str(df_raw.iloc[4, COL_TOTAL]) if pd.notna(df_raw.iloc[4, COL_TOTAL]) else ""
    match = re.search(r'([IVX]+)\s+TRIMESTRE\s+(\d{4})', celda, re.IGNORECASE)
    if match:
        romanos = {"I": 1, "II": 2, "III": 3, "IV": 4}
        num = romanos.get(match.group(1).upper(), match.group(1))
        return f"T{num}_{match.group(2)}"

    m = re.search(r'trim(\d)', os.path.basename(ruta_xls), re.IGNORECASE)
    if m:
        return f"T{m.group(1)}_2025"

    return os.path.splitext(os.path.basename(ruta_xls))[0]


def encontrar_inicio_indicador(df: pd.DataFrame, numero: int) -> int:
    """Devuelve el índice de la fila donde comienza el indicador `numero`."""
    patron = re.compile(rf'^\s*{numero}\.')
    for i, row in df.iterrows():
        for j in range(4):
            val = str(row[j]) if pd.notna(row[j]) else ""
            if patron.match(val):
                return i
    raise ValueError(f"No se encontro el indicador {numero} en la hoja.")


def encontrar_fin_bloque(df: pd.DataFrame, inicio: int) -> int:
    """
    Devuelve el índice de la primera fila DESPUES del bloque.
    El bloque termina cuando aparece el siguiente indicador numerado
    o una seccion (I, II, III ...).
    """
    patron = re.compile(r'^\s*(\d+\.|\bII?\b|\bIII\b|\bIV\b)\s')
    for i in range(inicio + 1, len(df)):
        for j in range(4):
            val = str(df.iloc[i, j]) if pd.notna(df.iloc[i, j]) else ""
            if patron.match(val):
                return i
    return len(df)


def construir_etiqueta(fila: pd.Series):
    """
    Reconstruye la etiqueta jerarquica de una fila concatenando el contenido
    de las columnas de contexto (2, 3, 4, 5) que tengan valor.
    Devuelve None si la fila no tiene categoria.
    """
    partes = []
    for j in [2, 3, 4, 5]:
        val = str(fila[j]).strip() if pd.notna(fila[j]) else ""
        if val:
            partes.append(val)
    return " > ".join(partes) if partes else None


# ── Extraccion ────────────────────────────────────────────────────────────────

def extraer_indicador(df: pd.DataFrame, numero: int,
                      nombre_indicador: str, trimestre: str) -> pd.DataFrame:
    """
    Extrae las filas de datos de un indicador y devuelve un DataFrame con:
        Trimestre | Indicador | Categoria | Total | Hombres | Mujeres

    Filtra automaticamente:
      - Filas sin valores numericos (encabezados internos).
      - Filas con Total = 0 en los tres generos (sin datos reales).
    """
    inicio = encontrar_inicio_indicador(df, numero)
    fin    = encontrar_fin_bloque(df, inicio)

    registros = []
    for i in range(inicio, fin):
        fila = df.iloc[i]
        etiqueta = construir_etiqueta(fila)
        if not etiqueta:
            continue

        total   = fila[COL_TOTAL]
        hombres = fila[COL_HOMBRES]
        mujeres = fila[COL_MUJERES]

        # Descartar filas sin valores numericos (sub-encabezados)
        valores = [total, hombres, mujeres]
        if not any(isinstance(v, (int, float)) and not pd.isna(v) for v in valores):
            continue

        def limpiar(v):
            return round(float(v), 4) if isinstance(v, (int, float)) and not pd.isna(v) else None

        t = limpiar(total)
        h = limpiar(hombres)
        m = limpiar(mujeres)

        # Descartar filas donde todos los valores son 0 (sin informacion real)
        vals_limpios = [v for v in [t, h, m] if v is not None]
        if vals_limpios and all(v == 0.0 for v in vals_limpios):
            continue

        registros.append({
            "Trimestre":  trimestre,
            "Indicador":  nombre_indicador,
            "Categoria":  etiqueta,
            "Total":      t,
            "Hombres":    h,
            "Mujeres":    m,
        })

    return pd.DataFrame(registros)


# ── Proceso por archivo ───────────────────────────────────────────────────────

def procesar_archivo(ruta_xls: str):
    """
    Convierte y carga un .xls, extrae los indicadores 5 y 6,
    y devuelve (df_ind5, df_ind6).
    """
    print(f"\nProcesando: {os.path.basename(ruta_xls)}")

    ruta_xlsx = convertir_xls_a_xlsx(ruta_xls)
    df_raw = pd.read_excel(ruta_xlsx, sheet_name=HOJA, header=None)

    trimestre = extraer_trimestre(ruta_xls, df_raw)
    print(f"  Trimestre: {trimestre}")

    ind5 = extraer_indicador(
        df_raw, 5,
        "Promedio de horas en actividades economicas (poblacion 15+ anos)",
        trimestre,
    )
    ind6 = extraer_indicador(
        df_raw, 6,
        "Promedio de ingreso por hora trabajada (poblacion ocupada)",
        trimestre,
    )

    print(f"  Indicador 5: {len(ind5)} categorias extraidas")
    print(f"  Indicador 6: {len(ind6)} categorias extraidas")

    return ind5, ind6


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    todos_ind5 = []
    todos_ind6 = []

    for nombre_xls in ARCHIVOS_XLS:
        ruta = os.path.join(script_dir, nombre_xls)
        if not os.path.exists(ruta):
            print(f"ADVERTENCIA: no se encontro '{nombre_xls}', se omite.")
            continue
        ind5, ind6 = procesar_archivo(ruta)
        todos_ind5.append(ind5)
        todos_ind6.append(ind6)

    if not todos_ind5:
        print("No se proceso ningun archivo. Verifica que los .xls esten en el mismo directorio.")
        return

    df_ind5 = pd.concat(todos_ind5, ignore_index=True)
    df_ind6 = pd.concat(todos_ind6, ignore_index=True)

    salida_ind5 = os.path.join(script_dir, "indicador5_horas_actividades_economicas.csv")
    salida_ind6 = os.path.join(script_dir, "indicador6_ingreso_por_hora.csv")

    df_ind5.to_csv(salida_ind5, index=False, encoding="utf-8-sig")
    df_ind6.to_csv(salida_ind6, index=False, encoding="utf-8-sig")

    print(f"\n[OK] {os.path.basename(salida_ind5)}")
    print(f"     {len(df_ind5)} filas | "
          f"{df_ind5['Trimestre'].nunique()} trimestres x "
          f"{df_ind5['Categoria'].nunique()} categorias")

    print(f"\n[OK] {os.path.basename(salida_ind6)}")
    print(f"     {len(df_ind6)} filas | "
          f"{df_ind6['Trimestre'].nunique()} trimestres x "
          f"{df_ind6['Categoria'].nunique()} categorias")

    print("\nEstructura de los CSV:")
    print("  Trimestre | Indicador | Categoria | Total | Hombres | Mujeres")
    print("  Una fila por (Trimestre x Categoria) -> ideal para barras agrupadas.")

    print("\nEjemplo – Indicador 5 (primeras 5 filas del T1):")
    muestra = df_ind5[df_ind5["Trimestre"] == df_ind5["Trimestre"].iloc[0]].head(5)
    print(muestra[["Trimestre", "Categoria", "Total", "Hombres", "Mujeres"]].to_string(index=False))


if __name__ == "__main__":
    main()
