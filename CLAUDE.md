# Diretrizes de redação forense e elaboração de IPJs (Claude Code / Desktop)

Regras completas na skill `skills/redacao-forense/SKILL.md` — leia-a antes de redigir,
estruturar ou revisar qualquer Informação Policial (IPJ), relatório de análise técnica,
parecer ou peça de investigação nesta voz. O resumo abaixo é o que cabe neste arquivo; a
skill e suas `references/` (`formulario.md`, `metodologia-patrimonial.md`,
`erros-recorrentes.md`, `padrao-grafico.md`) têm o detalhe, os exemplos e as citações.

## Regras mandatórias

1. **O leitor é leigo, mesmo quando o conteúdo é técnico.** O destinatário (delegado, MP,
   juízo) domina o direito, não domina perícia, telemática, fiscal ou cripto. Traduzir o
   termo técnico numa frase logo após citá-lo; simular o raciocínio do leigo/vítima em vez
   de só declarar a limitação; usar exemplo hipotético e diagrama em texto antes de aplicar
   o conceito ao caso concreto.
2. **Primeira pessoa no juízo, impessoal no dado.** "Constata-se que..." (dado) convive com
   "entendemos que..." (juízo). Nunca inverter.
3. **Autolimitação antecipada obrigatória, com "Não obstante".** Declarar a fraqueza da
   própria análise antes que alguém a encontre, sempre seguida do que se sustenta apesar
   dela — nunca só a ressalva, nunca só a conclusão.
4. **Metodologia declarada antes do resultado**, em peça longa: regra de cálculo, lacuna
   nomeada e seu efeito no número, conceito definido com fonte, URL e data de acesso.
5. **Cadeia de custódia no corpo do texto** — nome, timestamp, hash de todo arquivo extraído
   de nuvem ou aparelho —, com transcrição literal e comentário do analista em bloco
   separado.
6. **A escada de certeza:** hipótese → indício → reforço → demonstração, cada afirmação no
   grau que a prova sustenta. "Em tese" é obrigatório para imputação de crime/papel/intenção,
   nunca para o dado técnico em si.
7. **Eixo DECLARADO × OBSERVADO/CONSTATADO** em toda análise patrimonial — nunca "Fórmula do
   Crédito Descoberto" como termo fixo; usar os conceitos e o vocabulário efetivamente
   medidos no acervo (`references/metodologia-patrimonial.md`).
8. **Estrutura por gênero, não uma única estrutura para tudo:** peça analítica longa (seção 8
   do SKILL.md) ≠ peça que pede medida judicial (seção por requisito legal, pedido resumido
   no início) ≠ gêneros curtos (informe, status, confirmatória, cadeia de custódia como peça
   inteira — sem saudação obrigatória).
9. **Fecho varia por gênero:** "É a informação." (analítica longa) · "É o relatório."
   (levantamento/amostragem) · "É o que tenho/tinha a informar até o momento." (status) · "É
   o relatório com as informações disponíveis até o momento." (pedido). Nunca fixar um único
   fecho nem uma assinatura de exemplo como se fosse regra.

## Proibições absolutas

- Emoji, negrito decorativo, ASCII art de organograma no corpo da peça final.
- Nomear sistema policial (fica "pesquisas em sistemas"); deixar de nomear órgão público com
  URL e data de acesso.
- Corrigir ou uniformizar transcrição literal de anotação, mensagem ou documento do
  investigado.
- Suavizar ou omitir a limitação da própria análise para a peça parecer mais conclusiva —
  a falha mais grave contra esta voz.
- Meta-texto sobre ferramentas de geração (scripts, LLM, prompt) no documento final.

## Erros gramaticais a nunca deixar passar

Concordância verbal com sujeito posposto plural, crase (ausente antes de feminino / indevida
antes de nome masculino), particípio sem concordância em voz passiva, grafia inconsistente de
estrangeirismo/sigla no mesmo documento. Tabela completa com exemplo e correção em
`skills/redacao-forense/references/erros-recorrentes.md`.

## Comandos úteis do repositório

- Instalar globalmente nos agentes da máquina:
  ```powershell
  powershell -ExecutionPolicy Bypass -File scripts\instalar.ps1
  ```
- Validar se há emojis ou artefatos em arquivos Markdown/Docx:
  ```bash
  python scripts/instalar.py --check
  ```
