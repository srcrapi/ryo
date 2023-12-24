<!-- Header -->

# Ryo

## Ryo é um instalador de aplicativos para fazer uma instalação base, e para os devs uma IDE

<h2 align="center">
    <img src="resources/ryo_image.jpg" alt="app-image">
</h2>

<!-- Information -->

### Idiomas

<p>[ <a href="README.md">English</a> ] [ <a href="README-PT.md">Portuguese</a> ]</p>

### Versão suporte OS

| OS         | ✅  |
| ---------- | --- |
| Windows 11 | ✓   |
| Windows 10 | ✓   |
| Windows 7  | ✓   |

> Não tenho certeza se o Windows 7 funcionará corretamente

<!-- Instructions -->

## Uso

<p>Para ter a certeza que o script vai rodar corretamente porfavor coloque a politica correta.</p>

- RemoteSigned: Deixa rodar os scripts localmente
- Unsigned: Deixa rodar os scripts localmente e os da internet
  > Escolha apenas um.

```powershell
> Set-ExecutionPolicy RemoteSigned
> Set-ExecutionPolicy Unsigned
```

Se tiver a dar algum erro tenta usar este

```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unsigned
```

Clona este repositório para alguma localização que gostares

<p>Adicione a pasta "src" no caminho</p>

- Windows (powershell)

```powershell
> [Environment]::SetEnvironmentVariable("PATH", "$env:PATH;C:\Users\user\path\to\your\folder\src\", [System.EnvironmentVariableTarget]::User)
```

<br>
<p>Este programa ainda está em desenvolvimento e pode conter bugs e mau visual</p>

## Preview

![Preview-1](resources/previews/preview1.png)

![Preview-2](resources/previews/preview2.png)

## Questões e Solicitações

<p>
	Se tiveres alguma questão ou problema apenas abre uma.
	<br>
	<strong>Solicitações são Bem-Vindas!</strong>
</p>

- <a href="https://github.com/srcrapi/ryo/issues">Issues</a>
- <a href="https://github.com/srcrapi/ryo/pulls">Pull Requests</a>

## Todo

- [ ] **Fazer mais opções de instalação**
- [ ] **Fazer categorias de instalação em vês de instalações base**
