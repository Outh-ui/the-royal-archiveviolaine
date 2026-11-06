#!/usr/bin/env python3
"""Build a gallery index from images uploaded to designated folders."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets' / 'gallery-uploads'
CHARACTERS = ['vincent', 'violaine', 'simon', 'evelyn', 'thea', 'lowen', 'charlotte', 'nilan', 'brennan', 'sylvia', 'vince', 'rosalinda', 'malvira']
MOMENTS = ['couple', 'evelyn-simon', 'family', 'other']
EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'}
def images(folder):
    if not folder.exists(): return []
    return [f.relative_to(ROOT).as_posix() for f in sorted(folder.iterdir(), key=lambda f: f.name.casefold()) if f.is_file() and f.suffix.lower() in EXTENSIONS]
manifest = {'characters': {k: images(BASE/'characters'/k) for k in CHARACTERS}, 'moments': {k: images(BASE/'moments'/k) for k in MOMENTS}}
(ROOT/'assets'/'gallery-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Gallery manifest built:', sum(map(len,manifest['characters'].values())), 'character photos,', sum(map(len,manifest['moments'].values())), 'moment photos')
