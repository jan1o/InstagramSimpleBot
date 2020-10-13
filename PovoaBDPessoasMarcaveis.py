from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from AcessoBd import AcessoBD

class PovoaPessoasMarcaveis:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Geckodriver\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)

        # Para digitar no campo 'login'
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)

        # Para digitar no campo 'senha'
        pass_element = driver.find_element_by_xpath("//input[@name='password']")
        pass_element.clear()
        pass_element.send_keys(self.password)

        pass_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.Povoar()

    def Povoar(self):
        driver = self.driver
        driver.get('https://www.instagram.com/janliucas/')
        time.sleep(2)

        followers = driver.find_element_by_xpath("//a[@href='/janliucas/following/']")
        followers.click()
        time.sleep(2)

        fBody = driver.find_element_by_xpath("//div[@class='isgrP']")
        last_height = driver.execute_script('return arguments[0].scrollHeight', fBody)
        print(last_height)
        while True:
            # Scroll down to bottom
            #driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', fBody)
            # Wait to load page
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script('return arguments[0].scrollHeight', fBody)
            print(new_height)
            if new_height == last_height:
                break
            last_height = new_height

        contas = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")

        nomes = []
        for elem in contas:
            nomes.append('@' + str(elem.get_attribute('title')))

        bd = AcessoBD()
        excluidos = bd.ReadPessoasExcluidas()
        ex = []
        for e in excluidos:
            ex.append(e[0])

        for nome in nomes:
            if nome in ex:
                nomes.remove(nome)


        for nome in nomes:
            bd.AddPessoaMarcavel(nome)





meuBot = PovoaPessoasMarcaveis('deathersheol@gmail.com','deatherinferno')
meuBot.login()