from random import randint, uniform


class Mercado:
    def __init__(self):
        self.VALOR_UNIFORM = {"min": 150.0, "max": 250.0}
        self.VALOR_RANDINT = {"min": 1, "max": 100}
        self.empresas = {}
        self.atualizar_precos()

    def atualizar_precos(self):
        for empresa in ["NanoTech", "Soleil", "Veridian",
                        "CosmoTravel", "EduNexus", "AeroStratus",
                        "SkyScape", "TerraBounty", "GoldenGrain",
                        "BrewCraft", "OceanHarvest", "SavoryFields"]:
            novo_preco = round(
                uniform(self.VALOR_UNIFORM["min"], self.VALOR_UNIFORM["max"]), 2)
            nova_quant = randint(
                self.VALOR_RANDINT["min"], self.VALOR_RANDINT["max"])
            self.empresas[empresa] = [novo_preco, nova_quant]

    def remover_quantidade(self, empresa, quantidade):
        if empresa in self.empresas:
            preco, quant_atual = self.empresas[empresa]
            nova_quant = max(0, quant_atual - quantidade)
            self.empresas[empresa] = [preco, nova_quant]
            return True
        return False

    def adicionar_quantidade(self, empresa, quantidade):
        if empresa in self.empresas:
            preco, quant_atual = self.empresas[empresa]
            self.empresas[empresa] = [preco, quant_atual + quantidade]
            return True
        return False

    def get_empresas(self):
        return self.empresas
