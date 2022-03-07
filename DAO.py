from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('arquivos-txt/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos-txt/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        
        return cat

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('arquivos-txt/venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + '|' + 
            venda.itensVendido.preco + '|' + 
            venda.itensVendido.categoria + '|' + 
            venda.vendedor + '|' + venda.comprador + '|' + 
            str(venda.quantidadeVendida) + '|' + venda.data)


            arq.writelines('\n')

    @classmethod    
    def ler(cls):
        with open('arquivos-txt/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vend = []

        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('arquivos-txt/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco +
            '|' + produto.categoria + '|' + str(quantidade))

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos-txt/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        
        est = []

        for i in cls.estoque:
            est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))

        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('arquivos-txt/fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj +
            '|' + fornecedor.telefone + '|' + fornecedor.categoria)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos-txt/fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        
        forn = []

        for i in cls.estoque:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('arquivos-txt/clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.telefone +
            '|' + pessoas.cpf + '|' + pessoas.email + 
            '|' + pessoas.endereco)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos-txt/clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))
        
        clie = []

        for i in cls.clientes:
            clie.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return clie

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('arquivos-txt/funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome +
            '|' + funcionario.telefone + '|' + funcionario.cpf + 
            '|' + funcionario.email + '|' + funcionario.endereco)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos-txt/funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))
        
        func = []

        for i in cls.funcionarios:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return func




        