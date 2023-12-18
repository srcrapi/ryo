# Includes

. "$PSScriptRoot\global.ps1"

# Code

function wgInstall {
    param (
        $package
    )
    
    winget install $package
}

function chocoInstall {
    param(
        $package
    )

    choco install $package
}

function IDEinstall {
    Write-Host ""
    Write-Host "[*] Select one IDE:"
    Write-Host ""
    Write-Host "[1] Visual Studio Code"
    Write-Host "[2] VSCodium"
    Write-Host "[3] Pycharm"
    Write-Host "[4] Visual Studio"
    Write-Host ""

    $ide_option = Read-Host "-> Option "

    switch ($ide_option) {
        1 {
            chocoInstall "vscode"
            $ide = "VSCode"
        }
        2 {
            chocoInstall "vscodium"
            $ide = "VSCodium"
        }
        3 {
            chocoInstall "pycharm-community"
            $ide = "Pycharm"
        }
        4 {
            chocoInstall "visualstudio2022community"
            $ide = "Visual Studio"
        }

        Default {
            Write-Host "[!] Enter a valid value."
        }
    }

    Write-Host "[!] $ide installed sucessfuly."
}

function StandardInstall {
    Write-Host ""
    Write-Host "  [*] Select one browser:"
    Write-Host ""
    Write-Host "  [1] Firefox"
    Write-Host "  [2] Vivaldi"
    Write-Host "  [3] Chrome"
    Write-Host "  [4] Chromium"
    Write-Host "  [5] Waterfox"
    Write-Host "  [6] Brave"
    Write-Host "  [7] OperaGX"
    Write-Host ""

    $browser_option = Read-Host "  -> Option "

    switch ($browser_option) {
        1 {
            chocoInstall "firefox"
            $browser = "Firefox"
        }
        2 {
            chocoInstall "vivaldi" 
            $browser = "Vivaldi"
        }
        3 {
            chocoInstall "googlechrome"
            $browser = "Chrome"
        }
        4 {
            wgInstall "Hibbiki.Chromium" 
            $browser = "Chromium"
        }
        5 {
            chocoInstall "waterfox" 
            $browser = "Waterfox"
        }
        6 {
            chocoInstall "brave" 
            $browser = "Brave"
        }
        7 {
            chocoInstall "opera-gx" 
            $browser = "OperaGX"
        }

        Default {
            Write-Host "  [!] Enter a valid number."
        }
    }

    Write-Host "  [!] $browser installed sucessfuly."

    if (-not (Test-Path $discordPath)) {
        $discord_option = Read-Host "[*] Do you want to uninstall discord(y/n) "
        
        while (
            $discord_option.ToLower() -ne "y" -and 
            $discord_option.ToLower() -ne "yes" -and 
            $discord_option.ToLower() -ne "n" -and 
            $discord_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $discord_option = Read-Host "[*] Do you want to install discord(y/n) "
        }

        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "[+] Installing discord..."
            chocoUninstall "discord"
            Write-Host "[!] Discord installed sucessfuly."
        }
    }
    
    if (-not (Test-Path $epicGamesPath)) {
        $epic_option = Read-Host "[*] Do you want to install Epic Games(y/n) "
        
        if ($epic_option.ToLower() -eq "y" -or $epic_option.ToLower() -eq "yes") {
            Write-Host "[+] Installing epic games..."
            wgInstalchocoInstall "epicgameslauncher"
            Write-Host "[!] Epic Games installed sucessfuly."
        }
    }

    if (-not (Test-Path $spotifyPath)) {
        Write-Host "[+] Installing spotify..."
        chocoInstall "spotify"
        Write-Host "[!] Spotify installed sucessfuly."
    }

    Write-Host "[*] All the programs are installed."
}
function DevInstall {
    Write-Host ""
    Write-Host "  [*] Select one browser:"
    Write-Host ""
    Write-Host "  [1] Firefox"
    Write-Host "  [2] Vivaldi"
    Write-Host "  [3] Chrome"
    Write-Host "  [4] Chromium"
    Write-Host "  [5] Waterfox"
    Write-Host "  [6] Brave"
    Write-Host "  [7] Tor"
    Write-Host ""

    $browser_option = Read-Host "-> Option "

    switch ($browser_option) {
        1 {
            chocoInstall "firefox"
            $browser = "Firefox"
        }
        2 {
            chocoInstall "Vivaldi" 
            $browser = "Vivaldi"
        }
        3 {
            chocoInstall "googlechrome"
            $browser = "Chrome"
        }
        4 {
            wgInstall "Hibbiki.Chromium" 
            $browser = "Chromium"
        }
        5 {
            chocoInstall "waterfox" 
            $browser = "Waterfox"
        }
        6 {
            chocoInstall "brave" 
            $browser = "Brave"
        }
        7 {
            wgInstall "TorProject.TorBrowser"
            $browser = "Tor"
        }

        Default {
            Write-Host "[!] Enter a valid number."
        }
    }

    Write-Host "[!] $browser installed sucessfuly."

    if (-not (Test-Path $discordPath)) {
        $discord_option = Read-Host "[*] Do you want to install discord(y/n) "
    
        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "[+] Installing discord..."
            chocoInstall "discord"
            Write-Host "[!] Discord installed sucessfuly."
        }
    }

    if (-not (Test-Path $spotifyPath)) {
        Write-Host "[+] Installing spotify..."
        chocoInstall "spotify"
        Write-Host "[!] Spotify installed sucessfuly."
    }

    IDEinstall
}

function Install {
    Clear-Host

    Write-Host ""
    Write-Host "    +--------------------------------------+"
    Write-Host "    |                                      |"
    Write-Host "    |      ██████╗ ██╗   ██╗ ██████╗       |"
    Write-Host "    |      ██╔══██╗╚██╗ ██╔╝██╔═══██╗      |"
    Write-Host "    |      ██████╔╝ ╚████╔╝ ██║   ██║      |"
    Write-Host "    |      ██╔══██╗  ╚██╔╝  ██║   ██║      |"
    Write-Host "    |      ██║  ██║   ██║   ╚██████╔╝      |"
    Write-Host "    |      ╚═╝  ╚═╝   ╚═╝    ╚═════╝       |"
    Write-Host "    |               By rap1                |"
    Write-Host "    |                                      |"
    Write-Host "    +--------------------------------------+"
    Write-Host ""
    Write-Host ""
    Write-Host "    +---------------+" 
    Write-Host "    |    Install    |"
    Write-Host "    +---------------+"
    Write-Host ""
    Write-Host "  [1] Stantard Installation"
    Write-Host "  [2] Dev Installation"
    Write-Host "  [3] Back"
    Write-Host ""

    $option = Read-Host "  [?] Select one option "

    switch ($option) {
        1 {
            StandardInstall
        }
        2 {
            DevInstall
        }
        3 {
            menu
        }

        Default {
            Write-Host "  [!] Enter a valid number."
        }
    }
}