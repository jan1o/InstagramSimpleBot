from AcessoBd import AcessoBD
from SorteioBot import SorteioInstagram


bd = AcessoBD()
#bd.LimparPessoasMarcaveis()
#print(bd.ReadPessoasExcluidas())

bot = SorteioInstagram()
bot.login("janliucas", "deatherinferno")
bot.SorteioFrases("https://www.instagram.com/p/CEh9S_LBnfP/", "EU QUERO", 1000)












