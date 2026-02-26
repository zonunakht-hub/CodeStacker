# CodeStacker Install Script (Windows PowerShell)
# Usage: iwr -useb https://raw.githubusercontent.com/CoSama-Ai/CodeStacker/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

$Repo = "https://github.com/CoSama-Ai/CodeStacker.git"
$TmpDir = Join-Path $env:TEMP "codestacker-install"

Write-Host ""
Write-Host "📦 Installing CodeStacker..."
Write-Host ""

# Clean up any previous temp install
if (Test-Path $TmpDir) {
    Remove-Item -Recurse -Force $TmpDir
}

# Clone repo to temp
git clone --depth 1 $Repo $TmpDir --quiet

# Copy entry point and system folder to current directory
Copy-Item "$TmpDir\stack.md" .
Copy-Item -Recurse "$TmpDir\.codestacker" .

# Cleanup
Remove-Item -Recurse -Force $TmpDir

Write-Host "✅ CodeStacker installed successfully."
Write-Host ""
Write-Host "Your project now has:"
Write-Host "  stack.md         <- AI entry point (single file in your project root)"
Write-Host "  .codestacker/    <- system files (rules, skills, project tracking)"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Open a chat with your AI assistant"
Write-Host "  2. Say: 'Read stack.md and follow it'"
Write-Host "  3. Run: Mode New Project"
Write-Host ""
Write-Host "  -> codestacker.co for skills, props & workflows"
Write-Host ""
