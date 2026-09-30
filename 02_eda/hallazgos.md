# Hallazgos del EDA

- El puntaje global tiene media 248.3 y mediana 245. El sesgo es 0.32: la forma es cercana a simétrica y no pide una transformación logarítmica.
- Hay 80 puntajes globales en cero y 1972 casos fuera de las vallas IQR (0.39% ). Se conservan: son resultados de la prueba, no fallas de captura.
- `COLE_BILINGUE` concentra el faltante grande (16.4% marcado como no reporta). El cuestionario familiar deja cerca del 3 % de celdas vacías. Conviene una categoría explícita de no respuesta, no borrar esas filas.
- La mediana del puntaje global sube del estrato 1 (233) al estrato 4 (277) y no sigue hasta el estrato 6 (246). Sin Estrato es el grupo más bajo (202). Kruskal-Wallis da épsilon²=0.068: las distribuciones difieren, con un efecto moderado.
- La mediana del colegio no oficial (272) queda por encima de la del oficial (239), con d=0.62. En el estrato 1, el 91% está en colegio oficial; en el estrato 4, el 60% está en colegio no oficial.
- La educación de la madre se asocia con superar la mediana del puntaje (V de Cramer=0.29). Quien reporta madre con educación profesional o de postgrado cae con más frecuencia sobre la mediana.
- Más horas de trabajo a la semana se asocian con un puntaje global más bajo (Spearman rho=-0.21). La relación es débil: trabajar no explica por sí solo el resultado.
- Los cinco puntajes de área se mueven juntos y el global es, en la práctica, su suma (correlación 0.994). Un modelo que use el global y las áreas a la vez cuenta dos veces el mismo desempeño.
- La mediana departamental no es plana: el extremo bajo de la gráfica y el alto no cuentan la misma historia. El departamento describe contexto; no alcanza para atribuir la diferencia solo al territorio.
