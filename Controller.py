from Models import *
from DAO import *
from datetime import datetime
class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já existe.')
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe.')
        else:
            for i in range(0, len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
            with open('arquivos-txt/categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade) if(
                            x.produto.categoria == categoriaRemover) else(x), estoque))
        with open('arquivos-txt/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco +
            '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                with open('arquivos-txt/categoria.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.categoria)    
                        arq.writelines('\n') 
                print(f'Categoria {categoriaAlterar} alterada para {categoriaAlterada}.')
            else:
                print('A categoria para qual deseja alterar já existe.')
        else:
            print('A categoria que deseja alterar não existe.')
        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) if(
                                x.produto.categoria == categoriaAlterar) else(x), estoque))
        with open('arquivos-txt/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco +
            '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma categoria cadastrada.')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        e = DaoEstoque.ler()
        c = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria, c))
        est = list(filter(lambda x: x.produto.nome == nome, e))
        if len(cat) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já existe em estoque.')
        else:
            print('Categoria não existe.')
    def removerProduto(self, nome):
        e = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, e))
        if len(est) > 0:
            for i in range(0, len(e)):
                if e[i].produto.nome == nome:
                    del e[i]
                    break
            with open('arquivos-txt/estoque.txt', 'w') as arq:
                for i in e:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco +
            '|' + i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')
            print('Produto removido com sucesso!')
        else:
            print('O produto que deseja remover não existe.')
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        e = DaoEstoque.ler()
        c = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == novaCategoria, c))
        if len(cat) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, e))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, e))
                if len(est) == 0:
                    e = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), e))
                    with open('arquivos-txt/estoque.txt', 'w') as arq:
                        for i in e:
                            arq.writelines(i.produto.nome + '|' + i.produto.preco +
            '|' + i.produto.categoria + '|' + str(i.quantidade))
                            arq.writelines('\n')
                    print('Produto alterado com sucesso.')
                else:
                    print('Produto já cadastrado.')
            else:
                print('O produto que deseja alterar não existe.')
        else:
            print('A categoria informada não existe.')
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print('=====Produtos=====')
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}\n'
                      f'------------------'
                )
class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        e = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        for i in e:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        with open('arquivos-txt/estoque.txt', 'w') as arq:
            for i in temp:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))  
                arq.writelines('\n')
        if existe == False:
            print('O produto não existe.')
            return None
        elif not quantidade:
            print('A quantidade vendida não contêm em estoque.')
        else:
            print('Venda realizada com sucesso.')
            return valorCompra
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = int(i.quantidadeVendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': quantidade + x['quantidade']} if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Estes são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'==========Produto [{a}]==========')
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n"
                  '-----------------------------------'
            )
            a += 1
    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 
                                        and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f'==========Venda [{cont}]==========')
            print(f'Nome: {i.itensVendido.nome}\n'
                  f'Categoria: {i.itensVendido.categoria}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: {i.comprador}\n'
                  f'Vendedor: {i.vendedor}\n'
            )
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f'Total vendido: {total}')
class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        fon = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, fon))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, fon))
        if len(listaCnpj) > 0:
            print('O CNPJ já existe.')
        elif len(listaTelefone) > 0:
            print('O telefone já existe.')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso.')
            else:
                print('Digite um CNPJ e/ou telefone válido.')
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        fon = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, fon))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, fon))
            if len(est) == 0:
                fon = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar) else(x), fon))
                with open('arquivos-txt/fornecedores.txt', 'w') as arq:
                    for i in fon:
                        arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                        arq.writelines('\n')
                print('Fornecedor alterado com sucesso.')
            else:
                print('CNPJ já existe.')
        else:
            print('O fornecedor que deseja alterar não existe.')
    def removerFornecedor(self, nome):
        fon = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, fon))
        if len(est) > 0:
            for i in range(0, len(fon)):
                if fon[i].nome == nome:
                    del fon[i]
                    with open('arquivos-txt/fornecedores.txt', 'w') as arq:
                        for i in fon:
                            arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                            arq.writelines('\n')
                    print('Fornecedor removido com sucesso.')
                    break
        else:
            print('O fornecedor que deseja remover não existe.')
            return None
    def mostrarFornecedor(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia.')
        else:
            print('==========Fornecedores==========')
            for i in fornecedores:
                print(f'Categoria fornecida: {i.categoria}\n'
                      f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'CNPJ: {i.cnpj}\n'
                      f'--------------------------------'
                )
class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        pes = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, pes))
        if len(listaCpf) > 0:
            print('CPF já existente.')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso.')
            else:
                print('Digite um CPF e/ou telefone válido.')
    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        pes = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, pes))
        if len(est) > 0:
            est = list(filter(lambda x: x.nome == novoNome, pes))
            if len(est) == 0:
                pes = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(
                    x.nome == nomeAlterar) else(x), pes))
                with open('arquivos-txt/clientes.txt', 'w') as arq:
                    for i in pes:
                        arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                        arq.writelines('\n')
                print('Cliente alterado com sucesso.')
            else:
                print('O cliente para qual deseja alterar já existe.')
        else:
            print('O cliente que deseja alterar não existe.')
    def removerCliente(self, nome):
        pes = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, pes))
        if len(est) > 0:
            for i in range(0, len(pes)):
                if pes[i].nome == nome:
                    del pes[i]
                    with open('arquivos-txt/clientes.txt', 'w') as arq:
                        for i in pes:
                            arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                            arq.writelines('\n')
                    print('Cliente removido com sucesso.')
                    break
        else:
            print('O cliente que deseja remover não existe.')
            return None
    def mostrarCliente(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print('Lista de clientes vazia.')
        else:
            print('==========Clientes==========')
            for i in clientes:
                print(f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Endereço: {i.endereco}\n'
                      f'Email: {i.email}\n'
                      f'CPF: {i.cpf}\n'
                      f'--------------------------------'
                )
class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        fun = DaoFuncionario.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, fun))
        listaClt = list(filter(lambda x: x.clt == clt, fun))
        if len(listaCpf) > 0:
            print('CPF já existente.')
        elif len(listaClt) > 0:
            print('Já existe um funcionário com essa CLT.')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionário cadastrado com sucesso.')
            else:
                print('Digite um CPF e/ou telefone válido.')
    def alterarFuncionario(self, nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        fun = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, fun))
        if len(est) > 0:
            est = list(filter(lambda x: x.nome == novoNome, fun))
            if len(est) == 0:
                est = list(filter(lambda x: x.clt == novaClt, fun))
                if len(est) == 0:
                    fun = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(
                        x.nome == nomeAlterar) else(x), fun))
                    with open('arquivos-txt/funcionarios.txt', 'w') as arq:
                        for i in fun:
                            arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                            arq.writelines('\n')
                    print('Funcionário alterado com sucesso.')
                else:
                    print('Já existe um funcionário com essa CLT.')
            else:
                print('O funcionário para qual deseja alterar já existe.')
        else:
            print('O funcionário que deseja alterar não existe.')
    def removerFuncionario(self, nome):
        fun = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, fun))
        if len(est) > 0:
            for i in range(0, len(fun)):
                if fun[i].nome == nome:
                    del fun[i]
                    with open('arquivos-txt/funcionarios.txt', 'w') as arq:
                        for i in fun:
                            arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                            arq.writelines('\n')
                    print('Funcionário removido com sucesso.')
                    break
        else:
            print('O funcionário que deseja remover não existe.')
            return None
    def mostrarFuncionario(self):
        funcionarios = DaoFuncionario.ler()
        if len(funcionarios) == 0:
            print('Lista de funcionários vazia.')
        else:
            print('==========Funcionários==========')
            for i in funcionarios:
                print(f'CLT: {i.clt}\n'
                      f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Endereço: {i.endereco}\n'
                      f'Email: {i.email}\n'
                      f'CPF: {i.cpf}\n'
                      f'--------------------------------'
                )