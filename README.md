# AMLO sin pausas

Independientemente de tu afiliación política, si en algo podemos concordar todos, 
es en que Andrés Manuel López Obrador (AMLO), presidente electo de México, hace muchas pausas al hablar, en ocasiones excesivas.
 Por esta razón nace _AMLO sin pausas_, un script hecho en Python que quita todas las pausas del presidente al hablar.

## Ejemplo
 
 En el repositorio se encuentran dos archivos mp3 para que puedas ver las diferencias. El original fue sacado 
 de la conferencia mañanera de AMLO del [9 de enero de 2019](https://www.youtube.com/watch?v=gIEEjSb9xzA&)
 y el reducido fue creado con el script.

##  Cómo usarlo

Desde cualquier sistema que tenga Python y las dependencias instaladas, puedes ejecutar el
script de la siguiente manera:

```python
python amlo.py AUDIO.mp3 SALIDA.mp3
```

El formato del archivo de entrada puede ser mp3, wav, ogg, o [cualquier otra cosa que ffmpeg soporte](http://www.ffmpeg.org/general.html#File-Formats).

## Requerimientos y dependencias

El script fue probado en Ubuntu 18.04, Python 3.7 y ffmpeg 3.4.4.

Para instalar las librerías que utiliza el script:

```bash
pip install -r requirements.txt
```

Para instalar ffmpeg en sistemas basados en Debian (solo si planeas usar formatos diferentes a wav):

```bash
sudo apt install ffmpeg
```

## Disclaimer

Este script es solo un ejercicio en Python. No me hago responsable por el uso que se le dé.