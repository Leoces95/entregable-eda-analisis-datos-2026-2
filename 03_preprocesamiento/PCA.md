# Preprocesamiento

- Filas usadas: 504,538 (se quitaron solo los registros sin puntaje de inglés).
- Matriz para PCA: 37 columnas (5 puntajes y el resto indicadoras).
- PC1 explica el 13.1% y PC2 el 10.9%. Juntas, 23.9%.
- Hacen falta 21 componentes para pasar el 80 % de la varianza. Dos componentes no alcanzan para reemplazar la tabla: el contexto socioeconómico queda repartido en ejes siguientes.
- PC1 junta los cinco puntajes con el mismo signo: es un eje de desempeño. Quien saca más alto en las áreas queda hacia un costado de ese eje.
- Las cargas más grandes de PC2 son FAMI_EDUCACIONMADRE_No responde, FAMI_TIENEINTERNET_No responde, ESTU_HORASSEMANATRABAJA_No responde, FAMI_ESTRATOVIVIENDA_No responde, FAMI_TIENECOMPUTADOR_No responde. Ese eje agrupa a quien dejó el cuestionario en blanco: las indicadoras de no respuesta viajan juntas. No mide el desempeño ni ordena el estrato.
