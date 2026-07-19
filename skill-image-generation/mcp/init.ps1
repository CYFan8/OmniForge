# MCP Image Generation Bridge Initialization Script
# Installs dependencies and checks all tool connections
Write-Host "=== Image Generation MCP Initialization ===" -ForegroundColor Cyan

# Check Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "[FAIL] Python not found. Install Python 3.10+ from python.org" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Python: $(python --version)" -ForegroundColor Green

# Install dependencies
Write-Host "`nInstalling Python dependencies..." -ForegroundColor Yellow
$packages = @("pywin32", "requests", "Pillow", "watchdog")
foreach ($pkg in $packages) {
    Write-Host "  Installing $pkg..."
    python -m pip install $pkg -q 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] $pkg" -ForegroundColor Green
    } else {
        Write-Host "  [WARN] $pkg failed (may be optional)" -ForegroundColor Yellow
    }
}

Write-Host "`n=== Running MCP Router Init ===" -ForegroundColor Cyan
$mcpDir = "$PSScriptRoot"
python "$mcpDir\router.py" init
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[OK] MCP initialization complete" -ForegroundColor Green
} else {
    Write-Host "`n[WARN] Some bridges are not available (this is normal if tools aren't installed)" -ForegroundColor Yellow
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Photoshop: Check with 'python router.py status'" -ForegroundColor White
Write-Host "Stable Diffusion: Start with 'python launch.py --api' then check" -ForegroundColor White
Write-Host "SAI: Always available (filesystem-based)" -ForegroundColor White
Write-Host "Krita: Available when Krita is installed" -ForegroundColor White
Write-Host "`nAll bridge scripts in: $mcpDir" -ForegroundColor White