# Exploración Inteligente para la Ciencia de Datos — Grupo 7

**Universidad Andrés Bello (UNAB)**  
**Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial  
**Asignatura:** Exploración Inteligente para la Ciencia de Datos  
**Grupo:** 7  
**Periodo académico:** 2026

## Integrantes

- Felipe Palma Barrientos
- Cristian Grandón Grandón
- Jorge Gutiérrez Jaramillo

## 1. Descripción del proyecto

Este repositorio contiene el desarrollo del proyecto académico de **Exploración Inteligente para la Ciencia de Datos** correspondiente al Grupo 7.

El trabajo se organiza en distintas fases y sumativas, incorporando progresivamente:

- definición del problema;
- selección y descripción del conjunto de datos;
- análisis exploratorio;
- limpieza y transformación;
- visualización;
- interpretación de resultados;
- documentación de decisiones;
- conclusiones y limitaciones.

El objetivo es construir un flujo de trabajo claro, trazable y reproducible, donde cada análisis pueda relacionarse con una pregunta, una acción ejecutada y un resultado interpretable.

## 2. Objetivo general

Desarrollar un análisis exploratorio reproducible que permita comprender las características, relaciones y patrones presentes en un conjunto de datos, documentando las decisiones metodológicas y las limitaciones del análisis.

## 3. Índice del repositorio

| Fase | Contenido | Acceso |
|---|---|---|
| Fase 1 | Definición y exploración inicial | [Ir a F1](./F1/) |
| Fase 2 | Desarrollo del análisis exploratorio | [Ir a F2](./F2/) |
| Fase 3 | Análisis estadístico | [Ir a F3](./F3/) |
| Fase 4 | Resultados y presentación final | [Ir a F4](./F4/) |
| Documentación | Minutas, bibliografía y rúbricas | [Ir a docs](./docs/) |

## 4. Dataset

El conjunto de datos utilizado será documentado en el notebook y en el informe correspondiente a la primera fase.

La documentación incluirá:

- nombre del dataset;
- fuente de origen;
- enlace de consulta;
- unidad de observación;
- cantidad de filas y columnas;
- descripción de variables;
- tipos de datos;
- valores faltantes;
- justificación de su elección;
- relación con las preguntas de análisis.

## 5. Instalación mínima (Windows / PowerShell)

Esta es la guía central de instalación del proyecto. Instala Git, Python (por ejemplo, Python 3.11) y VS Code con las extensiones **Python** y **Jupyter**.

### Paso 1. Clonar el repositorio

```powershell
git clone "https://github.com/felipeandrespalmabarrientos-cpu/Exploraci-n-Inteligente-para-la-Ciencia-de-Datos.-Grupo-7.git"
cd "Exploraci-n-Inteligente-para-la-Ciencia-de-Datos.-Grupo-7"
```

Si ya tienes una copia local, abre PowerShell en la raíz del repositorio.

### Paso 2. Instalar las dependencias mínimas

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-cache-dir -r requirements.txt
```

No necesitas activar el entorno ni registrar un kernel global. [requirements.txt](./requirements.txt) incluye NumPy, pandas, seaborn y Matplotlib para el análisis, e ipykernel para ejecutar las celdas en VS Code. Sus dependencias internas se instalan automáticamente y también son necesarias.

### Paso 3. Ejecutar el notebook

Abre [el notebook de F1](./F1/mcdi503_f1_sumativo_grupox.ipynb) en VS Code. En **Select Kernel → Python Environments**, selecciona el intérprete `.venv\Scripts\python.exe` del proyecto y ejecuta **Restart Kernel and Run All Cells**.

La primera carga de Titanic requiere internet si el dataset no está en la caché de Seaborn. Consulta [la documentación de F1](./F1/README.md) para conocer el análisis.

### Alternativa opcional: navegador

La instalación mínima no incluye el servidor de Jupyter Notebook ni JupyterLab. Si prefieres el navegador, instala JupyterLab por separado (ocupará más espacio):

```powershell
.\.venv\Scripts\python.exe -m pip install --no-cache-dir jupyterlab
.\.venv\Scripts\python.exe -m jupyter lab
```

### Mantener el entorno liviano

- Instala solo las dependencias necesarias. No borres archivos internos de las bibliotecas.
- `--no-cache-dir` evita guardar descargas en la caché de pip; no reduce el tamaño de las bibliotecas instaladas en el entorno.
- Cambiar los requisitos no desinstala paquetes existentes. Para reducir un entorno anterior, detén sus kernels y terminales, elimina únicamente la carpeta `.venv` del proyecto y repite el paso 2. Antes, comprueba que solo contiene el entorno generado y no notebooks ni datos propios.
- Excluye `.venv/`, `venv/`, `__pycache__/` y `.ipynb_checkpoints/` mediante las reglas de Git. Cada integrante recrea su entorno: no se entrega ni se sube al repositorio.

Los requisitos tienen rangos de versiones, no versiones exactas. Antes de la entrega, ejecuta todos los notebooks y registra las versiones utilizadas y la versión de Python. Esta guía no implica que se hayan probado todas las versiones de Python.

## 6. Estructura del repositorio

```text
.
├── README.md
├── requirements.txt
│
├── F1/
│   ├── notebooks/
│   ├── reports/
│   └── data/
│
├── docs/
│   ├── bibliografia/
│   ├── minutas/
│   └── rubricas/
│
├── src/
│   └── módulos reutilizables
│
└── tests/
    └── pruebas automatizadas
