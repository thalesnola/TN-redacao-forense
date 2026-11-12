#!/usr/bin/env python3
"""
Instalador e validador universal de redacao forense para agentes de codigo.
Suporta Antigravity, Claude Code, Cursor, Windsurf, GitHub Copilot, OpenCode e Codex.
"""

import os
import sys
import shutil
import argparse
import re
from pathlib import Path

# Console do Windows (cp1252) quebra ao imprimir emoji/caractere fora da tabela --
# reconfigurar para UTF-8 evita UnicodeEncodeError em qualquer print deste script.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def install_skill_dir(dest_skill_dir: Path, label: str) -> None:
    """Copia a skill inteira (SKILL.md + references/), nao so o SKILL.md.

    O SKILL.md referencia references/formulario.md, metodologia-patrimonial.md e
    erros-recorrentes.md por caminho relativo -- copiar so o SKILL.md quebra essas
    referencias no destino.
    """
    root = get_repo_root()
    src = root / "skills" / "redacao-forense"
    dest_skill_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest_skill_dir, dirs_exist_ok=True)
    print(f"[+] {label}: skill instalada em {dest_skill_dir} (SKILL.md + references/)")


def install_global():
    root = get_repo_root()
    home = Path.home()
    print("=== Instalando Redacao Forense nos agentes do sistema ===")

    # 1. Antigravity global
    if (home / ".gemini").exists():
        install_skill_dir(home / ".gemini" / "config" / "skills" / "redacao-forense", "Antigravity")

    # 2. Claude Code global
    if (home / ".claude").exists():
        install_skill_dir(home / ".claude" / "skills" / "redacao-forense", "Claude Code")

    # 3. OpenCode global
    opencode_dir = home / ".config" / "opencode"
    if opencode_dir.exists():
        shutil.copy2(root / "AGENTS.md", opencode_dir / "AGENTS.md")
        print(f"[+] OpenCode: AGENTS.md sincronizado em {opencode_dir}")

    # 4. Codex global: skill em ~/.agents/skills (onde o Codex le skills de usuario).
    # So a skill: o ~/.codex/AGENTS.md e do usuario (regras proprias) e nao e sobrescrito.
    if (home / ".codex").exists() or (home / ".agents").exists():
        install_skill_dir(home / ".agents" / "skills" / "redacao-forense", "Codex")

    print("\nInstalacao global finalizada com sucesso!")


def install_workspace(target_path: Path):
    root = get_repo_root()
    target = target_path.resolve()
    print(f"=== Instalando Redacao Forense no workspace: {target} ===")

    # Cursor
    cursor_rules = target / ".cursor" / "rules"
    cursor_rules.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / ".cursor" / "rules" / "redacao-forense.mdc", cursor_rules / "redacao-forense.mdc")
    shutil.copy2(root / ".cursorrules", target / ".cursorrules")

    # Windsurf
    shutil.copy2(root / ".windsurfrules", target / ".windsurfrules")

    # GitHub Copilot
    github_dir = target / ".github"
    github_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / ".github" / "copilot-instructions.md", github_dir / "copilot-instructions.md")

    # Universal / Claude
    shutil.copy2(root / "CLAUDE.md", target / "CLAUDE.md")
    shutil.copy2(root / "AGENTS.md", target / "AGENTS.md")

    # Skill completa (SKILL.md + references/), para quem le .claude/skills/ no proprio projeto
    install_skill_dir(target / ".claude" / "skills" / "redacao-forense", "Claude Code (workspace)")

    print("[+] Arquivos locais (.cursorrules, .cursor/rules/, .windsurfrules, "
          ".github/copilot-instructions.md, CLAUDE.md, AGENTS.md, .claude/skills/) "
          "criados com sucesso!")
    print("Nota: SYSTEM_PROMPT.md nao e instalado automaticamente -- e para colar manualmente "
          "em chat web ou Modelfile (Ollama), onde nao ha leitura de arquivo do repositorio.")


def check_files(target_dir: Path):
    print(f"=== Varrendo arquivos em busca de artefatos de LLM em: {target_dir} ===")
    # Ranges precisos de emoji decorativo -- deliberadamente SEM o bloco 2600-26FF
    # (Miscellaneous Symbols), que contem "warning sign" (U+26A0, "[AVISO]"), usado
    # de proposito no proprio acervo como marcador de ressalva, nao como emoji
    # decorativo. Inclui 1F780-1F7FF (Geometric Shapes Extended) porque e onde
    # vivem os quadrados coloridos citados como anti-padrao no SKILL.md.
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"  # dingbats
        "\U0001F780-\U0001F7FF"  # geometric shapes extended (quadrados coloridos)
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U0001FA70-\U0001FAFF"
        "]+", flags=re.UNICODE
    )
    # Nomes de arquivo cujo proprio conteudo explica/documenta emoji ou termo
    # fabricado como ANTI-padrao, ou usa marcador de ressalva de proveniencia --
    # nao contam como violacao.
    isentos = ("skill", "readme", "agents", "claude", "rules", "prompt",
               "erros-recorrentes", "formulario", "metodologia-patrimonial")
    termos_fabricados = re.compile(
        r"F[oó]rmula do Cr[ée]dito Descoberto|duto financeiro|cortina de fuma[cç]a",
        re.IGNORECASE,
    )

    issues_found = 0
    for path in target_dir.rglob("*.md"):
        if ".git" in str(path) or "node_modules" in str(path):
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        if not any(rule in path.name.lower() for rule in isentos):
            emojis = emoji_pattern.findall(content)
            if emojis:
                print(f"[!] Emojis detectados em {path.name}: {emojis[:5]}")
                issues_found += len(emojis)

        # Termo fabricado (nao verificado) so e problema fora de contexto de proibicao
        for m in termos_fabricados.finditer(content):
            trecho = content[max(0, m.start() - 40):m.start()].lower()
            if not any(neg in trecho for neg in ("nao usar", "nunca", "não usar")):
                print(f"[!] Termo nao verificado usado sem ressalva em {path.name}: '{m.group(0)}'")
                issues_found += 1

    if issues_found == 0:
        print("[OK] Nenhum emoji ou termo nao verificado encontrado nos documentos varridos.")
    else:
        print(f"[AVISO] Total de {issues_found} potenciais desvios encontrados.")


def main():
    parser = argparse.ArgumentParser(description="Instalador e validador de Redacao Forense")
    parser.add_argument("--global", dest="is_global", action="store_true",
                         help="Instala nas configuracoes globais dos agentes")
    parser.add_argument("--workspace", type=str,
                         help="Instala no workspace de projeto especificado")
    parser.add_argument("--check", type=str, nargs="?", const=".",
                         help="Valida presenca de emojis/termos nao verificados em documentos")

    args = parser.parse_args()
    if args.check:
        check_files(Path(args.check))
    elif args.workspace:
        install_workspace(Path(args.workspace))
    elif args.is_global:
        install_global()
    else:
        install_global()


if __name__ == "__main__":
    main()
