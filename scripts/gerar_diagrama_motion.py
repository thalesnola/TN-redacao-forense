# Script deterministico para geracao de docs/diagrama-motion.svg
# Compativel 100% com sanitizador do GitHub (SVG Puro sem <filter> e sem style= inline)

import pathlib

SVG_CONTENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 920" width="1000" height="920">
  <defs>
    <!-- Degradê de fundo suave Motion -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F3EEFF"/>
      <stop offset="50%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9F7FF"/>
    </linearGradient>

    <!-- Ambient Glows em SVG Puro (substitui feGaussianBlur compatível com GitHub) -->
    <radialGradient id="glow_pink" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF7AC6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF7AC6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F9BFF" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#2F9BFF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>

    <!-- Motion Trails Diagonais -->
    <linearGradient id="trail_purple" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8A5CF6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#8A5CF6" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#8A5CF6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="trail_blue" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Fundo -->
  <rect width="1000" height="920" fill="url(#bg)"/>

  <!-- Ambient Glows -->
  <circle cx="910" cy="110" r="230" fill="url(#glow_pink)"/>
  <circle cx="90" cy="790" r="250" fill="url(#glow_blue)"/>
  <circle cx="500" cy="330" r="280" fill="url(#glow_purple)"/>

  <!-- Motion Trails Diagonais (-12deg) -->
  <rect x="120" y="80" width="280" height="26" rx="13" fill="url(#trail_purple)" transform="rotate(-12 260 93)"/>
  <rect x="680" y="440" width="260" height="24" rx="12" fill="url(#trail_blue)" transform="rotate(-12 810 452)"/>
  <rect x="60" y="36" width="331.5" height="26" rx="13" fill="#EDE9FE" stroke="#DDD6FE" stroke-width="1"/>
  <text x="225.75" y="53" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#6D28D9" text-anchor="middle" letter-spacing="0.5">METODOLOGIA DE REDAÇÃO · DIAGRAMAS MOTION</text><text x="60" y="86" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="26" font-weight="800" fill="#1B1F3B">TN-redacao-forense · Metodologia e Clareza Jurídica</text><text x="60" y="114" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="500" fill="#4A5568">Regras de redação forense para agentes de IA: peças fluidas, figuras didáticas Motion e zero ruído.</text>
  <rect x="82" y="158" width="370" height="290" rx="18" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="81" y="154" width="370" height="290" rx="18" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="80" y="150" width="370" height="290" rx="18" fill="#FFFFFF" stroke="#FECACA" stroke-width="1.5"/><rect x="96" y="166" width="120" height="20" rx="10" fill="#FEE2E2"/><text x="156" y="180" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#DC2626" text-anchor="middle">ANTES: TEXTO BRUTO</text><text x="96" y="210" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="800" fill="#1B1F3B">Dificuldade para o Leitor Jurídico</text><rect x="96" y="230" width="338" height="42" rx="8" fill="#FFF1F2" stroke="#FECDD3"/><text x="108" y="248" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#991B1B">✕ Jargão Técnico Intransponível</text><text x="108" y="263" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#E11D48">Termos de rede e telecomunicação crus</text><rect x="96" y="280" width="338" height="42" rx="8" fill="#FFF1F2" stroke="#FECDD3"/><text x="108" y="298" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#991B1B">✕ Tabelas Gigantescas Sem Foco</text><text x="108" y="313" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#E11D48">Despejo de 400 linhas sem conclusão</text><rect x="96" y="330" width="338" height="42" rx="8" fill="#FFF1F2" stroke="#FECDD3"/><text x="108" y="348" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#991B1B">✕ Ausência de Elementos Visuais</text><text x="108" y="363" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#E11D48">Páginas densas que cansam magistrados</text><rect x="96" y="380" width="338" height="42" rx="8" fill="#FFF1F2" stroke="#FECDD3"/><text x="108" y="398" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#991B1B">✕ Falta de Hierarquia Narrativa</text><text x="108" y="413" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#E11D48">Fatos misturados fora de cronologia</text>
  <circle cx="500" cy="302" r="28" fill="#1B1F3B" fill-opacity="0.08"/>
  <circle cx="500" cy="295" r="28" fill="#7C3AED" stroke="#6D28D9" stroke-width="2"/><text x="500" y="302" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">→</text>
  <rect x="552" y="158" width="370" height="290" rx="18" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="551" y="154" width="370" height="290" rx="18" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="550" y="150" width="370" height="290" rx="18" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.5"/><rect x="566" y="166" width="130" height="20" rx="10" fill="#DCFCE7"/><text x="631" y="180" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">DEPOIS: REDAÇÃO FORENSE</text><text x="566" y="210" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="800" fill="#1B1F3B">Clareza Imediata para o Julgador</text><rect x="566" y="230" width="338" height="42" rx="8" fill="#F0FDF4" stroke="#BBF7D0"/><text x="578" y="248" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#166534">✓ Tradução Didática Precisa</text><text x="578" y="263" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#15803D">Conceitos complexos explicados com clareza</text><rect x="566" y="280" width="338" height="42" rx="8" fill="#F0FDF4" stroke="#BBF7D0"/><text x="578" y="298" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#166534">✓ Diagramas Motion em SVG</text><text x="578" y="313" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#15803D">Visual limpo no padrão do design motion_v</text><rect x="566" y="330" width="338" height="42" rx="8" fill="#F0FDF4" stroke="#BBF7D0"/><text x="578" y="348" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#166534">✓ Tabelas Sintéticas com Destaque</text><text x="578" y="363" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#15803D">Apenas as linhas e dados que provam o fato</text><rect x="566" y="380" width="338" height="42" rx="8" fill="#F0FDF4" stroke="#BBF7D0"/><text x="578" y="398" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#166534">✓ Rastreabilidade Documental</text><text x="578" y="413" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#15803D">Hashes SHA-256 e folhas exatas indicadas</text>
  <!-- BLOCO DE DEMONSTRAÇÃO PRÁTICA -->
  
  <rect x="62" y="563" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="559" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="555" width="880" height="220" rx="22" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  
  <rect x="80" y="569" width="225" height="24" rx="12" fill="#1B1F3B"/>
  <text x="192" y="585" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="800" fill="#60A5FA" text-anchor="middle" letter-spacing="0.8">DEMONSTRAÇÃO PRÁTICA</text>
  <text x="320" y="586" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#64748B">Fluxo operacional concreto do repositório</text>
  
  <!-- Coluna 1: Entrada -->
  
  <rect x="84" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="83" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="82" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.5"/>
  <rect x="94" y="617" width="90" height="20" rx="10" fill="#EDE9FE"/>
  <text x="139" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#7C3AED" text-anchor="middle">DADO TÉCNICO BRUTO</text>
  <text x="96" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Registro de 500 ERBs</text>
  <text x="96" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="96" dy="0">Extrato bruto com milhares de</tspan><tspan x="96" dy="16">conexões celulares incompreensíveis</tspan><tspan x="96" dy="16">para o leitor não-técnico.</tspan></text>
  
  <!-- Seta 1 -> 2 -->
  <circle cx="359" cy="682.5" r="14" fill="#EDE9FE" stroke="#C4B5FD" stroke-width="1.5"/>
  <text x="359" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#7C3AED" text-anchor="middle">→</text>
  
  <!-- Coluna 2: Processamento -->
  
  <rect x="379" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="378" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="377" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="389" y="617" width="125" height="20" rx="10" fill="#E0F2FE"/>
  <text x="451" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">MÉTODO FORENSE</text>
  <text x="391" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Síntese + Diagrama Motion</text>
  <text x="391" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="391" dy="0">Agente aplica regras de redação,</tspan><tspan x="391" dy="16">isola os 3 marcos temporais-chave e</tspan><tspan x="391" dy="16">gera figura visual em SVG Motion.</tspan></text>
  
  <!-- Seta 2 -> 3 -->
  <circle cx="654" cy="682.5" r="14" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1.5"/>
  <text x="654" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#0284C7" text-anchor="middle">→</text>
  
  <!-- Coluna 3: Saída -->
  
  <rect x="674" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="673" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="672" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="684" y="617" width="105" height="20" rx="10" fill="#DCFCE7"/>
  <text x="736" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">PEÇA JURÍDICA</text>
  <text x="686" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Compreensão Instantânea</text>
  <text x="686" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="686" dy="0">Juiz ou promotor compreende a</tspan><tspan x="686" dy="16">dinâmica em 30 segundos,</tspan><tspan x="686" dy="16">fundamentando decisões rápidas.</tspan></text>
  <!-- Faixa Navy Inferior de Conclusão Técnica -->
  <rect x="60" y="800" width="880" height="64" rx="18" fill="#1B1F3B"/>
  <circle cx="95" cy="832" r="15" fill="#3B82F6" fill-opacity="0.25"/>
  <text x="95" y="837" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="15" font-weight="800" fill="#60A5FA" text-anchor="middle">✓</text>
  <text x="125" y="829" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Comunicação Pericial Elegante e Eficaz</text>
  <text x="125" y="848" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#94A3B8">Transforma dados técnicos em argumentos cristalinos com figuras vetoriais de altíssimo padrão estético.</text>
</svg>'''

def main():
    p = pathlib.Path(__file__).parent.parent / 'docs' / 'diagrama-motion.svg'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(SVG_CONTENT, encoding='utf-8')
    print('SVG gerado em:', p)

if __name__ == '__main__':
    main()
