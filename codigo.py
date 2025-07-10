import pyautogui
import time
import pandas
import os

# Configuração de pausa entre comandos do pyautogui
def configurar_pyautogui():
    pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
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

# Passo 2: Fazer login
def fazer_login(email, senha):
    pyautogui.click( x=874, y=471)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)  # Espera a tela carregar

# Passo 3: Importar base de dados
def importar_base_dados(caminho_csv):
    tabela = pandas.read_csv(caminho_csv)
    print(tabela)
    return tabela

# Passo 4: Cadastrar os produtos
def cadastrar_produtos(tabela):
    for linha in tabela.index:
    pyautogui.click(x=475, y=259)  # Clique para iniciar o cadastro
    time.sleep(1)  # Esperar que o campo está ativo
 
    pyautogui.press("tab")

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

if __name__ == "__main__":
    os.chdir(r"C:\Users\nicor\OneDrive\Desktop\Proyectos Nico\copia de projeto hashtag 1")
    configurar_pyautogui()
    abrir_navegador_e_acessar_site()
    fazer_login("aguantechaca@gmail.com", "minhasenhasupersecreta")
    tabela = importar_base_dados("produtos.csv")
    cadastrar_produtos(tabela)

