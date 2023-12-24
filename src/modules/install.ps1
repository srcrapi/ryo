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

function install_package {
    param(
        $package
    )

    switch ($package) {
        "discord" {
            $package_name = "Discord"
        }
        "epicgameslauncher" {
            $package_name = "Epic Games"
        }
        "spotify" {
            $package_name = "Spotify"
        }
    }

    $option = Read-Host "  [*] Do you want to install $package_name? (y/n) "
        
    while (
        $option.ToLower() -ne "y" -and 
        $option.ToLower() -ne "yes" -and 
        $option.ToLower() -ne "n" -and 
        $option.ToLower() -ne "no"
    ) {
        Write-Host "  [!] Enter a valid option."
        $option = Read-Host "  [*] Do you want to install $package_name? (y/n) "
    }

    if ($option.ToLower() -eq "y" -or $option.ToLower() -eq "yes") {
        Write-Host "  [+] Installing $package_name..."
        chocoInstall $package
        Write-Host "  [!] $package_name installed sucessfuly."
    }
}

function IDEinstall {
    Write-Host ""
    Write-Host "  [*] Select one IDE:"
    Write-Host ""
    Write-Host "           [1] Visual Studio Code"
    Write-Host "           [2] VSCodium"
    Write-Host "           [3] Pycharm"
    Write-Host "           [4] Visual Studio"
    Write-Host "          --------------------"
    Write-Host "           [b] Back"
    Write-Host ""

    $ide_option = Read-Host "  -> Option "

    while (-not ($ideSelected)) {
        switch ($ide_option) {
            1 {
                chocoInstall "vscode"
                $ide = "VSCode"
                $ideSelected = $true
            }
            2 {
                chocoInstall "vscodium"
                $ide = "VSCodium"
                $ideSelected = $true
            }
            3 {
                chocoInstall "pycharm-community"
                $ide = "Pycharm"
                $ideSelected = $true
            }
            4 {
                chocoInstall "visualstudio2022community"
                $ide = "Visual Studio"
                $ideSelected = $true
            }
            "b" {
                Install
            }
    
            Default {
                Write-Host "  [!] Enter a valid value."
                $ide_option = Read-Host "  -> Option "
            }
        }
    }

    Write-Host ""
    Write-Host "  [!] $ide installed sucessfuly."

    Write-Host "  [*] All the programs are installed."

    exit
}

function StandardInstall {
    Write-Host ""
    Write-Host "  [*] Select one browser:"
    Write-Host ""
    Write-Host "           [1] Firefox"
    Write-Host "           [2] Vivaldi"
    Write-Host "           [3] Chrome"
    Write-Host "           [4] Chromium"
    Write-Host "           [5] Waterfox"
    Write-Host "           [6] Brave"
    Write-Host "           [7] OperaGX"
    Write-Host "          ----------------"
    Write-Host "           [b] Back"
    Write-Host ""
    
    $browser_option = Read-Host "  -> Option "

    while (-not $browserSelected) {
        switch ($browser_option) {
            1 {
                chocoInstall "firefox"
                $browser = "Firefox"
                $browserSelected = $true
            }
            2 {
                chocoInstall "vivaldi" 
                $browser = "Vivaldi"
                $browserSelected = $true
            }
            3 {
                chocoInstall "googlechrome"
                $browser = "Chrome"
                $browserSelected = $true
            }
            4 {
                wgInstall "Hibbiki.Chromium" 
                $browser = "Chromium"
                $browserSelected = $true
            }
            5 {
                chocoInstall "waterfox" 
                $browser = "Waterfox"
                $browserSelected = $true
            }
            6 {
                chocoInstall "brave" 
                $browser = "Brave"
                $browserSelected = $true
            }
            7 {
                chocoInstall "opera-gx" 
                $browser = "OperaGX"
                $browserSelected = $true
            }
            "b" {
                Install
            }
            
            Default {
                Write-Host "  [!] Enter a valid value."
                $browser_option = Read-Host "  -> Option "
            }
        }
    }

    Write-Host ""
    Write-Host "  [!] $browser installed sucessfuly."

    if (-not (Test-Path $discordPath)) {
        install_package "discord"
    }
    
    if (-not (Test-Path $epicGamesPath)) {
        install_package "epicgameslauncher"
    }

    if (-not (Test-Path $spotifyPath)) {
        install_package "spotify"
    }

    Write-Host "  [*] All the programs are installed."

    exit
}
function DevInstall {
    Write-Host ""
    Write-Host "  [*] Select one browser:"
    Write-Host ""
    Write-Host "           [1] Firefox"
    Write-Host "           [2] Vivaldi"
    Write-Host "           [3] Chrome"
    Write-Host "           [4] Chromium"
    Write-Host "           [5] Waterfox"
    Write-Host "           [6] Brave"
    Write-Host "           [7] Tor"
    Write-Host "          ----------------"
    Write-Host "           [b] Back"
    Write-Host ""
    
    $browser_option = Read-Host "  -> Option "

    while (-not ($browserSelected)) {
        switch ($browser_option) {
            1 {
                chocoInstall "firefox"
                $browser = "Firefox"
                $browserSelected = $true
            }
            2 {
                chocoInstall "Vivaldi" 
                $browser = "Vivaldi"
                $browserSelected = $true
            }
            3 {
                chocoInstall "googlechrome"
                $browser = "Chrome"
                $browserSelected = $true
            }
            4 {
                wgInstall "Hibbiki.Chromium" 
                $browser = "Chromium"
                $browserSelected = $true
            }
            5 {
                chocoInstall "waterfox" 
                $browser = "Waterfox"
                $browserSelected = $true
            }
            6 {
                chocoInstall "brave" 
                $browser = "Brave"
                $browserSelected = $true
            }
            7 {
                wgInstall "TorProject.TorBrowser"
                $browser = "Tor"
                $browserSelected = $true
            }
            "b" {
                Install
            }
    
            Default {
                Write-Host "  [!] Enter a valid number."
                $browser_option = Read-Host "  -> Option "
            }
        }
    }

    Write-Host ""
    Write-Host "  [!] $browser installed sucessfuly."

    if (-not (Test-Path $discordPath)) {
        install_package "discord"
    }

    if (-not (Test-Path $spotifyPath)) {
        install_package "spotify"
    }

    IDEinstall
}

function Install {
    showLogo

    Write-Host ""
    Write-Host "                  +---------------+" 
    Write-Host "                  |    Install    |"
    Write-Host "                  +---------------+"
    Write-Host ""
    Write-Host "  [1] Stantard Installation     [2] Dev Installation"
    Write-Host ""
    Write-Host "                      [b] Back"
    Write-Host ""
    Write-Host ""
    
    $option = Read-Host "  [?] Select one option "
    
    while ($true) {
        switch ($option) {
            1 {
                StandardInstall
            }
            2 {
                DevInstall
            }
            "b" {
                menu
            }
            
            Default {
                Write-Host "  [!] Enter a valid number."
                $option = Read-Host "  [?] Select one option "
            }
        }
    }
}