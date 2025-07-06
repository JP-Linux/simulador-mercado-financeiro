from Mercado import Mercado
from Carteira import Carteira
from Visualizar import Visualizar
from Compra import Compra
from Venda import Venda


def main():
    # Criar instâncias únicas compartilhadas
    mercado = Mercado()
    carteira = Carteira()
    visualizar = Visualizar(mercado, carteira)
    compra = Compra(mercado, carteira, visualizar)
    venda = Venda(mercado, carteira, visualizar)

    while True:
        print("\n" + "=" * 50)
        print("SIMULADOR DE MERCADO FINANCEIRO")
        print("=" * 50)
        print("1. Ver Mercado")
        print("2. Ver Carteira")
        print("3. Comprar Ações")
        print("4. Vender Ações")
        print("5. Atualizar Preços do Mercado")
        print("6. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida!")
            continue

        if opcao == 1:
            visualizar.mostrar_mercado()
        elif opcao == 2:
            visualizar.mostrar_carteira()
        elif opcao == 3:
            compra.executar()
        elif opcao == 4:
            venda.executar()
        elif opcao == 5:
            mercado.atualizar_precos()
            print("\nPreços do mercado atualizados!")
            visualizar.mostrar_mercado()
        elif opcao == 6:
            print("\nEncerrando simulador...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
