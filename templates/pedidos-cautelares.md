# Modelo — peça que pede medida judicial

**Não usar o esqueleto analítico** (`templates/modelo-ipj-instituicao-completo.md`) para este
gênero. Peça que fundamenta pedido de medida judicial (afastamento de sigilo telemático,
quebra de dados de plataforma, interceptação) é organizada **por requisito legal do pedido**,
com o objeto do pedido resumido logo no início — não no fim. Ver `AGENTS.md`/`SKILL.md`,
seção 8, "peça que pede medida judicial", para o detalhe de cada item abaixo.

---

<!-- CABEÇALHO -->
DOCUMENTO [UNIDADE] [XXX]/[AAAA] – INFORMAÇÃO POLICIAL [XX]/[AAAA.NNNNNNN]

## 1. DADOS DO PROCEDIMENTO

[igual à peça analítica]

## 2. CONTEXTO

Senhor Delegado,

[Estado da instrução + autolimitação + "Não obstante" + o que os próximos tópicos vão fazer
— igual à peça analítica.]

## 3. SUMÁRIO

## 4. OBJETO DO PEDIDO — EM UMA PÁGINA

| O que se pede | Alvo | Regime jurídico | Período |
|---|---|---|---|
| [.] | [NOME], CPF/CNPJ [.] | [cadastral / registro de acesso / conteúdo / fluxo em tempo real] | [DD/MM/AAAA] até [.] |

Os poucos fatos que sustentam o pedido, resumidos aqui — o detalhe vem nas seções seguintes.

## 5. CADEIA DE CUSTÓDIA DOS INSUMOS

[Identificação, timestamp e hash de cada arquivo que fundamenta o pedido, no corpo do
texto.]

## 6. A POSIÇÃO DO ALVO NA ESTRUTURA

[Por assimetria medida — volume de mensagens, redes IP distintas, grupos administrados,
contato direto com a ponta — nunca por adjetivo.]

## 7. O OBJETO MATERIAL

[Identificadores exatos do que se pede — chave estável do provedor, não só e-mail/telefone
que o titular troca — e a advertência que invalidaria a requisição se estiver errado.]

## 8. POR QUE ESTA VIA, E POR QUE SÓ ELA

| Via tentada | Resultado |
|---|---|
| [.] | esgotada / negativa / fechada por decisão, com o motivo concreto nomeado |

## 9. FUNDADOS INDÍCIOS

### 9.1. O ilícito investigado

[Tipos penais em jogo, com o lastro fático de cada um — sem esta subseção, o requisito
"fundados indícios da ocorrência do ilícito" fica pela metade.]

### 9.2. Indícios específicos do alvo

[Cada afirmação no grau que a prova sustenta — ver a escada de certeza. "Em tese" obrigatório
para imputação de papel/intenção.]

## 10. UTILIDADE

| O que se pede | A pergunta que responde | Por que só esta fonte |
|---|---|---|
| [.] | [.] | [.] |

## 11. PERÍODO, DELIMITAÇÃO E FUNDAMENTOS

- **Termo inicial:** a data provada pela fonte, sem recuo de precaução — se uma requisição
  anterior de janela recuada provou que nada existe antes de X, o pedido começa em X.
- **Termo final aberto**, se justificado por ciclo medido (o alvo rotaciona a cada N dias),
  nunca por conveniência.

## 12. O QUE SE REQUER

a) [Item], com o **regime jurídico** declarado — cadastral / registro de acesso (com porta de
origem e user agent, não só IP) / conteúdo / fluxo em tempo real;

b) **Preservação imediata** como item próprio — o mais barato e o mais urgente quando o alvo
rotaciona contas;

c) **Item que fecha o universo pelo aparelho** — todos os registros vinculados ao
IMEI/serial, inclusive de contas não nominadas acima.

## 13. PROPORCIONALIDADE, SUBSIDIARIEDADE E SIGILO

[Sigilo justificado por comportamento medido do próprio alvo, nunca por fórmula genérica.]

## 14. O QUE O DEFERIMENTO NÃO PROVARÁ

[No corpo, nunca em rodapé — declarar o limite do que a medida vai efetivamente demonstrar.]

## 15. DILIGÊNCIAS CORRELATAS, PARA O MESMO PASSE

## 16. RESUMO E CONCLUSÃO

---

É o relatório com as informações disponíveis até o momento.

[Cidade]/[UF], [data por extenso].

<br><br>

_____________________________________________
[NOME DO POLICIAL], [FUNÇÃO/UNIDADE]

---

## Notas de qualidade — pontos que decidem o deferimento

- **Achado negativo é fundamento, não campo vazio.** "O alvo não tem conta em plataforma
  alguma" parece falha de diligência quando escrito como lacuna, e vira prova de higiene
  operacional quando escrito como resultado — com a lista do que foi consultado e voltou
  negativo.
- **Separar os regimes jurídicos** dos itens pedidos. Bloco indistinto convida ao
  deferimento parcial pelo menor deles.
- **Nunca fixar uma fórmula de balizamento temporal genérica** ("desde a abertura da conta")
  sem justificar com o dado real do caso — o termo inicial se prova, não se arbitra.
