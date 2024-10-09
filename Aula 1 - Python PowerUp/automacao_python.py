import pyautogui as pg 
import time as t


#Comando padrão do pyautogui para adicionar um intervalo padrão entre todas as operações
pg.PAUSE = 0.5

#Passo 1: Abrir o navegador 
pg.press("win")
pg.write("Chrome")
pg.press("enter")

#Passo 2: entrar no link do sistema
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")

#Pausa pontual para aumentar a espera do carregamento do site do sistema
t.sleep(6)

#Login com email e senha
#Comando para fazer um click com o mouse - a posição cartesiano pode ser localizado pelo doc auxiliar para printar o position() atual do mouse
pg.click(x=486, y=409)
pg.write("Teste@email.com")

#Tab para avançar nos campos do formulario 
pg.press("tab")
#pg.click(x=527, y=506)
pg.write("senha")
pg.press("enter")

t.sleep(6)

import pandas as pd
#importando a base
tabela = pd.read_csv(r"C:\Users\jhony\Desktop\Hashtag_2024\Projeto1\Aula 1 - Python PowerUp\produtos.csv")


for linha in tabela.index:

    #preenchendo o cadastro
    pg.click(x=433, y=289)


    codigo = tabela.loc[linha, "codigo"]
    pg.write(str(codigo))
    pg.press("tab")

    marca = tabela.loc[linha, "marca"]
    pg.write(str(marca))
    pg.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pg.write(str(tipo))
    pg.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pg.write(str(categoria))
    pg.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pg.write(str(preco_unitario))
    pg.press("tab")

    custo = tabela.loc[linha, "custo"]
    pg.write(str(custo))
    pg.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pg.write(str(obs))
    pg.press("tab")

    pg.press("enter")
    pg.scroll(5000)
