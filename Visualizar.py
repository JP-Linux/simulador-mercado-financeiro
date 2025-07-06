class Visualizar:
    def __init__(self, mercado, carteira):
        self.mercado = mercado
        self.carteira = carteira

    def mostrar_mercado(self):
        empresas = self.mercado.get_empresas()
        print("\nMERCADO DE AÇÕES")
        print("=" * 50)
        print(f"{'Empresa':<15} {'Preço':<15} {'Qtd Disponível':<15}")
        print("-" * 50)
        for empresa, dados in empresas.items():
            preco, quantidade = dados
            print(f"{empresa:<15} R${preco:<14.2f} {quantidade:<15}")
        print("=" * 50)

    def mostrar_carteira(self):
        acoes = self.carteira.get_acoes()
        print("\nSUA CARTEIRA")
        print("=" * 50)
        print(f"Saldo disponível: R${self.carteira.get_dinheiro():.2f}")
        print("-" * 50)
        print(
            f"{'Empresa':<15} {'Qtd':<10} {'Preço Médio':<15} {'Valor Investido':<15}")
        print("-" * 50)

        if not acoes:
            print("Você não possui ações")
        else:
            for empresa, dados in acoes.items():
                preco_medio, quantidade = dados
                total_investido = preco_medio * quantidade
                print(
                    f"{empresa:<15} {quantidade:<10} R${preco_medio:<14.2f} R${total_investido:<14.2f}")
        print("=" * 50)
