"""Figura de exemplo do padrao (DADOS SINTETICOS): barras ordenadas com estado do dado."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import estilo_forense as ef

DADOS = [  # (rotulo, valor em R$ mil, estado, fonte do dado) -- tudo ficticio
    ("Conta A", 480, "confirmado", "extrato fls. 12-14"),
    ("Conta B", 310, "confirmado", "extrato fls. 15-16"),
    ("Conta C", 220, "inferido", "cruzamento por chave PIX"),
    ("Conta D", 90, "inferido", "cruzamento por chave PIX"),
    ("Conta E", 60, "nao_identificado", "titular nao informado"),
]
COR = ef.OKABE_ITO[0]
W, X0, XB, BH, GAP, Y0 = 900, ef.MARGEM, 190, 26, 22, 130
maxv = max(v for _, v, _, _ in DADOS)
esc = (W - XB - 190) / maxv

corpo = []
for i, (rot, v, est, fonte) in enumerate(DADOS):
    y = Y0 + i * (BH + GAP)
    e = ef.ESTADOS[est]
    fill = COR if est == "confirmado" else (ef.FUNDO if est == "nao_identificado" else COR + "33")
    stroke = ef.NAO_IDENT if est == "nao_identificado" else COR
    wb = v * esc
    corpo.append(ef.t(XB - 10, y + 18, rot, 13, ancora="end"))
    corpo.append(f'<rect x="{XB}" y="{y}" width="{wb:.1f}" height="{BH}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{e["peso"]}" stroke-dasharray="{e["dash"]}"/>')
    corpo.append(ef.t(XB + wb + 8, y + 12, f"R$ {v} mil", 12, "bold"))
    corpo.append(ef.t(XB + wb + 8, y + 24, fonte, 9.5, cor="#4a5364"))  # fonte do dado em cada barra

ytot = Y0 + len(DADOS) * (BH + GAP) + 10
prov = dict(fonte="dados sinteticos de exemplo", folhas="fls. 12-16", dados_sha512=ef.sha512_curto(DADOS),
            data="2026-09-30",
            ressalva="valores inferidos dependem de confirmacao por oficio; barra tracejada nao e prova de titularidade.")
svg = ef.moldura(W, ytot + 70, "Duas contas concentram 68% dos repasses (R$ 790 de 1.160 mil)",
                 "Repasses por conta de destino, em R$ mil (exemplo com dados ficticios)",
                 [("Confirmado", COR, "confirmado"), ("Inferido", COR, "inferido"),
                  ("Nao identificado", COR, "nao_identificado")],
                 "\n".join(corpo), prov, ytot)
out = Path(__file__).with_name("exemplo_figura_barras.svg")
out.write_text(svg, encoding="utf-8")
erros = ef.verificar(out)
print("OK" if not erros else "\n".join(erros), "->", out)
