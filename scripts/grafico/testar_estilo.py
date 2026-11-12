"""Regressao do estilo_forense: rodar apos mexer em estilo_forense.py."""
import hashlib, os, subprocess, sys, tempfile
import estilo_forense as ef

# 1. hash do rodape e deterministico e sensivel ao dado
assert ef.sha512_curto([1, 2]) == ef.sha512_curto([1, 2]) != ef.sha512_curto([1, 3])
# 2. a auditoria PEGA categorias solidas indistinguiveis em cinza
ruim = {"a": ("#e6f4ee", "#009E73", ("", 1.5)), "b": ("#e6f1f9", "#56B4E9", ("", 1.5))}
assert any("cinza" in e for e in ef.verificar_paleta(ruim)), "auditoria nao detectou colapso em cinza"
# 3. ...e deixa passar quando a espessura separa
ok = {"a": ruim["a"][:2] + (("", 3.5),), "b": ruim["b"][:2] + (("", 1.0),)}
assert ef.verificar_paleta(ok) == [], ef.verificar_paleta(ok)
# 4. contraste WCAG: preto/branco = 21
assert round(ef.contraste("#000", "#fff")) == 21
# 5. a figura de exemplo e reproduzivel byte a byte e passa na verificacao
aqui = os.path.dirname(os.path.abspath(__file__))
def gerar():
    subprocess.run([sys.executable, os.path.join(aqui, "exemplo_figura_barras.py")], check=True, capture_output=True)
    return hashlib.sha512(open(os.path.join(aqui, "exemplo_figura_barras.svg"), "rb").read()).hexdigest()
assert gerar() == gerar(), "saida nao deterministica"
assert ef.verificar(os.path.join(aqui, "exemplo_figura_barras.svg")) == []
# 6. rodape final suprime "ver ficha"/ressalva; rascunho mostra tudo
p = dict(fonte="x", folhas="ver ficha", dados_sha512="abc", data="2026-01-01", ressalva="r")
fin, ras = ef.rodape(p, 900, 0)[0], ef.rodape(p, 900, 0, "rascunho")[0]
assert "ver ficha" not in fin and "Ressalva" not in fin and "Fonte: x |" in fin
assert "ver ficha" in ras and "Ressalva: r" in ras
assert "(fls. 1-2)" in ef.rodape(dict(p, folhas="fls. 1-2"), 900, 0)[0]
print("estilo_forense: 6 verificacoes OK")
