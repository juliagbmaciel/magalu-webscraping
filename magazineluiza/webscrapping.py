from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import connection


cursor = connection.cursor()

class Tvs:
    def __init__(self):
        self.site = 'https://www.magazineluiza.com.br/busca/tv/'
        self.map = {
            'nome':{
                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/h2'
            },
            'valor': {
                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/div[2]/div/p[2]'
            }
        }
        self.driver = webdriver.Chrome()
        self.lista = []
        self.insert_tvs()

    def insert_tvs(self):
        cursor.execute(f"""Delete from tvs""")
        connection.commit()
        self.nomes = []
        self.valores = []
        self.driver.get(self.site)
        sleep(3)
        for i in range(3, 15):
            try:
                sleep(0.3)
                self.valores.append(self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace('%contador%', f'{i}')).text)
                self.nomes.append(self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace('%contador%', f'{i}')).text)
                print("achou")
                try:
                    cursor.execute(f"""INSERT INTO tvs (nome, preco) VALUES ( '{self.nomes[i-3]}', '{self.valores[i-3]}') """)
                    connection.commit()
                    print("adicionou")
                except:
                    print("Não adicionou")
            except:
                try:
                    self.map = {
                        'nome': {
                            'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/h2'
                        },
                        'valor': {
                            'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/div/div/p[2]'
                        }
                    }
                    self.valores.append(
                        self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace('%contador%', f'{i}')).text)
                    self.nomes.append(
                        self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace('%contador%', f'{i}')).text)
                    print("achou except")
                    try:
                        cursor.execute(f"""INSERT INTO tvs (nome, preco) VALUES ( '{self.nomes[i-3]}', '{self.valores[i-3]}') """)
                        connection.commit()
                        print("adicionou except")
                    except:
                        print("Não adicionou except")
                except:
                    print("erro ni")

class Marcas:
    def __init__(self):
        self.site = 'https://www.magazineluiza.com.br/busca/tv+marca/'
        self.map = {
            'nome':{
                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/h2'
            },
            'valor': {
                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/div[2]/div/p[2]'
            }
        }
        self.driver = webdriver.Chrome()
        self.lista = []
        self.insert_brand()

    def insert_brand(self):
        cursor.execute("""delete from samsung;""")
        cursor.execute("""delete from lg;""")
        cursor.execute("""delete from tcl;""")
        cursor.execute("""delete from multilaser;""")
        connection.commit()
        self.brands = ['Samsung', 'LG', 'multilaser', 'tcl']
        self.names = []
        self.price = []
        for brand in self.brands:
            print(f'marca: {brand}')
            self.names.clear()
            self.price.clear()
            self.driver.get(self.site.replace('marca', brand))
            sleep(3)
            for i in range(4, 15):
                try:
                    self.names.append(self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace('%contador%', f'{i}')).text)
                    self.price.append(self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace('%contador%', f'{i}')).text)
                    try:
                        cursor.execute(f"""INSERT INTO {brand} (nome, preco) VALUES ( '{self.names[i-4]}', '{self.price[i-4]}') """)
                        print('adicionando...')
                    except:
                            print(f'erro p inserir, o valor era {self.names[i-4]} EEEEE {self.price[i-4]}')

                except:
                    if brand == 'multilaser' or brand == 'Samsung':
                        self.map = {
                            'nome': {
                                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/h2'
                            },
                            'valor': {
                                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/div/div/p[1]'
                            }
                        }
                        self.names.append(self.driver.find_element(By.XPATH,
                                                                   self.map["nome"]["xpath"].replace('%contador%',
                                                                                                     f'{i}')).text)
                        self.price.append(self.driver.find_element(By.XPATH,
                                                                   self.map["valor"]["xpath"].replace('%contador%',
                                                                                                      f'{i}')).text)
                        print(f'adicionando {brand}...')
                        cursor.execute(
                            f"""INSERT INTO {brand} (nome, preco) VALUES ( '{self.names[i - 4]}', '{self.price[i - 4]}') """)
                    elif brand == 'LG':
                        self.map = {
                            'nome': {
                                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/h2'
                            },
                            'valor': {
                                'xpath': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[%contador%]/a/div[3]/div/div/p[1]'
                            }
                        }
                        self.names.append(self.driver.find_element(By.XPATH,
                                                                   self.map["nome"]["xpath"].replace('%contador%',
                                                                                                     f'{i}')).text)
                        self.price.append(self.driver.find_element(By.XPATH,
                                                                   self.map["valor"]["xpath"].replace('%contador%',
                                                                                                      f'{i}')).text)
                        print(f'adicionando {brand}...')
                        cursor.execute(
                            f"""INSERT INTO {brand} (nome, preco) VALUES ( '{self.names[i - 4]}', '{self.price[i - 4]}') """)
                    else:
                        print("erro pra achar")
            connection.commit()
