class Carteira:
    def __init__(self, dinheiro_inicial=200.00):
        self._dinheiro = dinheiro_inicial
        self.acoes = {}  # {empresa: [preco_medio, quantidade]}

    def comprar_acao(self, empresa, quantidade, preco_unitario):
        custo_total = quantidade * preco_unitario
        if self._dinheiro < custo_total:
            return False

        self._dinheiro -= custo_total

        if empresa in self.acoes:
            preco_medio_antigo, quant_antiga = self.acoes[empresa]
            novo_total = (preco_medio_antigo * quant_antiga) + custo_total
            nova_quantidade = quant_antiga + quantidade
            novo_preco_medio = novo_total / nova_quantidade
            self.acoes[empresa] = [novo_preco_medio, nova_quantidade]
        else:
            self.acoes[empresa] = [preco_unitario, quantidade]

        return True

    def vender_acao(self, empresa, quantidade, preco_venda):
        if empresa not in self.acoes or self.acoes[empresa][1] < quantidade:
            return False

        _, quant_atual = self.acoes[empresa]

        # Atualizar quantidade na carteira
        nova_quantidade = quant_atual - quantidade
        if nova_quantidade == 0:
            del self.acoes[empresa]
        else:
            self.acoes[empresa][1] = nova_quantidade

        # Adicionar dinheiro da venda
        receita = quantidade * preco_venda
        self._dinheiro += receita
        return True

    def get_dinheiro(self):
        return self._dinheiro

    def get_acoes(self):
        return self.acoes

    def get_quantidade_acao(self, empresa):
        if empresa in self.acoes:
            return self.acoes[empresa][1]
        return 0
