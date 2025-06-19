import pyautogui
import time

# pyautogui.click -> clicar em algum lugar 
# pyautogui.press -> apretar uma tecla
# pyautogui.write -> escrever um txt

pyautogui.PAUSE = 0.5

# paso 1: entrar no sistema da empresa 
# abrir chrome 
pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(2)

# seleçao do usuario
pyautogui.click(x=431, y=544)

# digitar o site https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# paso 2: fazer login 
pyautogui.click(x=683, y=375)
pyautogui.write("aguantechaca@gmail.com")

# prencher a senha 
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# paso 3: importar base de datos 

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# paso 4: cadastrar 1 produto

for linha in tabela.index: # para cada linha da minha tabela 

    pyautogui.click(x=475, y=259)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar ao proximo campo 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # passar ao proximo campo 
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar ao proximo campo 
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar ao proximo campo 
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar ao proximo campo 
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar ao proximo campo 
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)


    pyautogui.press("tab") # passar ao proximo campo 
    pyautogui.press("enter")

    # voltar no inicio
    pyautogui.scroll(1000000)


# paso 5: repetir para todos os produtos

