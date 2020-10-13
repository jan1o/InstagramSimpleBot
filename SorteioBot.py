from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from AcessoBd import AcessoBD

class SorteioInstagram:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Geckodriver\geckodriver.exe')

    def login(self, username, password):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)

        #Para digitar no campo 'login'
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(username)

        # Para digitar no campo 'senha'
        pass_element = driver.find_element_by_xpath("//input[@name='password']")
        pass_element.clear()
        pass_element.send_keys(password)

        pass_element.send_keys(Keys.RETURN)
        time.sleep(5)

        # Teste para abrir pagina de sorteio hidromel
        #self.MarcarPessoasSorteio('https://www.instagram.com/p/CEEmRwGAznA/')

    def SorteioSimples(self, sorteio):
        driver = self.driver
        driver.get(sorteio)

        bd = AcessoBD()
        pessoas = bd.ReadPessoasMarcaveis()

        for pessoa in pessoas:
            driver.find_element_by_class_name('Ypffh').click()  #Acha campo de comentario e deixa possivel ser escrito
            coment = driver.find_element_by_class_name('Ypffh') #Passa ele para uma variavel
            time.sleep(random.randint(1, 3))

            for letra in pessoa:
                coment.send_keys(letra)
                time.sleep(random.randint(1, 5)/30)

            time.sleep(random.randint(3, 5))
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(random.randint(2, 4))

    def SorteioDuplo(self, sorteio):
        driver = self.driver
        driver.get(sorteio)

        bd = AcessoBD()
        pessoas = bd.ReadPessoasMarcaveis()

        for i in range(0, len(pessoas), 2):
            driver.find_element_by_class_name('Ypffh').click()  # Acha campo de comentario e deixa possivel ser escrito
            coment = driver.find_element_by_class_name('Ypffh')  # Passa ele para uma variavel
            time.sleep(random.randint(1, 3))

            for letra in pessoas[i]:
                coment.send_keys(letra)
                time.sleep(random.randint(1, 5) / 30)
            coment.send_keys(' ')
            time.sleep(random.randint(1, 5) / 30)

            for letra in pessoas[i+1]:
                coment.send_keys(letra)
                time.sleep(random.randint(1, 5) / 30)

            time.sleep(random.randint(3, 5))
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(random.randint(2, 4))

    def SorteioFrases(self, sorteio, frase, numComents):
        driver = self.driver
        driver.get(sorteio)

        for x in range(0, numComents):
            driver.find_element_by_class_name('Ypffh').click()  # Acha campo de comentario e deixa possivel ser escrito
            coment = driver.find_element_by_class_name('Ypffh')  # Passa ele para uma variavel
            time.sleep(random.randint(1, 3))

            for letra in frase:
                coment.send_keys(letra)
                time.sleep(random.randint(1, 5) / 30)

            time.sleep(random.randint(2, 5))
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(random.randint(2, 4))
            print(x+1)