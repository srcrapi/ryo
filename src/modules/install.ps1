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

    $chose = Read-Host "  [*] Do you want to go back to the menu(y/n) "

    while (
        $chose.ToLower() -ne "y" -and
        $chose.ToLower() -ne "yes" -and
        $chose.ToLower() -ne "n" -and
        $chose.ToLower() -ne "no"
    ) {
        Write-Host "  [!] Enter a valid value."
        $chose = Read-Host "  [*] Do you want to go back to the menu(y/n) "
    }

    if ($chose.ToLower() -eq "y" -or $chose.ToLower() -eq "yes") {
        menu
    }

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
        $discord_option = Read-Host "  [*] Do you want to uninstall discord(y/n) "
        
        while (
            $discord_option.ToLower() -ne "y" -and 
            $discord_option.ToLower() -ne "yes" -and 
            $discord_option.ToLower() -ne "n" -and 
            $discord_option.ToLower() -ne "no"
        ) {
            Write-Host "  [!] Enter a valid option."
            $discord_option = Read-Host "  [*] Do you want to install discord(y/n) "
        }

        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "  [+] Installing discord..."
            chocoInstall "discord"
            Write-Host "  [!] Discord installed sucessfuly."
        }
    }
    
    if (-not (Test-Path $epicGamesPath)) {
        $epic_option = Read-Host "  [*] Do you want to install Epic Games(y/n) "
        
        while (
            $epic_option.ToLower() -ne "y" -and 
            $epic_option.ToLower() -ne "yes" -and 
            $epic_option.ToLower() -ne "n" -and 
            $epic_option.ToLower() -ne "no"
        ) {
            Write-Host "  [!] Enter a valid option."
            $epic_option = Read-Host "  [*] Do you want to install Epic Games(y/n) "
        }

        if ($epic_option.ToLower() -eq "y" -or $epic_option.ToLower() -eq "yes") {
            Write-Host "  [+] Installing epic games..."
            chocoInstall "epicgameslauncher"
            Write-Host "  [!] Epic Games installed sucessfuly."
        }
    }

    if (-not (Test-Path $spotifyPath)) {
        $spotify_option = Read-Host "  [*] Do you want to install spotify(y/n) "
        
        while (
            $spotify_option.ToLower() -ne "y" -and 
            $spotify_option.ToLower() -ne "yes" -and 
            $spotify_option.ToLower() -ne "n" -and 
            $spotify_option.ToLower() -ne "no"
        ) {
            Write-Host "  [!] Enter a valid option."
            $spotify_option = Read-Host "  [*] Do you want to install spotify(y/n) "
        }

        if ($spotify_option.ToLower() -eq "y" -or $spotify_option.ToLower() -eq "yes") {
            Write-Host "  [+] Installing spotify..."
            chocoInstall "spotify"
            Write-Host "  [!] Spotify installed sucessfuly."
        }
    }

    Write-Host "  [*] All the programs are installed."

    $chose = Read-Host "  [*] Do you want to go back to the menu(y/n) "

    while (
        $chose.ToLower() -ne "y" -and
        $chose.ToLower() -ne "yes" -and
        $chose.ToLower() -ne "n" -and
        $chose.ToLower() -ne "no"
    ) {
        Write-Host "  [!] Enter a valid value."
        $chose = Read-Host "  [*] Do you want to go back to the menu(y/n) "
    }

    if ($chose.ToLower() -eq "y" -or $chose.ToLower() -eq "yes") {
        menu
    }

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
        $discord_option = Read-Host "  [*] Do you want to install discord(y/n) "
    
        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "  [+] Installing discord..."
            chocoInstall "discord"
            Write-Host "  [!] Discord installed sucessfuly."
        }
    }

    if (-not (Test-Path $spotifyPath)) {
        Write-Host "  [+] Installing spotify..."
        chocoInstall "spotify"
        Write-Host "  [!] Spotify installed sucessfuly."
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