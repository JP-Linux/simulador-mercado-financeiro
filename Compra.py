class Compra:
    def __init__(self, mercado, carteira, visualizar):
        self.mercado = mercado
        self.carteira = carteira
        self.visualizar = visualizar

    def executar(self):
        self.visualizar.mostrar_mercado()
        empresas = list(self.mercado.get_empresas().keys())
        
        if not empresas:
            print("Não há empresas disponíveis!")
            return

        try:
            print("\nDigite o número da empresa que deseja comprar:")
            for i, empresa in enumerate(empresas, 1):
                print(f"{i}. {empresa}")
            
            escolha = int(input(">>> ")) - 1
            if escolha < 0 or escolha >= len(empresas):
                print("Opção inválida!")
                return
                
            empresa = empresas[escolha]
            preco = self.mercado.get_empresas()[empresa][0]
            quant_disponivel = self.mercado.get_empresas()[empresa][1]
            
            quantidade = int(input(f"Quantidade de ações de {empresa} (Disponíveis: {quant_disponivel}): "))
            
            if quantidade <= 0:
                print("Quantidade inválida!")
                return
                
            if quantidade > quant_disponivel:
                print(f"Quantidade indisponível! Máximo: {quant_disponivel}")
                return
                
            custo_total = preco * quantidade
            
            if self.carteira.comprar_acao(empresa, quantidade, preco):
                self.mercado.remover_quantidade(empresa, quantidade)
                print(f"\nCompra realizada com sucesso!")
                print(f"Você comprou {quantidade} ações de {empresa} a R${preco:.2f} cada")
                print(f"Total gasto: R${custo_total:.2f}")
            else:
                print("Saldo insuficiente para comprar!")
                
        except ValueError:
            print("Entrada inválida!")