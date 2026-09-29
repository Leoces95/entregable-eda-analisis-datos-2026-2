# Comparación de bases y elección

Exploración hecha sobre los archivos descargados, no sobre la ficha del portal.

| Base | Tipo de dato | Origen para el equipo | Registros | Atributos | Tamaño (MB) | Faltantes | Documentación | Uso posible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Saber 11 2020-2 | Tabular | Secundaria | 504872 | 81 | 373.5 | 40 columnas; celda vacía promedio 1.27% | Ficha en datos.gov.co e ICFES | Relación entre contexto del estudiante y puntaje |
| Calidad del aire anual | Tabular | Secundaria | 29683 | 28 | 8.5 | celda vacía promedio 0.02% | Ficha IDEAM en datos.gov.co | Comparar contaminantes entre estaciones y años |
| Rolo Speech v0.1 | Audio | Secundaria (primaria para quien grabó) | 220 | 6 | 29.4 | sin transcripciones vacías | Tarjeta de Hugging Face y licencia CC BY-NC-SA 4.0 | Reconocimiento de voz de un acento; no el EDA tabular del curso |

## Criterios

- **Completitud.** Saber 11 tiene faltantes reales en el cuestionario (sobre todo `COLE_BILINGUE` y el bloque familiar, cerca del 3 %). El aire está casi completo, así que deja poco que decidir sobre imputación. Rolo Speech está completo, pero es un solo hablante.
- **Relevancia.** Saber 11 permite hipótesis sobre estrato, educación de la madre, naturaleza del colegio y puntaje. El aire sirve para medio ambiente, aunque cada fila ya es un promedio anual. El audio no trae las variables que el EDA del curso pide contrastar.
- **Documentación.** Las dos tabulares tienen ficha pública en datos.gov.co. Rolo Speech tiene tarjeta de dataset y licencia, suficiente para descartarla con criterio y corta para un análisis largo.
- **Manejabilidad.** Saber 11 pesa 374 MB y abre en pandas. El aire es más liviano (8.5 MB). El audio cabe en disco, pero el trabajo posterior (IQR, chi-cuadrado, PCA de atributos) no es su análisis natural.

## Elección

**Saber 11, calendario A, periodo 2020-2.**

Es la base que deja hacer las tres fases con datos colombianos: hay categóricas y numéricas, faltantes que hay que justificar, puntajes donde se puede discutir si un valor extremo se conserva, y bastantes filas para una prueba estadística con tamaño del efecto. El archivo histórico 2010-2022 (más de 7 millones de filas) se deja por fuera por tamaño. El aire queda como segunda opción si el equipo prefiere medio ambiente. Rolo Speech cumple el segundo tipo de dato y no se elige como base final.
