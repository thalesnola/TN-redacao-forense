# GitHub Copilot Instructions: Redação Forense e IPJs

Full detail, examples and sourced citations: `AGENTS.md` and `skills/redacao-forense/SKILL.md`.

When drafting, formatting, or reviewing Brazilian Federal Police intelligence reports (IPJs)
and forensic documents:

- The reader is a legal professional, not a technical one: translate every technical term
  into a plain-language sentence right after citing it — don't simplify the content, translate it.
- First person for judgment ("entendemos que", "afirmo"), impersonal for raw data
  ("constata-se que"). Never invert.
- Mandatory upfront self-limitation in the context section, always followed by "Não
  obstante" ("Notwithstanding") and what still holds despite the limitation.
- Certainty ladder: every claim gets the degree the evidence supports (hypothesis → clue →
  reinforcement → demonstration); "em tese" ("in theory") is mandatory for any claim
  imputing crime, role, or intent — never for the raw technical fact itself.
- Asset analysis runs on the DECLARED × OBSERVED/CONFIRMED axis — do not use a fixed
  "Undisclosed Credit Formula" as if it were established terminology.
- Document structure varies by genre: long analytical report ≠ piece requesting a judicial
  measure (one section per legal requirement, the request summarized upfront) ≠ short genres
  (no mandatory greeting). The closing line varies by genre too — never fix a single one.
- Absolute prohibitions: emojis, ASCII-art diagrams, naming the internal police system used
  (keep it generic), correcting or normalizing a literal transcription of the investigated
  person's own words, softening the analysis's stated limitations, meta-text about
  generation scripts/LLMs/prompts in the final document.
- Always check for: subject-verb agreement with a postposed plural subject, missing/wrong
  crase, participle agreement in passive voice — see
  `skills/redacao-forense/references/erros-recorrentes.md`.
