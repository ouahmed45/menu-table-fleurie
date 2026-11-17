"""Génère les QR codes pour La Table Fleurie – Pâtisserie & Cafétéria.
Crée le dossier qr-cafeteria/ avec table-01.png à table-20.png et menu-general.png"""
import sys, os, cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

base = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else 'https://menu-table-fleurie.vercel.app/cafeteria'
n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
os.makedirs('qr-cafeteria', exist_ok=True)
enc = cv2.QRCodeEncoder.create()

def get_font(sz, bold=False):
    candidates = [
        'C:/Windows/Fonts/georgia.ttf',
        'C:/Windows/Fonts/arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
        '/System/Library/Fonts/Georgia.ttf'
    ]
    for f in candidates:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, sz)
            except Exception:
                pass
    return ImageFont.load_default()

def create_card(url, title, subtitle, bottom_text, filename):
    # Encodage du QR Code
    q = enc.encode(url)
    q = cv2.copyMakeBorder(q, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=255)
    q = cv2.resize(q, None, fx=9, fy=9, interpolation=cv2.INTER_NEAREST)
    qh, qw = q.shape[:2]

    card_w = max(qw + 140, 520)
    card_h = qh + 380

    im = Image.new('RGB', (card_w, card_h), '#0d0b08')
    d = ImageDraw.Draw(im)

    # Double bordure or décorative
    gold = (201, 160, 99)
    gold_soft = (226, 196, 142)
    muted = (156, 142, 118)

    d.rounded_rectangle([(16, 16), (card_w - 16, card_h - 16)], radius=18, outline=gold, width=2)
    d.rounded_rectangle([(22, 22), (card_w - 22, card_h - 22)], radius=14, outline=(42, 36, 27), width=1)

    # Titre "La Table Fleurie"
    f_title = get_font(42)
    tw = d.textlength("La Table Fleurie", font=f_title)
    d.text(((card_w - tw) / 2, 42), "La Table Fleurie", fill=gold_soft, font=f_title)

    # Sous-titre "PÂTISSERIE & CAFÉTÉRIA"
    f_sub = get_font(18)
    tw = d.textlength(subtitle, font=f_sub)
    d.text(((card_w - tw) / 2, 96), subtitle, fill=gold, font=f_sub)

    # Filet séparateur
    d.line([((card_w - 120) / 2, 126), ((card_w + 120) / 2, 126)], fill=gold, width=1)

    # Placement du QR Code (centré)
    qx = int((card_w - qw) / 2)
    qy = 150
    im.paste(Image.fromarray(q).convert('RGB'), (qx, qy))

    # Badge / Titre de table (ex: Table 1)
    f_badge = get_font(38)
    tw = d.textlength(title, font=f_badge)
    d.text(((card_w - tw) / 2, qy + qh + 24), title, fill=gold_soft, font=f_badge)

    # Instruction en bas
    f_bot = get_font(20)
    tw = d.textlength(bottom_text, font=f_bot)
    d.text(((card_w - tw) / 2, qy + qh + 80), bottom_text, fill=muted, font=f_bot)

    # Sauvegarde
    im.save(filename)

# 1. Génération des QR codes des tables Cafétéria
for t in range(1, n + 1):
    table_url = f'{base}?t={t}'
    create_card(
        url=table_url,
        title=f"Table {t}",
        subtitle="PÂTISSERIE & CAFÉTÉRIA",
        bottom_text="Scannez pour la carte Cafétéria",
        filename=f'qr-cafeteria/table-{t:02d}.png'
    )

# 2. Génération du QR code général Cafétéria
create_card(
    url=base,
    title="Menu Cafétéria",
    subtitle="PÂTISSERIE & CAFÉTÉRIA",
    bottom_text="Scannez pour la carte Cafétéria",
    filename='qr-cafeteria/menu-general.png'
)

print(f"Succès : {n} QR codes Cafétéria + 1 général générés dans le dossier qr-cafeteria/")
print(f"URL de base : {base}")
