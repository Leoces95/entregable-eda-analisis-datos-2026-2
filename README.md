# Análisis de datos, evento 2 (2026-2)

## INTEGRANTES
- HAROL STIVEN RESTREPO RESTREPO
- JALVI HUMBERTO VILLEGAS TABORDA
- LEONEL ANTONIO MARTINEZ SILGADO
- YULIETH MARCELA URREGO RESTREPO

Exploración de tres bases colombianas, elección de una y análisis de Saber 11 (calendario A, 2020-2). El trabajo de esta rama cubre las tres fases del enunciado.

## Bases

| Base | Tipo | Papel |
|---|---|---|
| [Saber 11, 2020-2](https://www.datos.gov.co/Educaci-n/Saber-11-2020-2/rnvb-vnyh) | Tabular, secundaria | Base elegida |
| [Calidad del aire, promedio anual (IDEAM)](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Calidad-del-Aire-en-Colombia-Promedio-Anual/kekd-7v7h) | Tabular, secundaria | Explorada y no elegida |
| [Rolo Speech v0.1](https://huggingface.co/datasets/Juliointheworld/rolo_speech_v01) | Audio, secundaria para el equipo | Explorado para cubrir un segundo tipo de dato |

La justificación está en `01_exploracion/comparacion.md`.

## Cómo repetir el análisis

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/descargar_bases.py
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 01_exploracion/01_exploracion.ipynb
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 02_eda/02_eda.ipynb
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 03_preprocesamiento/03_preprocesamiento.ipynb
```

Los CSV y el audio quedan en `data/` y no se suben al repositorio (Saber 11 pesa unos 374 MB).

## Estructura

- `01_exploracion/` — fichas, comparación y elección.
- `02_eda/` — faltantes, atípicos, distribuciones, relaciones e hipótesis.
- `03_preprocesamiento/` — codificación, escalado y PCA.
- `resultados/figuras/` — gráficas que salen de los cuadernos.
