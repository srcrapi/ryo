# Variables

$global:epicGamesPath = "C:\Program Files (x86)\Epic Games"
$global:discordPath = "$HOME\AppData\Local\Discord"
$global:spotifyPath = "$HOME\AppData\Roaming\Spotify"
$global:chocoPath = "C:\ProgramData\chocolatey\"
$global:browserSelected = $false
$global:ideSelected = $false

# Colors

# funtions

function showLogo {
    Clear-Host

    Write-Host ""
    Write-Host "    +--------------------------------------+"
    Start-Sleep -Seconds 0.1
    Write-Host "    |                                      |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ██████╗ ██╗   ██╗ ██████╗       |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ██╔══██╗╚██╗ ██╔╝██╔═══██╗      |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ██████╔╝ ╚████╔╝ ██║   ██║      |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ██╔══██╗  ╚██╔╝  ██║   ██║      |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ██║  ██║   ██║   ╚██████╔╝      |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |      ╚═╝  ╚═╝   ╚═╝    ╚═════╝       |"
    Start-Sleep -Seconds 0.1
    Write-Host "    |               By rap1                |"
    Start-Sleep -Seconds 0.1
    Write-Host "    +--------------------------------------+"
    Start-Sleep -Seconds 0.1
    Write-Host ""
}