from AcessoBd import AcessoBD
from SorteioBot import SorteioInstagram


bd = AcessoBD()
#bd.LimparPessoasMarcaveis()
#print(bd.ReadPessoasExcluidas())

bot = SorteioInstagram()
bot.login("Your mail", "your pass")
bot.SorteioFrases("https://www.instagram.com/p/CEh9S_LBnfP/", "EU QUERO", 1000)












