# Script para gerar o site estilo Netflix em React (Vite)
# Ele cria a estrutura e empacota em um ZIP (appfilmes_web.zip)

import os, shutil, zipfile, textwrap, json

root = "/mnt/data/appfilmes_web"
if os.path.exists(root):
    shutil.rmtree(root)
os.makedirs(root)

def write(path, content):
    full = os.path.join(root, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# Exemplo básico de index.html
write("index.html", textwrap.dedent("""<!doctype html>
<html>
  <head>
    <meta charset='utf-8'/>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'/>
    <title>AppFilmes — Netflix Style</title>
  </head>
  <body>
    <div id='root'></div>
  </body>
</html>
"""))

# Compacta em ZIP
zip_path = "/mnt/data/appfilmes_web.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for foldername, _, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, root)
            z.write(filepath, arcname)

print("ZIP criado em:", zip_path)
