class Venda:
    def __init__(self, mercado, carteira, visualizar):
        self.mercado = mercado
        self.carteira = carteira
        self.visualizar = visualizar

    def executar(self):
        acoes = self.carteira.get_acoes()

        if not acoes:
            print("Você não possui ações para vender!")
            return

        self.visualizar.mostrar_carteira()
        empresas = list(acoes.keys())

        try:
            print("\nDigite o número da empresa que deseja vender:")
            for i, empresa in enumerate(empresas, 1):
                print(f"{i}. {empresa}")

            escolha = int(input(">>> ")) - 1
            if escolha < 0 or escolha >= len(empresas):
                print("Opção inválida!")
                return

            empresa = empresas[escolha]
            preco_medio, quant_possuida = acoes[empresa]
            preco_atual = self.mercado.get_empresas()[empresa][0]

            quantidade = int(
                input(f"Quantidade de ações de {empresa} (Possui: {quant_possuida}): "))

            if quantidade <= 0:
                print("Quantidade inválida!")
                return

            if quantidade > quant_possuida:
                print(f"Quantidade insuficiente! Máximo: {quant_possuida}")
                return

            receita = preco_atual * quantidade

            if self.carteira.vender_acao(empresa, quantidade, preco_atual):
                self.mercado.adicionar_quantidade(empresa, quantidade)
                print(f"\nVenda realizada com sucesso!")
                print(
                    f"Você vendeu {quantidade} ações de {empresa} a R${preco_atual:.2f} cada")
                print(f"Total recebido: R${receita:.2f}")
            else:
                print("Erro ao vender ações!")

        except ValueError:
            print("Entrada inválida!")
