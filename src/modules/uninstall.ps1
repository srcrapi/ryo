# Includes

. "$PSScriptRoot\global.ps1"

# Code

function wgUninstall {
    param (
        $package
    )
    
    winget uninstall $package
}

function chocoUninstall {
    param(
        $package
    )

    choco uninstall $package
}

function IDEuninstall {
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
            chocoUninstall "vscode"
            $ide = "VSCode"
        }
        2 {
            chocoUninstall "vscodium"
            $ide = "VSCodium"
        }
        3 {
            chocoUninstall "pycharm-community"
            $ide = "Pycharm"
        }
        4 {
            chocoUninstall "visualstudio2022community"
            $ide = "Visual Studio"
        }

        Default {
            Write-Host "[!] Enter a valid value."
        }
    }

    Write-Host "[!] $ide uninstalled sucessfuly."
}

function uninstallAll {
    param (
        $confirmation
    )

    if ($confirmation -eq "confirmStandard") {
        Write-Host ""
        Write-Host "[*] Select one browser to uninstall:"
        Write-Host ""
        Write-Host "[1] Firefox"
        Write-Host "[2] Vivaldi"
        Write-Host "[3] Chrome"
        Write-Host "[4] Chromium"
        Write-Host "[5] Waterfox"
        Write-Host "[6] Brave"
        Write-Host "[7] OperaGX"
        Write-Host ""
    }

    if ($confirmation -eq "confirmDev") {
        Write-Host ""
        Write-Host "[*] Select one browser:"
        Write-Host ""
        Write-Host "[1] Firefox"
        Write-Host "[2] Vivaldi"
        Write-Host "[3] Chrome"
        Write-Host "[4] Chromium"
        Write-Host "[5] Waterfox"
        Write-Host "[6] Brave"
        Write-Host ""
    }

    $browser_option = Read-Host "-> Option "

    switch ($browser_option) {
        1 {
            chocoUninstall "firefox"
            $browser = "Firefox"
        }
        2 {
            chocoUninstall "vivaldi" 
            $browser = "Vivaldi"
        }
        3 {
            chocoUninstall "googlechrome"
            $browser = "Chrome"
        }
        4 {
            wgUninstall "Hibbiki.Chromium" 
            $browser = "Chromium"
        }
        5 {
            chocoUninstall "waterfox" 
            $browser = "Waterfox"
        }
        6 {
            chocoUninstall "brave" 
            $browser = "Brave"
        }
        7 {
            if ($confirmation -eq "confirmStandard") {
                chocoUninstall "opera-gx" 
                $browser = "OperaGX"
            }
        }

        Default {
            Write-Host "[!] Enter a valid number."
        }
    }

    Write-Host "[!] $browser uninstalled sucessfuly."

    Write-Host "[-] Uninstalling discord..."
    chocoUninstall "discord"
    Write-Host "[!] Discord uninstalled"

    Write-Host "[-] Uninstalling spotify..."
    chocoUninstall "spotify"
    Write-Host "[!] Spotify uninstalled"

    if ($confirmation -eq "confirmStandard") {
        Write-Host "[-] Uninstalling epic games..."
        chocoUninstall "epicgameslauncher"
        Write-Host "[!] Epic Games uninstalled"
        exit
    }

    IDEuninstall
}

function StandardUninstall {
    Write-Host ""
    Write-Host "[*] Do you want to uninstall all(y/n) "
    Write-Host ""

    $uninstallAll_option = Read-Host "-> Option "

    if ($uninstallAll_option.ToLower() -eq "y" -or $uninstallAll_option.ToLower() -eq "yes") {
        uninstallAll "confirmStandard"
        exit
    }

    Write-Host ""
    Write-Host "[*] Select one browser to uninstall:"
    Write-Host ""
    Write-Host "[1] Firefox"
    Write-Host "[2] Vivaldi"
    Write-Host "[3] Chrome"
    Write-Host "[4] Chromium"
    Write-Host "[5] Waterfox"
    Write-Host "[6] Brave"
    Write-Host "[7] OperaGX"
    Write-Host ""

    $browser_option = Read-Host "-> Option "

    switch ($browser_option) {
        1 {
            chocoUninstall "firefox"
            $browser = "Firefox"
        }
        2 {
            chocoUninstall "vivaldi" 
            $browser = "Vivaldi"
        }
        3 {
            chocoUninstall "googlechrome"
            $browser = "Chrome"
        }
        4 {
            wgUninstall "Hibbiki.Chromium" 
            $browser = "Chromium"
        }
        5 {
            chocoUninstall "waterfox" 
            $browser = "Waterfox"
        }
        6 {
            chocoUninstall "brave" 
            $browser = "Brave"
        }
        7 {
            chocoUninstall "opera-gx" 
            $browser = "OperaGX"
        }

        Default {
            Write-Host "[!] Enter a valid number."
        }
    }


    Write-Host "[!] $browser uninstalled sucessfuly."

    if (Test-Path $discordPath) {
        $discord_option = Read-Host "[*] Do you want to uninstall discord(y/n) "
        
        while (
            $discord_option.ToLower() -ne "y" -and 
            $discord_option.ToLower() -ne "yes" -and 
            $discord_option.ToLower() -ne "n" -and 
            $discord_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $discord_option = Read-Host "[*] Do you want to uninstall discord(y/n) "
        }

        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "[+] Uninstalling discord..."
            chocoUninstall "discord"
            Write-Host "[!] Discord uninstalled sucessfuly."
        }
    }
    
    if (Test-Path $epicGamesPath) {
        $epic_option = Read-Host "[*] Do you want to uninstall Epic Games(y/n) "

        while (
            $epic_option.ToLower() -ne "y" -and 
            $epic_option.ToLower() -ne "yes" -and 
            $epic_option.ToLower() -ne "n" -and 
            $epic_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $epic_option = Read-Host "[*] Do you want to uninstall Epic Games(y/n) "  
        }

        if ($epic_option.ToLower() -eq "y" -or $epic_option.ToLower() -eq "yes") {
            Write-Host "[+] Uninstalling epic games..."
            chocoUninstall "epicgameslauncher"
            Write-Host "[!] Epic Games uninstalled sucessfuly."
        }
    }

    if (Test-Path $spotifyPath) {
        $spotify_option = Read-Host "[*] Do you want to uninstall spotify(y/n) "

        while (
            $spotify_option.ToLower() -ne "y" -and
            $spotify_option.ToLower() -ne "yes" -and
            $spotify_option.ToLower() -ne "n" -and
            $spotify_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $spotify_option = Read-Host "[*] Do you want to uninstall spotify(y/n) "
        }

        if ($spotify_option.ToLower() -eq "y" -or $spotify_option.ToLower() -eq "yes") {
            Write-Host "[+] Uninstalling spotify..."
            chocoUninstall "spotify"
            Write-Host "[!] Spotify uninstalled sucessfuly."
        }
    }
}
function DevUninstall {
    Write-Host ""
    Write-Host "[*] Do you want to uninstall all(y/n) "
    Write-Host ""

    $uninstallAll_option = Read-Host "-> Option "

    if ($uninstallAll_option.ToLower() -eq "y" -or $uninstallAll_option.ToLower() -eq "yes") {
        uninstallAll "confirmDev"
        exit
    }

    Write-Host ""
    Write-Host "[*] Select one browser:"
    Write-Host ""
    Write-Host "[1] Firefox"
    Write-Host "[2] Vivaldi"
    Write-Host "[3] Chrome"
    Write-Host "[4] Chromium"
    Write-Host "[5] Waterfox"
    Write-Host "[6] Brave"
    Write-Host ""

    $browser_option = Read-Host "-> Option "

    switch ($browser_option) {
        1 {
            chocoUninstall "firefox"
            $browser = "Firefox"
        }
        2 {
            chocoUninstall "vivaldi" 
            $browser = "Vivaldi"
        }
        3 {
            chocoUninstall "googlechrome"
            $browser = "Chrome"
        }
        4 {
            wgUninstall "Hibbiki.Chromium" 
            $browser = "Chromium"
        }
        5 {
            chocoUninstall "waterfox" 
            $browser = "Waterfox"
        }
        6 {
            chocoUninstall "brave" 
            $browser = "Brave"
        }

        Default {
            Write-Host "[!] Enter a valid number."
        }
    }

    Write-Host "[!] $browser uninstalled sucessfuly."

    if (Test-Path $discordPath) {
        $discord_option = Read-Host "[*] Do you want to uninstall discord(y/n) "
        
        while (
            $discord_option.ToLower() -ne "y" -and 
            $discord_option.ToLower() -ne "yes" -and 
            $discord_option.ToLower() -ne "n" -and 
            $discord_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $discord_option = Read-Host "[*] Do you want to uninstall discord(y/n) "
        }

        if ($discord_option.ToLower() -eq "y" -or $discord_option.ToLower() -eq "yes") {
            Write-Host "[+] Uninstalling discord..."
            chocoUninstall "discord"
            Write-Host "[!] Discord uninstalled sucessfuly."
        }
    }

    if (Test-Path $spotifyPath) {
        $spotify_option = Read-Host "[*] Do you want to uninstall spotify(y/n) "

        while (
            $spotify_option.ToLower() -ne "y" -and
            $spotify_option.ToLower() -ne "yes" -and
            $spotify_option.ToLower() -ne "n" -and
            $spotify_option.ToLower() -ne "no"
        ) {
            Write-Host "[!] Enter a valid option."
            $spotify_option = Read-Host "[*] Do you want to uninstall spotify(y/n) "
        }

        if ($spotify_option.ToLower() -eq "y" -or $spotify_option.ToLower() -eq "yes") {
            Write-Host "[+] Uninstalling spotify..."
            chocoUninstall "spotify"
            Write-Host "[!] Spotify uninstalled sucessfuly."
        }

        IDEuninstall
    }

}

function Uninstall {
    Write-Host ""
    Write-Host "     +-----------------+"
    Write-Host "     |    Uninstall    |"
    Write-Host "     +-----------------+"
    Write-Host ""
    Write-Host "[1] Stantard Uninstallation"
    Write-Host "[2] Dev Uninstallation"
    Write-Host "[3] Back"
    Write-Host ""

    $option = Read-Host "[?] Select one option "

    switch ($option) {
        1 {
            StandardUninstall
        }
        2 {
            DevUninstall
        }
        3 {
            menu
        }

        Default {
            Write-Host "[!] Enter a valid number."
        }
    }
}