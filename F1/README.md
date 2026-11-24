# Fase 1 — EDA reproducible: supervivencia en el Titanic

## Entregables y ejecución

- [Notebook ejecutado](mcdi503_f1_sumativo_grupo7.ipynb).
- [Informe técnico complementario](Informe_tecnico_MCDI503_Grupo7.pdf), tres páginas.
- [CSV de respaldo](data/titanic.csv).

Seguir las instrucciones de instalación del [README principal](../README.md). El notebook es autónomo: contiene las funciones y el CSV incorporado mediante gzip/Base64, con verificación SHA-256. El archivo CSV de respaldo no es una dependencia de ejecución. Una vez instaladas las bibliotecas, no se requiere internet. Las salidas guardadas registran 10 celdas ejecutadas en Python 3.14.8 (Windows).

## Datos y objetivo

Fuente: [Titanic de Seaborn](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv). Unidad de observación: registro de pasajero. El conjunto contiene 891 filas y 15 variables originales. Se busca caracterizar su calidad, distribuciones y patrones descriptivos de supervivencia.

## Preguntas y evidencias

| Pregunta | Secciones del notebook |
|---|---|
| P1. Estructura y calidad | 2, 3 y 7 |
| P2. Supervivencia general | 4 |
| P3. Supervivencia por grupos | 5 y 6 |
| P4. Distribuciones | 4, 5 y 7 |
| P5. Asociaciones descriptivas | 6 |

La sección 8 sintetiza las cinco respuestas y registra las decisiones metodológicas.

## Decisiones y hallazgos

Se conservan los nulos, las 107 filas repetidas posteriores a la primera ocurrencia y los valores potencialmente atípicos. Se incorporan dos variables familiares sobre una copia sin alterar las originales: 891 filas y 17 columnas finales. Sobreviven 342 pasajeros (38,38 %); mujeres 74,20 %, hombres 18,89 %; primera clase 62,96 %, segunda 47,28 % y tercera 24,24 %. Hay 177 edades y 688 cubiertas faltantes. No existe identificador único de pasajero; no se asume ausencia aleatoria ni representatividad, y las asociaciones no implican causalidad.

## Continuidad

Profundizar en mecanismos de ausencia, sensibilidad a extremos y asociaciones conjuntas en las siguientes fases.

## Referencia docente

Universidad Andrés Bello. (2026). *Semana 01. Sumativa 1: Avance proyecto Fase 1* [Guía y rúbrica de MCDI503]. Canvas.
