from AcessoBd import AcessoBD

class ExcluirPessoa:
    def __init__(self):
        escolha = 0
        bd = AcessoBD()
        while escolha == 0:
            escolha = int(input("Digite 1 para excluir pessoa ou 2 para sair: "))
            if escolha == 1:
                nome = input("Digite o nome da pessoa/conta: ")
                bd.AddPessoaExcluida('@' + nome)
                escolha = 0

classe = ExcluirPessoa()