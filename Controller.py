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




a = ControllerEstoque()
a.removerProduto('banana')
