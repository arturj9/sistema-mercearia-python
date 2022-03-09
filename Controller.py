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
        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
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
                #TODO: ALTERAR A CATEGORIA TAMBÉM DO ESTOQUE
            else:
                print('A categoria para qual deseja alterar já existe.')
        else:
            print('A categoria que deseja alterar não existe.')
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma cadastrada.')
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