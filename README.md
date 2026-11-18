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

## 5. Reproducibilidad

Los siguientes pasos permiten preparar un entorno virtual y ejecutar los notebooks del proyecto en **Windows con PowerShell**. Ejecuta los comandos desde la raíz del repositorio, una vez clonado.

**Requisitos previos**

- Git y Python instalados, con los comandos `git` y `py` disponibles en PowerShell.
- El archivo [requirements.txt](./requirements.txt) con las dependencias base del proyecto: JupyterLab, IPython kernel, NumPy, pandas, SciPy, Matplotlib y seaborn.
- Los datos de entrada indicados en el notebook de la fase correspondiente, respetando las rutas documentadas.

Las dependencias iniciales no tienen versiones fijadas. Una vez validado el entorno con los notebooks, el equipo deberá registrar las versiones utilizadas y la versión de Python para reproducir el mismo entorno.

### Paso 1. Clonar el repositorio

```powershell
git clone "https://github.com/felipeandrespalmabarrientos-cpu/Exploraci-n-Inteligente-para-la-Ciencia-de-Datos.-Grupo-7.git"
cd "Exploraci-n-Inteligente-para-la-Ciencia-de-Datos.-Grupo-7"
```

Si ya tienes una copia local, abre PowerShell en la carpeta del proyecto y continúa con el paso 2.

### Paso 2. Preparar el entorno y ejecutar JupyterLab

El entorno `.venv` mantiene las dependencias del proyecto separadas de otras instalaciones de Python. Los siguientes comandos crean el entorno, instalan las dependencias de [requirements.txt](./requirements.txt) y abren JupyterLab. Utilizan directamente el intérprete del entorno, por lo que no es necesario activarlo.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

En JupyterLab, abre el notebook de la fase correspondiente. Reinicia el kernel y ejecuta todas las celdas en orden, desde la primera hasta la última, para comprobar que el análisis no depende de ejecuciones previas.

Para mantener la reproducibilidad, cada notebook debe documentar los datos de entrada, las transformaciones realizadas y, cuando corresponda, la semilla aleatoria utilizada. Las rutas a los datos deben ser relativas al proyecto y evitar ubicaciones específicas del equipo de un integrante.

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
├── F2/
│   ├── notebooks/
│   ├── reports/
│   └── data/
│
├── F3/
│   ├── notebooks/
│   ├── reports/
│   └── data/
│
├── F4/
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
