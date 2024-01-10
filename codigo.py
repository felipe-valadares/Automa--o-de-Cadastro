import pyautogui
import time
import pandas
import numpy
import openpyxl


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'


pyautogui.PAUSE = 1

#Abrir site
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')

# time.sleep(5)

#Login
pyautogui.click(x=1033, y=371)
pyautogui.write('abc2@gmail.com')
pyautogui.press('tab')
pyautogui.write('abc')
pyautogui.press('tab')
pyautogui.press('enter')

# time.sleep(5) 1   

table=pandas.read_csv('produtos.csv')
print(table)

#Cadastro de produtos
for row in table.index:
    #codigo
    pyautogui.click(x=1002, y=261)
    pyautogui.write(table.loc[row, 'codigo'])
    pyautogui.press('tab')

    #marca
    pyautogui.write(table.loc[row, 'marca'])
    pyautogui.press('tab')

    #tipo
    pyautogui.write(table.loc[row, 'tipo'])
    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(table.loc[row, 'categoria']))
    pyautogui.press('tab')

    #preço
    pyautogui.write(str(table.loc[row, 'preco_unitario']))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(table.loc[row, 'custo']))
    pyautogui.press('tab')

    #obs
    obs = (table.loc[row, 'obs'])
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

pyautogui.scroll(5000)
    






