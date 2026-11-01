# Copy the hackathon-winner skill into the right folders for each tool.
# Usage: ./install.ps1 [-Opencode] [-Codex] [-Claude] [-Global]
param([switch]$Opencode, [switch]$Codex, [switch]$Claude, [switch]$Global)
$src = Join-Path $PSScriptRoot "skills/hackathon-winner"
if (-not (Test-Path (Join-Path $src "SKILL.md"))) { Write-Error "skill source not found at $src"; exit 1 }
if (-not ($Opencode -or $Codex -or $Claude)) { Write-Error "choose at least one of -Opencode -Codex -Claude"; exit 1 }
function Install-To($dest) {
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  $target = Join-Path $dest "hackathon-winner"
  if (Test-Path $target) { Remove-Item -Recurse -Force $target }
  Copy-Item -Recurse -Force $src $target
  Write-Host "installed -> $target"
}
$home_ = [Environment]::GetFolderPath("UserProfile")
if ($Global) {
  if ($Opencode) { Install-To (Join-Path $home_ ".config/opencode/skills") }
  if ($Codex)    { Install-To (Join-Path $home_ ".agents/skills") }
  if ($Claude)   { Install-To (Join-Path $home_ ".claude/skills") }
} else {
  if ($Opencode) { Install-To ".opencode/skills" }
  if ($Codex)    { Install-To ".agents/skills" }
  if ($Claude)   { Install-To ".claude/skills" }
}
Write-Host "done. Restart your agent if the skill does not appear."
