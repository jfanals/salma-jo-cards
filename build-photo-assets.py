"""Build embedded monochrome backgrounds for the Live wire gallery.
Preview only: permissions must be confirmed before print. Requires Pillow.
"""
import base64
import io
import json
import qrcode
from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parent
photos = [
    dict(id='mate-live', name='Live / red stage', file='salma-jo-mate-preview.jpg',
         source='https://www.matefestival.com/projeto/salma-jo/', publication='MATE Festival',
         credit='Filename suggests @nataliamichalzuk; credit not independently confirmed.', y=50),
    dict(id='dm-live', name='Live / dark atmosphere', file='salma-jo-live-dm.jpg',
         source='https://www.dm.com.br/entretenimento/salma-jo-descobri-ainda-mais-a-forca-das-minhas-letras/',
         publication='Diário da Manhã', credit='Page credits @nataliamichalzuk.', y=50),
    dict(id='dm-portrait', name='Portrait / at the mic', file='salma-jo-portrait-dm.jpg',
         source='https://www.dm.com.br/entretenimento/salma-jo-descobri-ainda-mais-a-forca-das-minhas-letras/',
         publication='Diário da Manhã', credit='Filename suggests Emily Colona; credit not independently confirmed.', y=25),
    dict(id='hotel', name='Hotel / neon portrait', file='salma-jo-hotel.jpg',
         source='https://www.arte-factos.net/noticia-musica/salma-jo-lanca-hotel-o-seu-primeiro-single-solo-apos-a-pausa-dos-carne-doce/',
         publication='Arte-Factos', credit='Photographer credit not confirmed.', y=45),
]
for photo in photos:
    image = Image.open(root / 'assets' / photo['file'])
    photo['width'], photo['height'] = image.size
    image = ImageOps.autocontrast(ImageOps.grayscale(image), cutoff=1)
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=92)
    photo['data'] = 'data:image/jpeg;base64,' + base64.b64encode(buffer.getvalue()).decode('ascii')
    photo['thumbnail'] = 'assets/' + photo.pop('file')
    photo['x'] = 50

(root / 'assets/photo-data.js').write_text(
    '/* Web-sourced photo previews. Print permission not confirmed. */\n'
    'window.SALMA_PHOTOS = ' + json.dumps(photos, ensure_ascii=False) + ';\n'
)
press_url = 'https://tinyurl.com/salmajo-epk'
qr_image = qrcode.make(press_url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=4)
buffer = io.BytesIO()
qr_image.save(buffer, format='PNG')
qr = 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode('ascii')
(root / 'assets/qr-data.js').write_text(
    'window.SALMA_PRESS_URL = ' + json.dumps(press_url) + ';\n'
    'window.SALMA_PRESS_DISPLAY = "tinyurl.com/salmajo-epk";\n'
    'window.SALMA_QR = ' + json.dumps(qr) + ';\n'
)
