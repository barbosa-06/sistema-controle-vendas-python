produtos = []
vendas = []

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir(self):
        print(f'Nome: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}')


    def cadastrar_produto(self):
        self.nome = input('Digite o nome do produto: ').strip().title()
        self.preco = float(input('Digite o preço do produto: R$'))
        self. estoque = int(input('Digite a quantidade em estoque: '))

        print('\nProduto cadastrado com sucesso!\n')


    def realizar_venda(self, quantidade):
        if quantidade > self.estoque:
            print('Quantidade solicitada excede o estoque disponivel.')

        else:
            self.estoque -= quantidade
            valor_total = quantidade * self.preco
            print(f'Venda realizada com sucesso! Valor total: R${valor_total:.2f}')

def gerar_relatorio_vendas(vendas):
    if not vendas:
        print('Nenhuma venda realizada.')
        
    else:
        print('RELATÓRIO DE VENDAS'.center(30, '='))
        
        fatura_total = sum(venda['valor_total'] for venda in vendas)
        print(f'\nFaturamento total: R${fatura_total:.2f}')

        quantidade_por_produto = {}

        for venda in vendas:
            produto = venda['produto']

            if produto not in quantidade_por_produto:
                quantidade_por_produto[produto] = 0

            quantidade_por_produto[produto] += venda['quantidade']

        print(quantidade_por_produto)

        for produto, quantidade in quantidade_por_produto.items():
            print(f'Produto: {produto} / Quantidade vendida: {quantidade}')
            
            maior_quantidade = max(vendas, key=lambda x: x['quantidade'])
            print(f'maior quantidade vendida: {maior_quantidade["produto"]} - {maior_quantidade["quantidade"]} unidades')

        for venda in vendas:
            print('-' * 30)
            print(f'Produto: {venda["produto"]}')
            print(f'Quantidade: {venda["quantidade"]}')
            print(f'Valor total: R${venda["valor_total"]:.2f}')


def listar_produtos(produtos):
    if not produtos:
        print('Nenhum produto cadastrado.')
    else:
        for produto in produtos:
            print('=' * 30)
            print('INFORMAÇÕES DO PRODUTO'.center(30))
            print('=' * 30)
            produto.exibir()
            
try:
    with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, preco, estoque = linha.strip().split('/')
            produto = Produto(nome.strip(), float(preco.strip()), int(estoque.strip()))
            produtos.append(produto)
except FileNotFoundError:
    print('Arquivo de produtos não encontrado.')

while True:
    print('===== Sistema de Vendas =====')
    print('''
[ 1 ] - Cadastrar produto
[ 2 ] - Listar produtos
[ 3 ] - Realizar venda
[ 4 ] - Relatório de vendas
[ 5 ] - Sair\n''')

    opcao = int(input('Sua escolha: '))

    if opcao == 1:
        produto = Produto('', 0.0, 0)
        produto.cadastrar_produto()
        produtos.append(produto)

        with open('produtos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{produto.nome} / {produto.preco} / {produto.estoque}\n')
    elif opcao == 2:
        listar_produtos(produtos)

    elif opcao == 3:
        if not produtos:
            print('Nenhum produto cadastrado para realizar a venda.')
        else:
            nome_produto = input('Digite o nome do produto para a venda: ').strip().title()
            produto_encontrado = None

            for produto in produtos:
                if produto.nome == nome_produto:
                    produto_encontrado = produto
                    break

            if produto_encontrado:
                quantidade = int(input('Digite a quantidade de produtos a vender: '))
                produto_encontrado.realizar_venda(quantidade)

                vendas.append({'produto' : produto_encontrado.nome, 'quantidade' : quantidade, 'valor_total' : produto_encontrado.preco * quantidade})

                with open('produtos.txt', 'w', encoding='utf-8') as arquivo:
                    for produto in produtos:
                        arquivo.write(f'{produto.nome} / {produto.preco} / {produto.estoque}\n')
            else:
                print('Produto não encontrado para realizar a venda.')

    elif opcao == 4:
        gerar_relatorio_vendas(vendas)
        
    elif opcao == 5:
        print('Encerrando o sistema. Até logo!')
        break

    else:
        print('Opção inválida, por favor escolha uma opção válida.')