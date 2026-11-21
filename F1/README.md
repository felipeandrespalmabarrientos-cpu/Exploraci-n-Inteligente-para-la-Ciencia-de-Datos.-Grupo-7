# EDA reproducible: supervivencia en el Titanic

**MCDI503 · Evaluación Sumativa 1 · Fase 1 (noviembre de 2026)**

**Equipo:** Jorge Gutiérrez J., Felipe Palma B. y Cristian Grandón G.  
**Docente:** Sergio Paraíso M.

## 1. Descripción del proyecto

Este repositorio documenta una primera implementación de **análisis exploratorio de datos (EDA) reproducible** sobre el conjunto `titanic` de la biblioteca Seaborn. El objetivo es diagnosticar la calidad de los registros y describir patrones iniciales de supervivencia según características de los pasajeros, sin realizar inferencia causal ni entrenar modelos predictivos.

El trabajo integra código Python, resultados de ejecución, gráficos y celdas Markdown que explican las decisiones y sus implicancias. Se desarrolla en el marco de la Fase 1 de MCDI503 y sirve como base para etapas posteriores del proyecto.

## 2. Preguntas exploratorias

- ¿Qué estructura, cobertura y problemas de calidad presenta el dataset?
- ¿Cuál es la proporción general de pasajeros que sobrevivieron?
- ¿Cómo varía descriptivamente la supervivencia según sexo, clase y presencia de familiares a bordo?
- ¿Qué características presentan las distribuciones de edad, tarifa y acompañantes familiares?
- ¿Qué asociaciones iniciales se observan entre variables numéricas y grupos de pasajeros?

## 3. Datos y alcance

- **Fuente:** `sns.load_dataset("titanic")`, colección de datasets de ejemplo de Seaborn.
- **Unidad de análisis:** registro de pasajero.
- **Estructura observada:** 891 registros y 15 columnas originales.
- **Variables relevantes:** `survived`, `sex`, `pclass`, `class`, `age`, `fare`, `sibsp`, `parch`, `embarked`, `deck` y `alone`, entre otras.
- **Variables derivadas:** `familia_a_bordo = sibsp + parch + 1` y `viaja_solo = (familia_a_bordo == 1)`.
- **Alcance:** EDA descriptivo; no incluye pruebas de hipótesis, imputación de faltantes ni modelos predictivos.

**Nota:** la primera carga requiere acceso a internet si el dataset no está disponible en la caché local de Seaborn. El notebook adjunto **no implementa un respaldo CSV automático**: si se desea ejecutar completamente sin conexión, debe adaptarse explícitamente la celda de carga.

## 4. Organización del repositorio

Estructura sugerida:

```text
.
├── mcdi503_f1_sumativo_grupox.ipynb
├── requirements.txt
├── README.md
└── .gitignore                  # recomendado
```

El archivo de notebook del repositorio debe conservar el nombre efectivamente utilizado. El nombre mostrado es la convención sugerida para la entrega, no una dependencia del código.

## 5. Requisitos previos

- Python 3.11 o posterior, con versiones compatibles de las dependencias.
- Visual Studio Code con extensiones **Python** y **Jupyter**.
- Conexión a internet para instalar paquetes y, en la primera ejecución, obtener `titanic` desde Seaborn.
- Un archivo `requirements.txt` en la raíz del proyecto con, al menos:

```text
numpy
pandas
seaborn
matplotlib
ipykernel
notebook
```

Se recomienda fijar las versiones efectivamente utilizadas antes de la entrega definitiva para mejorar la reproducibilidad. El notebook registra las versiones de Python, pandas, Seaborn y NumPy; Matplotlib se utiliza para los gráficos.

## 6. Configuración del entorno en VS Code (Windows / PowerShell)

Abrir la carpeta del repositorio en VS Code y ejecutar en su terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdi503-titanic --display-name "Python (MCDI503 Titanic)"
```

Si PowerShell bloquea la activación, puede utilizarse el intérprete directamente sin modificar la política de ejecución:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

En VS Code, abrir el notebook y elegir **Select Kernel → Python Environments → `.venv`**, o el kernel registrado **Python (MCDI503 Titanic)**.

En macOS/Linux, la activación del entorno es `source .venv/bin/activate` y el comando para crear el entorno puede ser `python3 -m venv .venv`.

## 7. Ejecución reproducible

1. Verificar que el entorno virtual y el kernel seleccionados correspondan al proyecto.
2. Abrir el notebook y ejecutar **Restart Kernel and Run All Cells** (o la opción equivalente de VS Code).
3. Comprobar que la validación inicial de columnas y codificación de `survived` finalice correctamente.
4. Revisar que las tablas y gráficos se generen sin errores.
5. Confirmar que la síntesis final informe **dos columnas derivadas** y que el número de filas se haya conservado.
6. Guardar el `.ipynb` con sus salidas ejecutadas, si así lo requiere la entrega académica.

Las transformaciones se realizan sobre `df`, una copia de `titanic`, y no modifican las columnas originales. No se utiliza aleatoriedad en los cálculos principales.

## 8. Contenido del notebook

| Sección | Contenido |
|---|---|
| 1. Importación y carga | Librerías, versiones, carga desde Seaborn y validaciones iniciales |
| 2. Inspección inicial | Tipos, valores faltantes, duplicados y consistencia básica |
| 3. Estadísticas descriptivas | Resúmenes numéricos y frecuencias categóricas |
| 4. Variables derivadas | Tamaño familiar registrado, viaje individual y validación con `alone` |
| 5. Distribuciones univariantes | Histogramas y diagramas de caja |
| 6. Variables categóricas | Gráficos de frecuencias |
| 7. Relaciones entre variables | Supervivencia por grupos, dispersión y correlaciones |
| 8. Comparaciones entre grupos | Promedios y diagramas de caja de edad y tarifa |
| 9. Valores potencialmente atípicos | Detección mediante rango intercuartílico (IQR) |
| 10. Síntesis | Resumen de resultados, registro de decisiones, supuestos y limitaciones |

## 9. Principales hallazgos del avance

Los resultados registrados en el notebook incluyen:

- **Supervivencia global:** 342 de 891 pasajeros (**38,38 %**).
- **Cobertura:** 177 valores faltantes en `age` (**19,87 %**) y 688 en `deck` (**77,22 %**).
- **Duplicados completos:** 107 filas con valores idénticos; se conservan por falta de un identificador único de pasajero.
- **Supervivencia por sexo:** 74,20 % en mujeres y 18,89 % en hombres.
- **Supervivencia por clase:** 62,96 % en primera, 47,28 % en segunda y 24,24 % en tercera.
- **Composición familiar:** se agregan dos columnas sin modificar el número de registros; `viaja_solo` coincide con `alone` en los 891 casos.
- **Valores potencialmente atípicos por IQR:** 11 en edad y 116 en tarifa; no se eliminan automáticamente.

Estas cifras describen únicamente los registros disponibles. Las diferencias entre grupos **no demuestran causalidad**; las comparaciones de edad consideran observaciones con valores no faltantes.

## 10. Decisiones metodológicas y limitaciones

- Se conservan los registros completos, incluidos los aparentemente duplicados, porque no existe una clave que permita distinguir pasajeros repetidos de pasajeros distintos con atributos coincidentes.
- No se imputan edades ni cubiertas faltantes en esta fase; su tratamiento requiere un análisis posterior del mecanismo de ausencia.
- Los valores extremos detectados por IQR se documentan, pero no se consideran automáticamente errores.
- Las tasas de supervivencia se calculan **dentro de cada grupo** para evitar confundir diferencias de tamaño con diferencias de proporción.
- Las correlaciones de Pearson describen relaciones lineales y utilizan observaciones válidas por pares; los pares que incluyen edad tienen menor cobertura.
- `familia_a_bordo` es un tamaño familiar **registrado por pasajero**, no un identificador de familias distintas.
- No se realizan ajustes por factores de confusión ni generalizaciones más allá del dataset analizado.

## 11. Entrega académica

La evaluación de Fase 1 solicita un **notebook ejecutado** y un **informe PDF complementario de máximo tres páginas**, coherente con las preguntas, decisiones y hallazgos del notebook. El README y `requirements.txt` son documentación técnica de apoyo al repositorio y no sustituyen esos dos entregables.

Antes de enviar, revisar los nombres de archivos, los integrantes, las referencias bibliográficas y la correspondencia entre el PDF y las salidas del notebook.

## 12. Referencias y recursos

- Paraíso, S. (2026). *Resumen aplicado del libro: EDA mínimo viable* [Apunte]. Universidad Andrés Bello.
- [Documentación de Seaborn](https://seaborn.pydata.org/)
- [Documentación de pandas](https://pandas.pydata.org/docs/)
- [Documentación de Matplotlib](https://matplotlib.org/stable/)
- [Documentación de Jupyter](https://docs.jupyter.org/)

---

**Estado del proyecto:** primer avance exploratorio documentado. Los resultados deberán volver a comprobarse al ejecutar el notebook en el entorno definitivo del equipo.
