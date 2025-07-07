# 🤖 Automação de Cadastro de Produtos Web

Automatize o cadastro de produtos em sistemas web com eficiência, segurança e escalabilidade! Este projeto utiliza **Python**, **Selenium** e **Pandas** para ler arquivos CSV e inserir dados automaticamente via interface web. Ideal para equipes que lidam com cadastros repetitivos em sistemas internos ou e-commerces.

---

## 🚀 Funcionalidades

✅ Login automático no sistema web  
✅ Leitura de produtos a partir de arquivos CSV  
✅ Preenchimento de formulários com dados reais  
✅ Submissão automática e iterativa de cadastros  
✅ Registro de logs de execução  
✅ Navegação segura entre campos  
✅ Estrutura modular e escalável

---

## 🖥️ Pré-requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver compatível com sua versão do navegador

---
## 🛠️ Como Usar

## Passo 1 Instalação

```bash
git clone https://github.com/seu-usuario/automacao-cadastro-produtos.git
cd automacao-cadastro-produtos 
```
## Passo 2 Configure os clicks acorde ao seu computador com auxiliar.py 

```bash
import pyautogui
import time
time.sleep(4)


x, y = pyautogui.position()
print(f"Posição do mouse: x={x}, y={y}")
```
## Passo 3 Configuração de pausa entre comandos do pyautogui

```bash
def configurar_pyautogui():
    pyautogui.PAUSE = 0.5

  ```
## Passo 4 Entrar no sistema da empresa
```
def abrir_navegador_e_acessar_site():
    # Abrir o navegador Chrome
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(3)  # Espera o Chrome abrir
    # Seleção do usuário (ajuste as coordenadas conforme seu monitor)
    pyautogui.click(x=747, y=720)
    time.sleep(3)  # Espera o Navegador abrir 
    # Digitar o site
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")
    time.sleep(3)  # Espera o site carregar
```

## Passo 5 Fazer login
```
  def fazer_login(email, senha):
      pyautogui.click( x=874, y=471)
      pyautogui.write(email)
      pyautogui.press("tab")
      pyautogui.write(senha)
      pyautogui.press("tab")
      pyautogui.press("enter")
      time.sleep(3)  # Espera a tela carregar
```

## Passo 6 Importar base de dados
```
def importar_base_dados(caminho_csv):
    tabela = pandas.read_csv(caminho_csv)
    print(tabela)
    return tabela
```

## Passo 7 Cadastrar os produtos
```
def cadastrar_produtos(tabela):
    for linha in tabela.index:
        pyautogui.click(x=475, y=259)  # Clique para iniciar o cadastro
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")
        obs = str(tabela.loc[linha, "obs"])
        if obs.lower() != "nan":
            pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")  # Confirmar cadastro
        pyautogui.scroll(1000000)  # Voltar ao início da página (opcional)
```

🧩 Tecnologias Utilizadas

    Python

    Selenium

    Pandas

    python-dotenv

    ChromeDriver
    



---

## 👤 Sobre mim

Me chamo Nicolás, e sou apaixonado por análise de dados e machine learning.  
Conecte-se comigo no LinkedIn clicando no botão abaixo! 👇

<p align="center">
  📬 Me adicione no <a href="https://www.linkedin.com/in/nicol%C3%A1s-rivarola-011223176/" target="_blank">LinkedIn</a> !
</p>


---


⚠️ Avisos
Este script simula ações humanas em páginas web. Certifique-se de que o uso está de acordo com as políticas da plataforma alvo.

Não compartilhe arquivos .env com informações sensíveis.



Este script simula ações humanas em páginas web. Certifique-se de que o uso está de acordo com as políticas da plataforma alvo.

Não compartilhe arquivos .env com informações sensíveis.


