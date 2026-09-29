"""Descarga las tres bases colombianas usadas en la fase de exploración.

No versiona los archivos: quedan en data/ y están en .gitignore.
"""

from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DESTINOS = {
    ROOT / "data" / "raw" / "saber11_2020_2.csv": (
        "https://www.datos.gov.co/api/views/rnvb-vnyh/rows.csv?accessType=DOWNLOAD"
    ),
    ROOT / "data" / "raw" / "calidad_aire_anual.csv": (
        "https://www.datos.gov.co/api/views/kekd-7v7h/rows.csv?accessType=DOWNLOAD"
    ),
    ROOT / "data" / "audio" / "rolo_speech_train.parquet": (
        "https://huggingface.co/datasets/Juliointheworld/rolo_speech_v01/resolve/main/data/train-00000-of-00001.parquet"
    ),
}


def descargar(destino: Path, url: str) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists() and destino.stat().st_size > 0:
        print(f"ya existe: {destino} ({destino.stat().st_size / 1_048_576:.1f} MB)")
        return
    print(f"descargando {destino.name} ...")
    urllib.request.urlretrieve(url, destino)
    print(f"listo: {destino} ({destino.stat().st_size / 1_048_576:.1f} MB)")


def main() -> None:
    for destino, url in DESTINOS.items():
        descargar(destino, url)


if __name__ == "__main__":
    main()