
# Check if Redis is installed
if (-Not (Get-Command redis-server -ErrorAction SilentlyContinue)) {
    Write-Host "Redis is not installed. Installing Redis..."

    # Add Redis installation commands for Windows
    # Example: Using chocolatey
    choco install redis-64 -y

    # Set up Redis to run as a service
    New-Service -Name Redis -BinaryPathName "C:\Program Files\Redis\redis-server.exe" -DisplayName "Redis Server" -StartupType Automatic
    Start-Service -Name Redis
} else {
    Write-Host "Redis is already installed."
}

Write-Host "Setup complete. Redis should now be installed and running."
