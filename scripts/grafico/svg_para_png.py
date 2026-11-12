"""SVG -> PNG fiel (o mesmo render do navegador) via Edge/Chrome headless, escala 2x.
Uso: python svg_para_png.py arquivo.svg [mais.svg ...]   -> grava .png ao lado de cada .svg
Sem dependencia: usa o Edge/Chrome ja instalado. Nada sai da maquina (file://)."""
import os, re, subprocess, sys, tempfile
from pathlib import Path

NAVEGADORES = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
               r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
               r"C:\Program Files\Google\Chrome\Application\chrome.exe",
               "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
               "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"]


def converter(svg, escala=2):
    nav = next((n for n in NAVEGADORES if os.path.exists(n)), None)
    if not nav:
        raise SystemExit("nenhum Edge/Chrome encontrado")
    svg = Path(svg).resolve()
    m = re.search(r'<svg[^>]*\bwidth="([\d.]+)"[^>]*\bheight="([\d.]+)"', svg.read_text(encoding="utf-8"))
    w, h = int(float(m[1])), int(float(m[2]))
    png = svg.with_suffix(".png")
    # pagina HTML 1:1 evita margem/scrollbar que o SVG cru tem na janela headless
    html = Path(tempfile.mkdtemp()) / "p.html"
    html.write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#fff}}'
                    f'img{{display:block}}</style><img src="{svg.as_uri()}" width="{w}" height="{h}">', encoding="utf-8")
    subprocess.run([nav, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    f"--force-device-scale-factor={escala}", f"--window-size={w},{h}",
                    f"--screenshot={png}", html.as_uri()], check=True, capture_output=True, timeout=120)
    return png


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(converter(a))
