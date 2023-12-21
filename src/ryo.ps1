# Includes

. "$PSScriptRoot\modules\install.ps1"
. "$PSScriptRoot\modules\uninstall.ps1"
. "$PSScriptRoot\modules\global.ps1"

# ryo 1.0

function showAbout {
    showLogo

    Write-Host "  +------------------------------------------------+"
    Write-Host "  |                      Ryo                       |"
    Write-Host "  |          Windows Application Installer         |"
    Write-Host "  +------------------------------------------------+"
    Write-Host "  |                OS      : Windows               |"
    Write-Host "  |                Version : 1.0                   |"
    Write-Host "  |                Author  : rap1                  |"
    Write-Host "  +------------------------------------------------+"
    Write-Host ""
    Write-Host "  Description"
    Write-Host ""
    Write-Host "  Ryo is a script write in powershell"
    Write-Host "  with the objetive to be an app installer for windows."
    Write-Host ""
    Write-Host "                      [b] Back"
    Write-Host ""
    Write-Host ""
    $back = Read-Host "  -> Option "
    
    while ($back -ne "b") {
        Write-Host "  [!] Enter a valid value."
        $back = Read-Host "  -> Option "
    }

    menu
}

function ryoExit {
    Write-Host ""
    Write-Host "  [*] Thank you for using ryo."
    Write-Host "  [*] For more info you can always contact me on discord: buaq"
    Write-Host ""
    exit
}

function menu {
    showLogo

    Write-Host ""
    Write-Host ""
    Write-Host "         [1] Install       [2] Uninstall"
    Write-Host ""
    Write-Host "      [a] About ryo script         [q] Exit"
    Write-Host ""
    Write-Host ""

    $option = Read-Host "  [?] Select one option "

    switch ($option) {
        1 {
            Install # go to install.ps1
        }
        2 {
            Uninstall # go to uninstall.ps1
        }
        "q" {
            ryoExit
        }
        "a" {
            showAbout   
        }

        Default {
            Write-Host "  [!] Enter a valid value."
        }
    }
}

function Test-IsRunAsAdmin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Verifica se o terminal foi aberto como Admin ou não
if (-not (Test-IsRunAsAdmin)) {
    Write-Host ""
    Write-Host "  [!] Run the script as Administrator."
    Write-Host ""
    exit
}


# Verify if choco exists
if (-not (Test-Path $chocoPath)) {
    Write-Host ""
    Write-Host "  [!] You need chocolatey to use this program."
    Write-Host ""
}

menu