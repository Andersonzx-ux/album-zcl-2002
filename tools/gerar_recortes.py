# Gera os recortes reais da capa (assets/fios.jpg, cover-256/512). Uso: python3 -I tools/gerar_recortes.py
from PIL import Image
im = Image.open('assets/cover.jpg').convert('RGB')
im.resize((256, 256), Image.LANCZOS).save('assets/cover-256.jpg', quality=88)
im.resize((512, 512), Image.LANCZOS).save('assets/cover-512.jpg', quality=90)
im.crop((0, 538, 640, 582)).save('assets/fios.jpg', quality=95)   # faixa dos fios (progresso)
