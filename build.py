"""Rebuild both static pages using only Python's standard library."""
from pathlib import Path
import base64
import json

ROOT = Path(__file__).resolve().parent
source = ROOT / 'src'
page = (source / 'page.html').read_text()
style = (source / 'style.css').read_text()
script = (source / 'app.js').read_text() + '\n' + (source / 'practice.js').read_text()
page = page.replace('/*STYLES*/', style).replace('/*SCRIPT*/', script)
(ROOT / 'index.html').write_text(page)
names = ['01-orbite', '02-aree', '03-periodi', '04-struttura-sole', '05-sole-attivo']
assets = ['data:image/svg+xml;base64,' + base64.b64encode((ROOT / 'schede' / (name + '.svg')).read_bytes()).decode() for name in names]
offline = page.replace('<html lang="it">', '<html lang="it" data-offline="true">')
offline = offline.replace('/*SHEET_ASSETS*/null', json.dumps(assets))
pdf = 'schede/Berke_Missione_Cosmo_5_schede.pdf'
offline = offline.replace('href="' + pdf + '"', 'href="data:application/pdf;base64,' + base64.b64encode((ROOT / pdf).read_bytes()).decode() + '"')
(ROOT / 'missione-cosmo-offline.html').write_text(offline)
print('Built index.html and the self-contained offline page.')
