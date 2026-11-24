# Fase 1 — EDA reproducible: supervivencia en el Titanic

## Archivos y ejecución
El notebook `mcdi503_f1_sumativo_grupo7.ipynb` y el PDF homónimo son los entregables principales. Seguir las instrucciones de instalación del README raíz. Las preguntas P1–P5 se vinculan con las secciones del notebook y se responden en la síntesis final.

## Fuente
Dataset de ejemplo de Seaborn: https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv
Copia local `data/titanic.csv`: 891 filas y 15 columnas. El archivo local fue reconstruido desde una copia disponible de Titanic y contrastado con el CSV del repositorio de Seaborn mediante longitud y checksum FNV-1a de texto normalizado (2301464178); ambos coincidieron. El notebook registra SHA-256 del archivo local para identificar la entrada. No se requiere internet durante la ejecución.

## Decisiones y resultados
Se conservan nulos, duplicados potenciales y extremos por falta de justificación para eliminarlos. Se crean `familia_a_bordo` y `viaja_solo`, verificando la conservación de filas y valores originales. La supervivencia general es 38,38 %; mujeres 74,20 %, hombres 18,89 %; primera clase 62,96 %, segunda 47,28 % y tercera 24,24 %. El análisis es exclusivamente descriptivo. La cobertura de edad y cubierta es incompleta y no existe identificador único.

## Continuidad
Profundizar posteriormente en faltantes, sensibilidad a extremos y análisis conjunto de variables. La referencia al apunte docente se conserva del README original; contrastar sus datos bibliográficos con el material oficial antes de entregar.
