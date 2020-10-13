from SorteioBot import SorteioInstagram

class Home:
    def __init__(self):
        self.escolha = '0'

        self.username = input("Digite seu login do insta: ")
        self.password = input("Digite sua senha do insta: ")

        while self.escolha == '0':
            self.PrintsIniciais()

            if self.escolha == '1':
                print(' ')
                self.sorteio = input("Digite a página do sorteio: ")
                self.bot = SorteioInstagram()
                self.bot.login(self.username, self.password)
                self.bot.SorteioSimples(self.sorteio)

            if self.escolha == '2':
                print(' ')
                self.sorteio = input("Digite a página do sorteio: ")
                self.bot = SorteioInstagram()
                self.bot.login(self.username, self.password)
                self.bot.SorteioDuplo(self.sorteio)
            if self.escolha == '3':
                break

    def PrintsIniciais(self):
        print(' ')
        print("Menu: ")
        print("1 - Sorteios simples (marcar uma só pessoa por comentário)")
        print("2 - Sorteios duplos (marcar duas pessoas por comentário)")
        print("3 - Sair")
        self.escolha = input("digite sua escolha: ")

cod = Home()