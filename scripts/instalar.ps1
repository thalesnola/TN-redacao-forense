# Script de instalacao e sincronizacao universal de Redacao Forense (Windows PowerShell)
param (
    [switch]$WorkspaceOnly = $false,
    [string]$TargetWorkspace = ""
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Instalador Universal: Redacao Forense para Agentes IA  " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$UserHome = $env:USERPROFILE

function Install-SkillDir {
    param([string]$DestSkillDir, [string]$Label)
    # Copia a skill inteira (SKILL.md + references/), nao so o SKILL.md -- o
    # SKILL.md referencia references/*.md por caminho relativo, e copiar so o
    # arquivo principal quebraria essas referencias no destino.
    $SrcSkillDir = Join-Path $RepoRoot "skills\redacao-forense"
    if (-not (Test-Path $DestSkillDir)) {
        New-Item -ItemType Directory -Path $DestSkillDir -Force | Out-Null
    }
    Copy-Item -Path (Join-Path $SrcSkillDir "*") -Destination $DestSkillDir -Recurse -Force
    Write-Host "    -> $Label`: skill instalada em $DestSkillDir (SKILL.md + references\)" -ForegroundColor Gray
}

# 1. Antigravity Global
$AntigravitySkillDir = Join-Path $UserHome ".gemini\config\skills\redacao-forense"
if (Test-Path (Join-Path $UserHome ".gemini")) {
    Write-Host "[+] Configurando no Google Antigravity / Gemini CLI..." -ForegroundColor Green
    Install-SkillDir -DestSkillDir $AntigravitySkillDir -Label "Antigravity"
}

# 2. Claude Code Global
$ClaudeDir = Join-Path $UserHome ".claude"
if (Test-Path $ClaudeDir) {
    Write-Host "[+] Configurando no Claude Code..." -ForegroundColor Green
    $ClaudeSkillsDir = Join-Path $ClaudeDir "skills\redacao-forense"
    Install-SkillDir -DestSkillDir $ClaudeSkillsDir -Label "Claude Code"
}

# 3. OpenCode Global
$OpenCodeDir = Join-Path $UserHome ".config\opencode"
if (Test-Path $OpenCodeDir) {
    Write-Host "[+] Configurando no OpenCode..." -ForegroundColor Green
    Copy-Item -Path (Join-Path $RepoRoot "AGENTS.md") -Destination (Join-Path $OpenCodeDir "AGENTS.md") -Force
    Write-Host "    -> Regra AGENTS.md sincronizada em: $OpenCodeDir" -ForegroundColor Gray
}

# 3b. Codex Global: so a skill em ~/.agents/skills (o ~/.codex/AGENTS.md e do usuario e nao e sobrescrito)
if ((Test-Path (Join-Path $UserHome ".codex")) -or (Test-Path (Join-Path $UserHome ".agents"))) {
    Write-Host "[+] Configurando no Codex..." -ForegroundColor Green
    Install-SkillDir -DestSkillDir (Join-Path $UserHome ".agents\skills\redacao-forense") -Label "Codex"
}

# 4. Instalacao em workspace local (se especificado ou na pasta atual)
$DestWorkspace = if ($TargetWorkspace) { $TargetWorkspace } elseif ($WorkspaceOnly) { (Get-Location).Path } else { "" }
if ($DestWorkspace -and (Test-Path $DestWorkspace)) {
    Write-Host "[+] Instalando no Workspace: $DestWorkspace..." -ForegroundColor Green

    # Cursor
    $CursorRulesDir = Join-Path $DestWorkspace ".cursor\rules"
    if (-not (Test-Path $CursorRulesDir)) { New-Item -ItemType Directory -Path $CursorRulesDir -Force | Out-Null }
    Copy-Item -Path (Join-Path $RepoRoot ".cursor\rules\redacao-forense.mdc") -Destination (Join-Path $CursorRulesDir "redacao-forense.mdc") -Force
    Copy-Item -Path (Join-Path $RepoRoot ".cursorrules") -Destination (Join-Path $DestWorkspace ".cursorrules") -Force

    # Windsurf
    Copy-Item -Path (Join-Path $RepoRoot ".windsurfrules") -Destination (Join-Path $DestWorkspace ".windsurfrules") -Force

    # GitHub Copilot
    $GithubDir = Join-Path $DestWorkspace ".github"
    if (-not (Test-Path $GithubDir)) { New-Item -ItemType Directory -Path $GithubDir -Force | Out-Null }
    Copy-Item -Path (Join-Path $RepoRoot ".github\copilot-instructions.md") -Destination (Join-Path $GithubDir "copilot-instructions.md") -Force

    # Claude & Universal
    Copy-Item -Path (Join-Path $RepoRoot "CLAUDE.md") -Destination (Join-Path $DestWorkspace "CLAUDE.md") -Force
    Copy-Item -Path (Join-Path $RepoRoot "AGENTS.md") -Destination (Join-Path $DestWorkspace "AGENTS.md") -Force

    # Skill completa, para quem le .claude/skills/ no proprio projeto
    Install-SkillDir -DestSkillDir (Join-Path $DestWorkspace ".claude\skills\redacao-forense") -Label "Claude Code (workspace)"

    Write-Host "    -> Regras locais (.cursorrules, .cursor\rules\, .windsurfrules, .github\copilot-instructions.md, CLAUDE.md, AGENTS.md, .claude\skills\) instaladas com sucesso." -ForegroundColor Gray
    Write-Host "    -> SYSTEM_PROMPT.md nao e copiado automaticamente: e para colar manualmente em chat web ou Modelfile (Ollama)." -ForegroundColor DarkGray
}

Write-Host "`nInstalacao concluida com sucesso!" -ForegroundColor Cyan
