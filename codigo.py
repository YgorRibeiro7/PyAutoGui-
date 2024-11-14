 # Passo 1,  entrar no sistema da empresa  https://dlp.hashtagtreinamentos.com/python/intensivao/login
 # pip install pyautogui
import pyautogui
import time 
import pandas


pyautogui.PAUSE = 2 #Esse comando faz que a cada comando do pyautogui tenha um intervalo de 1 segundo 

pyautogui.press("win") #aqui ele apertou o botão de windwons 
pyautogui.write("CHROME") #na barra de pesquisa digitou "Google Chrome"
pyautogui.press("enter") #e depois clicou a tecla enter para entrar no navegador



# Passo 2, faze login do sistema 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1) #dar uma pausa de 3 segundo, ou seja, após os comando a cima ele irá ficar dormindo 5s para realizar outro comando
# pyautogui.press("win") 
pyautogui.click(x=819, y=524)
pyautogui.write("ygor@ygor.com")
pyautogui.press("tab")
pyautogui.write("1234@ygor#") 
pyautogui.press("tab")
# pyautogui.click(x=1034 , y=725)
pyautogui.press("enter")
 
 # Passo 3, Importar a base de dados 
tabela = pandas.read_csv("produtos.csv")
print(tabela)
 # Passo 4, Cadastrar 1 produtoCamisa
pyautogui.click(x=698, y=367)

linha = 0

for linha in tabela.index:    

    pyautogui.click(x=698, y=367)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # se essa condição não for vazio,  ela será excutada
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(2000)# numero positivo serve para rolar o mouse para tela de cima 



 # Passo 5, Repedir o processo de cadastro até acabar os produtos ,