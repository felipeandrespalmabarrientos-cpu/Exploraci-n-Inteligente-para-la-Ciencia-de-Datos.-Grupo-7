# Exploración Inteligente para la Ciencia de Datos — Grupo 7

**Universidad Andrés Bello (UNAB)** · Magíster en Ciencia de Datos e Inteligencia Artificial  
**Asignatura:** MCDI503 · Exploración Inteligente para la Ciencia de Datos  
**Periodo:** noviembre de 2026 · **Docente:** Sergio Paraíso M.

## Integrantes

- Felipe Palma Barrientos
- Cristian Grandón Grandón
- Jorge Gutiérrez Jaramillo

## Fase 1 — Análisis exploratorio reproducible

El objetivo es caracterizar la estructura, calidad y distribución de los datos del Titanic e identificar patrones descriptivos de supervivencia mediante un flujo trazable y reproducible. El alcance es descriptivo: no se realizan imputaciones, pruebas de hipótesis, modelos predictivos ni inferencias causales.

### Entregables

- [Notebook ejecutado](F1/mcdi503_f1_sumativo_grupo7.ipynb)
- [Informe técnico complementario (PDF)](F1/Informe_tecnico_MCDI503_Grupo7.pdf)
- [Documentación de Fase 1](F1/README.md)
- [CSV Titanic de respaldo](F1/data/titanic.csv)

Las fases posteriores se incorporarán conforme avance el curso.

## Instalación y ejecución (Windows / PowerShell)

Requisitos: Git, Python 3.14 y VS Code con extensiones Python y Jupyter. Desde la raíz del repositorio:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-cache-dir -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Abre el notebook y selecciona **Select Kernel → Python Environments → .venv**. Ejecuta **Restart Kernel and Run All Cells** y guarda las salidas. No es necesario activar el entorno desde PowerShell.

El notebook contiene sus funciones y una copia del CSV comprimida en gzip/Base64, validada mediante SHA-256. No necesita archivos externos ni internet una vez instaladas las dependencias. El CSV de la carpeta `data` es un respaldo, no un requisito de ejecución.

El notebook registra las versiones efectivas. Las salidas guardadas corresponden a Python 3.14.8 en Windows. Las dependencias están definidas mediante rangos en `requirements.txt`.

## Estructura actual

```text
.
├── .gitignore
├── .mailmap
├── README.md
├── requirements.txt
└── F1/
    ├── README.md
    ├── mcdi503_f1_sumativo_grupo7.ipynb
    ├── Informe_tecnico_MCDI503_Grupo7.pdf
    └── data/
        └── titanic.csv
```

Para Canvas se entregan únicamente el notebook ejecutado y el informe PDF. El entorno virtual y las cachés no se versionan.
