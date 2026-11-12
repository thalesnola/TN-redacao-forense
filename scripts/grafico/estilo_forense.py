"""Padrao grafico das pecas (relatorio/editorial): tokens, moldura e rodape de proveniencia.

Trilha PECA: fundo branco, SVG estatico, sem script/CDN/fonte externa, saida deterministica
(nada de data/hora do relogio: a data entra por parametro). Trilha TELA fica fora deste modulo.
Autenticidade = proveniencia visivel na propria figura, nao estetica "feita a mao".
"""
import hashlib
import json
import re
import xml.dom.minidom
from xml.sax.saxutils import escape

# --- tokens -------------------------------------------------------------------------------
FUNDO, TEXTO, PAINEL, BORDA, ARESTA, DESTAQUE = "#fff", "#1a2230", "#f4f6fa", "#d6dbe4", "#c8ccd6", "#e0a52e"
ESCURO = "#4a5364"  # contorno/texto secundario firme
NAO_IDENT = "#8a8f9c"  # contorno proprio: cinza claro some no papel
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9"]  # max 6 categorias
FONTE = "Calibri, 'Segoe UI', Arial, sans-serif"
# estado do dado: nunca so cor (sobrevive a escala de cinza)
ESTADOS = {
    "confirmado": {"dash": "", "peso": 1.5, "rotulo": "Confirmado"},
    "inferido": {"dash": "6 3", "peso": 1.5, "rotulo": "Inferido"},
    "nao_identificado": {"dash": "1.5 3", "peso": 1.5, "rotulo": "Nao identificado"},
}
MARGEM = 30
CHAR_W = 0.56  # largura media do glifo / corpo; estimativa conservadora (sem renderizador)


def _fonte_real():
    """Calibri (a 1a de FONTE) medida com Pillow; None se nao houver -> cai na estimativa."""
    try:
        from PIL import ImageFont
        for d in (r"C:\Windows\Fonts", "/Library/Fonts", "/System/Library/Fonts/Supplemental"):
            for n in ("calibri.ttf", "Calibri.ttf", "Arial.ttf", "arial.ttf"):
                try:
                    return ImageFont.truetype(f"{d}/{n}", 100)
                except OSError:
                    pass
    except ImportError:
        pass
    return None


_FR = _fonte_real()


def largura(txt, corpo):
    """Largura do texto em px: medida real da fonte (escala 100 -> corpo) ou estimativa por glifo."""
    if _FR:
        return _FR.getlength(txt) * corpo / 100
    return len(txt) * corpo * CHAR_W


def quebrar(txt, corpo, max_w):
    linhas, atual = [], ""
    for p in txt.split():
        t = (atual + " " + p).strip()
        if largura(t, corpo) > max_w and atual:
            linhas.append(atual)
            atual = p
        else:
            atual = t
    return linhas + [atual]


def sha512_curto(obj, n=12):
    """Hash do conjunto de dados que gerou a figura (JSON canonico) -> vai no rodape."""
    b = json.dumps(obj, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha512(b).hexdigest()[:n]


def t(x, y, txt, corpo=12, peso="normal", cor=TEXTO, ancora="start"):
    return (f'<text x="{x}" y="{y}" font-size="{corpo}" font-weight="{peso}" fill="{cor}" '
            f'text-anchor="{ancora}">{escape(txt)}</text>')


def legenda(itens, y, x=MARGEM):
    """itens: lista de (rotulo, cor, estado). Faixa no topo, nunca em canto."""
    out, cx = [f'<rect x="{x - 8}" y="{y - 16}" width="{{LW}}" height="26" fill="{PAINEL}" stroke="{BORDA}"/>'], x
    for rot, cor, est in itens:
        e = ESTADOS[est]
        fill = cor if est == "confirmado" else (FUNDO if est == "nao_identificado" else cor + "33")
        stroke = NAO_IDENT if est == "nao_identificado" else cor
        out.append(f'<rect x="{cx}" y="{y - 10}" width="22" height="14" fill="{fill}" stroke="{stroke}" '
                   f'stroke-width="{e["peso"]}" stroke-dasharray="{e["dash"]}"/>')
        out.append(t(cx + 28, y + 1, rot, 11))
        cx += 28 + largura(rot, 11) + 22
    out[0] = out[0].replace("{LW}", str(round(cx - x)))
    return "\n".join(out)


MODO_RODAPE = "final"  # "final" = peca para inserir em relatorio; "rascunho" = conferencia do analista
_PLACEHOLDER = re.compile(r"^\s*(ver ficha|a definir|pendente|n/?d|-+)?\s*$", re.I)


def rodape(prov, W, y, modo=None):
    """prov: dict fonte, folhas, dados_sha512, data, ressalva. Retorna (svg, altura).
    modo "final" (padrao): rodape enxuto -- Fonte | SHA512 | data. Suprime as observacoes de
    trabalho: folhas placeholder ("ver ficha"), e a linha de ressalva (a ressalva da peca vai no
    texto, na autolimitacao). modo "rascunho": mostra tudo, para o analista conferir."""
    modo = modo or MODO_RODAPE
    # Regra do repo redacao-forense: peca nao menciona script/prompt de geracao. Script e versao
    # NAO vao no rodape (prov["script"], se existir, e ignorado aqui): vao ao manifesto SHA512.
    folhas = prov.get("folhas", "")
    fol = "" if (modo == "final" and _PLACEHOLDER.match(folhas)) else (f' ({folhas})' if folhas else "")
    linha1 = (f'Fonte: {prov["fonte"]}{fol} | SHA512 dos dados: {prov["dados_sha512"]}... | '
              f'Elaborado em {prov["data"]}')
    corpo, max_w = 9.5, W - 2 * MARGEM
    linhas = quebrar(linha1, corpo, max_w)
    if modo != "final" and prov.get("ressalva"):
        linhas += quebrar("Ressalva: " + prov["ressalva"], corpo, max_w)
    out = [f'<line x1="{MARGEM}" y1="{y}" x2="{W - MARGEM}" y2="{y}" stroke="{BORDA}"/>']
    for i, l in enumerate(linhas):
        out.append(t(MARGEM, y + 16 + i * 13, l, corpo, cor="#4a5364"))
    return "\n".join(out), 16 + len(linhas) * 13 + 8


def moldura(W, H, titulo, subtitulo, leg_itens, corpo_svg, prov, rodape_y):
    """Titulo-tese (afirma a conclusao), subtitulo (escopo), legenda, corpo, rodape de proveniencia."""
    rod, _ = rodape(prov, W, rodape_y)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'font-family="{FONTE}">\n<rect width="{W}" height="{H}" fill="{FUNDO}"/>\n'
            + t(MARGEM, 42, titulo, 20, "bold") + "\n" + t(MARGEM, 62, subtitulo, 12, cor="#4a5364") + "\n"
            + legenda(leg_itens, 92) + "\n" + corpo_svg + "\n" + rod + "\n</svg>\n")


# --- verificacao (obrigatoria antes de entregar) ----------------------------------------------
def verificar(svg_path, folga=0.10):
    """XML bem formado + todo <text> cabe na largura da peca com 10% de folga (estimativa)."""
    src = open(svg_path, encoding="utf-8").read()
    xml.dom.minidom.parseString(src)
    W = float(re.search(r'viewBox="0 0 (\d+)', src).group(1))
    erros = []
    for m in re.finditer(r'<text x="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*text-anchor="(\w+)">([^<]*)</text>', src):
        x, corpo, anc, txt = float(m[1]), float(m[2]), m[3], m[4]
        w = largura(txt, corpo) * (1 + folga)
        ini = x if anc == "start" else (x - w if anc == "end" else x - w / 2)
        if ini < 0 or ini + w > W - MARGEM / 2:
            erros.append(f"vaza: {txt[:40]!r} ate x={ini + w:.0f} (limite {W - MARGEM / 2:.0f})")
    return erros


# --- acessibilidade: escala de cinza e daltonismo (fase 3) --------------------------------------
_MACHADO = {  # Machado et al. 2009, severidade 1.0, em RGB linear
    "protanopia": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "deuteranopia": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "tritanopia": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _rgb(hexa):
    h = hexa.lstrip("#")
    h = "".join(c * 2 for c in h) if len(h) == 3 else h
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def _lab(rgb_lin):
    r, g, b = rgb_lin
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda v: v ** (1 / 3) if v > 0.008856 else 7.787 * v + 16 / 116
    return 116 * f(y) - 16, 500 * (f(x) - f(y)), 200 * (f(y) - f(z))


def _simular(hexa, modo):
    lin = [_lin(c) for c in _rgb(hexa)]
    if modo == "cinza":
        y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
        return [y, y, y]
    m = _MACHADO[modo]
    return [max(0.0, min(1.0, sum(m[i][j] * lin[j] for j in range(3)))) for i in range(3)]


def delta_e(a, b, modo):
    la, lb = _lab(_simular(a, modo)), _lab(_simular(b, modo))
    return sum((p - q) ** 2 for p, q in zip(la, lb)) ** 0.5


def contraste(fg, bg):
    """Razao de contraste WCAG entre duas cores hex (texto normal exige >= 4,5)."""
    y = lambda h: sum(w * _lin(c) for w, c in zip((0.2126, 0.7152, 0.0722), _rgb(h)))
    a, b = sorted((y(fg), y(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def verificar_paleta(estilos, texto=TEXTO, de_min=20):
    """estilos: {nome: (preenchimento_hex6, contorno_hex6, dash)}. Devolve lista de problemas.
    Par de categorias passa se o traco (dash) difere OU o contorno separa (delta E >= de_min) em
    cinza, protanopia, deuteranopia e tritanopia. Texto sobre cada preenchimento: WCAG >= 4,5."""
    erros, nomes = [], list(estilos)
    for i, a in enumerate(nomes):
        for b in nomes[i + 1:]:
            (fa, sa, da), (fb, sb, db) = estilos[a], estilos[b]
            if da != db:
                continue
            for modo in ("cinza", *_MACHADO):
                de = delta_e(sa, sb, modo)
                if de < de_min:
                    erros.append(f"{a} x {b}: mesmo traco e contorno confunde em {modo} (dE={de:.0f})")
    for n, (f, _, _) in estilos.items():
        c = contraste(texto, f)
        if c < 4.5:
            erros.append(f"{n}: contraste do texto {c:.1f} < 4,5")
    return erros
