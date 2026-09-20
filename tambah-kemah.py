# Make kemah/NN-name.html for a camp module and register it in index.html READY.
# Usage: python tambah-kemah.py 35 35-funon "Funon"
import io, re, sys, os

no, base, title = sys.argv[1], sys.argv[2], sys.argv[3]
root = os.path.dirname(os.path.abspath(__file__))
html = f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>#{no} · {title} — Lorong Waktu</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../engine/ui.css">
</head>
<body>
<script type="module">
import camp from './{base}.js';
import {{ runCamp }} from '../engine/shell.js';
runCamp(camp, {{ narrationSrc: '../narasi/{base}.md', audioSrc: '../audio/{base}.mp3', vttSrc: '../narasi/{base}.vtt' }});
</script>
</body>
</html>
'''
io.open(os.path.join(root, 'kemah', base + '.html'), 'w', encoding='utf-8', newline='\n').write(html)

p = os.path.join(root, 'index.html')
s = io.open(p, encoding='utf-8').read()
m = re.search(r"const READY = \{(.*?)\};", s)
entries = dict(re.findall(r"(\w+): '([^']+)'", m.group(1)))
entries[no] = base + '.html'
keys = sorted((k for k in entries if k.isdigit()), key=int) + [k for k in entries if not k.isdigit()]
s = s[:m.start()] + 'const READY = { ' + ', '.join(f"{k}: '{entries[k]}'" for k in keys) + ' };' + s[m.end():]
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', base, len(entries), 'siap')
