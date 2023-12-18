# Includes

. "$PSScriptRoot\modules\install.ps1"
. "$PSScriptRoot\modules\uninstall.ps1"
. "$PSScriptRoot\modules\global.ps1"


# ryo 1.0

function installChoco {
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

function menu {
    Write-Host ""
    Write-Host "    +--------------------------------------+"
    Write-Host "    |                                      |"
    Write-Host "    |      ██████╗ ██╗   ██╗ ██████╗       |"
    Write-Host "    |      ██╔══██╗╚██╗ ██╔╝██╔═══██╗      |"
    Write-Host "    |      ██████╔╝ ╚████╔╝ ██║   ██║      |"
    Write-Host "    |      ██╔══██╗  ╚██╔╝  ██║   ██║      |"
    Write-Host "    |      ██║  ██║   ██║   ╚██████╔╝      |"
    Write-Host "    |      ╚═╝  ╚═╝   ╚═╝    ╚═════╝       |"
    Write-Host "    |                                      |"
    Write-Host "    +--------------------------------------+"
    Write-Host ""
    Write-Host "                 Welcome to ryo"
    Write-Host "                    By rap1"
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
            exit
        }

        Default {
            Write-Host "  [!] Enter a valid number."
        }
    }
}

function Test-IsRunAsAdmin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}


# Install choco if dont have
if (-not (Test-Path $chocoPath -PathType Leaf)) {
    installChoco
}

# Verifica se o termianl foi aberto como Admin ou não
if (-not (Test-IsRunAsAdmin)) {
    Write-Host ""
    Write-Host "[!] Run the script as Administrator."
    Write-Host ""
    exit
}

menu