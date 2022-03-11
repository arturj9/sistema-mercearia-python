import Controller
import os.path
def criarArquivos(*args):
    pasta = 'arquivos-txt'
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    for i in args:
        if not os.path.exists(f'{pasta}/{i}.txt'):
            with open(f'{pasta}/{i}.txt', 'w') as arq:
                arq.write('')
criarArquivos(
    'categoria', 'clientes', 
    'estoque', 'fornecedores', 
    'funcionarios', 'venda')
if __name__ == '__main__':
    while True:
        local = int(input("Digite 1 para acessar (Categorias)\n"
                          "Digite 2 para acessar (Estoque)\n"
                          "Digite 3 para acessar (Fornecedores)\n"
                          "Digite 4 para acessar (Clientes)\n"
                          "Digite 5 para acessar (Funcionários)\n"
                          "Digite 6 para acessar (Vendas)\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"
                          ": "))
        # CATEGORIAS                  
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"
                                    ": "))
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar: ")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover: ")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar: ")
                    novaCategoria = input("Digite a categoria para qual deseja alterar: ")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                elif decidir == 5:
                    break
                else:
                    print("Digite um valor válido.\n")
        # ESTOQUE
        elif local == 2:
            est = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair\n"
                                    ": "))
                if decidir == 1:
                    nome = input("Digite o nome do produto: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = input("Digite a quantidade do produto: ")
                    est.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite o produto que deseja remover: ")
                    est.removerProduto(produto)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do produto que deseja alterar: ")
                    novoNome = input("Digite o novo nome do produto: ")
                    novoPreco = input("Digite o novo preco do produto: ")
                    novaCategoria = input("Digite a nova categoria do produto: ")
                    novaQuantidade = input("Digite a nova quantidade do produto: ")
                    est.alterarProduto(nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    est.mostrarEstoque()
                elif decidir == 5:
                    break
                else:
                    print('Digite um valor válido.\n')
        # FORNECEDORES
        elif local == 3:
            fon = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para sair\n"
                                    ": "))
                if decidir == 1:
                    nome = input("Digite o nome do fornecedor: ")
                    cnpj = input("Digite o cnpj do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    categoria = input("Digite a categoria fornecida: ")
                    fon.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    fornecedor = input('Digite o fornecedor que deseja remover: ')
                    fon.removerFornecedor(fornecedor)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do fornecedor que deseja alterar: ")
                    novoNome = input('Digite o novo nome do fornecedor: ')
                    novoCnpj = input('Digite o novo cnpj do fornecedor: ')
                    novoTelefone = input('Digite o novo telefone do fornecedor: ')
                    novoCategoria = input('Digite a nova categoria fornecida: ')
                    fon.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    fon.mostrarFornecedor()
                elif decidir == 5:
                    break
                else:
                    print('Digite um valor válido.\n')
        # CLIENTES
        elif local == 4:
            cli = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar clientes\n"
                                    "Digite 5 para sair\n"
                                    ": "))
                if decidir == 1:
                    nome = input("Digite o nome do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    cpf = input("Digite o CPF do cliente: ")
                    email = input("Digite o E-mail do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    cli.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    cliente = input("Digite o cliente que deseja remover: ")
                    cli.removerCliente(cliente)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar: ")
                    novoNome = input("Digite o novo nome do cliente: ")
                    novoTelefone = input("Digite o novo telefone do cliente: ")
                    novoCpf = input("Digite o novo CPF do cliente: ")
                    novoEmail = input("Digite o novo E-mail do cliente: ")
                    novoEndereco = input("Digite o nono endereço do cliente: ")
                    cli.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cli.mostrarCliente()
                elif decidir == 5:
                    break
                else:
                    print('Digite um valor válido.\n')
        # FUNCIONÁRIOS
        elif local == 5:
            fun = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionário\n"
                                    "Digite 2 para remover um funcionário\n"
                                    "Digite 3 para alterar um funcionário\n"
                                    "Digite 4 para mostrar funcionários\n"
                                    "Digite 5 para sair\n"
                                    ": "))
                if decidir == 1:
                    clt = input("Digite a CLT do funcionário: ")
                    nome = input("Digite o nome do funcionário: ")
                    telefone = input("Digite o telefone do funcionário: ")
                    cpf = input("Digite o CPF do funcionárioe: ")
                    email = input("Digite o E-mail do funcionárioe: ")
                    endereco = input("Digite o endereço do funcionário: ")
                    fun.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    funcionario = input("Digite o funcionário que deseja remover: ")
                    fun.removerFuncionario(funcionario)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do funcionário que deseja alterar: ")
                    novaClt = input("Digite a nova CLT do funcionário: ")
                    novoNome = input("Digite o novo nome do funcionário: ")
                    novoTelefone = input("Digite o novo telefone do funcionário: ")
                    novoCpf = input("Digite o novo CPF do funcionário: ")
                    novoEmail = input("Digite o novo E-mail do funcionário: ")
                    novoEndereco = input("Digite o novo endereço do funcionário: ")
                    fun.alterarFuncionario(nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    fun.mostrarFuncionario()
                elif decidir == 5:
                    break
                else:
                    print('Digite um valor válido.\n')
        # VENDAS
        elif local == 6:
            ven = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"
                                    ": "))
                if decidir == 1:
                    nome = input('Digite o nome do produto: ')
                    vendedor = input('Digite nome do vendedor: ')
                    comprador = input('Digite o nome do cliente: ')
                    quantidade = int(input('Digite a quantidade: '))
                    ven.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano: ")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano: ")
                    ven.mostrarVenda(dataInicio, dataTermino)
                elif decidir == 3:
                    break
                else:
                    print("Digite um valor válido.")
        # RELÁTORIO PRODUTOS MAIS VENDIDOS
        elif local == 7:
            rel = Controller.ControllerVenda()
            rel.relatorioProdutos()
        # SAIR
        elif local == 8:
            break
        else:
            print('Digite um valor válido.\n')




