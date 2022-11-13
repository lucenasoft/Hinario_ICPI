import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

argument = {'argumentos':['--incognito','--disable-blink-features=AutomationControlled']}
local = os.getcwd()

titulos = list()  #Aqui sera armazenado todos os usúarios para verificar.
open_txt = open(f'{local}/config/titulos.txt')
read_titulos = open_txt.readlines()
for l in read_titulos:
    titulos.append(l.strip('\n'))

n_hino = 1
n_titulo = 0
open_txt = open(f'{local}/config/hinos/{n_hino}.txt')
read_hino = open_txt.read()
cont = 1


  #  Aqui é definido as configurações do navegador.
def navegador():
    path = 'config/driver'
    chrome_options = Options()
    for x in range(0,len(argument['argumentos'])):
        chrome_options.add_argument(f'{argument["argumentos"][x]}')
    manager = ChromeDriverManager(path=path)
    driver = webdriver.Chrome(service=Service(manager.install()),chrome_options=chrome_options)
    login(driver)

def hinos():  #  Nessa função e feito a leitura do hino pelo txt e salvo em read_hino.
    global n_hino
    global read_hino
    open_txt = open(f'{local}/config/hinos/{n_hino}.txt')
    read_hino = open_txt.read()

  
def login(driver): #  Nessa função é vericado os campos de login e feito o login caso esteja tudo ok.
    driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
    sleep(1)
    login = driver.find_element(By.ID, "id_username")
    login.send_keys("admin")
    password = driver.find_element(By.ID, "id_password")
    password.send_keys("admin")
    password.send_keys(Keys.ENTER)
    sleep(1)
    add_hinos(driver)

def add_hinos(driver):  #  Nessa função há a adição do titulo do hino e o proprio hino em si.
    global n_titulo
    global n_hino
    global cont
    driver.get('http://127.0.0.1:8000/admin/hinario/hino/add/')
    sleep(1)
    titulo_hino = driver.find_element(By.ID, "id_titulo")
    titulo_hino.send_keys(f'{titulos[n_titulo]}')
    hino = driver.find_element(By.TAG_NAME, "textarea")
    hino.send_keys(f'{read_hino}')
    enviar_hino = driver.find_element(By.CLASS_NAME, "default")
    enviar_hino.click()
    n_hino += 1
    n_titulo += 1
    cont += 1
    hinos()

while cont < 501:
    navegador()