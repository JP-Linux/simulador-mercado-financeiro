# Simulador de Mercado Financeiro

Bem-vindo ao Simulador de Mercado Financeiro! Este projeto permite que você simule operações de compra e venda de ações em um ambiente controlado, gerenciando seu portfólio de investimentos e acompanhando as flutuações do mercado.

![Simulador de Mercado Financeiro](https://via.placeholder.com/800x400?text=Screenshot+do+Simulador)

## Recursos Principais

- 💼 Interface interativa com menu fácil de usar
- 📈 Compra e venda de ações de empresas fictícias
- 💰 Acompanhamento em tempo real do seu saldo e investimentos
- 📊 Visualização detalhada do mercado e da sua carteira
- 🔄 Atualização dinâmica dos preços das ações
- 📦 Gestão de portfólio com cálculo automático de preço médio

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/JP-Linux/simulador-mercado-financeiro.git
cd simulador-mercado-financeiro
```

2. Execute o programa:
```bash
python main.py
```

## Como Usar
1. **Ver Mercado**: Visualize as ações disponíveis com seus preços e quantidades
2. **Ver Carteira**: Acompanhe seu saldo e as ações que você possui
3. **Comprar Ações**: Selecione uma empresa e a quantidade desejada
4. **Vender Ações**: Venda ações que você possui pelo preço de mercado atual
5. **Atualizar Preços**: Gere novos preços aleatórios para as ações
6. **Sair**: Encerre o programa

## Estrutura do Projeto
```
simulador-mercado-financeiro/
├── Mercado.py          # Gerencia empresas, preços e quantidades
├── Carteira.py         # Gerencia saldo e portfólio do usuário
├── Visualizar.py       # Responsável pela exibição de dados
├── Compra.py           # Lógica de compra de ações
├── Venda.py            # Lógica de venda de ações
├── main.py             # Arquivo principal com o menu
└── README.md           # Este arquivo
```

## Exemplo de Uso
```text
==================================================
SIMULADOR DE MERCADO FINANCEIRO
==================================================
1. Ver Mercado
2. Ver Carteira
3. Comprar Ações
4. Vender Ações
5. Atualizar Preços do Mercado
6. Sair
Escolha uma opção: 1

MERCADO DE AÇÕES
==================================================
Empresa         Preço           Qtd Disponível 
--------------------------------------------------
NanoTech        R$194.31         47             
Soleil          R$221.37         14             
Veridian        R$239.93         18             
CosmoTravel     R$237.36         26             
EduNexus        R$159.97         63             
AeroStratus     R$163.57         55             
SkyScape        R$181.71         25             
TerraBounty     R$245.67         47             
GoldenGrain     R$235.19         48             
BrewCraft       R$165.79         88             
OceanHarvest    R$218.71         74             
SavoryFields    R$242.66         73             
==================================================

```

## Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato
**Jorge Paulo Santos**  
Email: [jorgepsan7@gmail.com](mailto:jorgepsan7@gmail.com)  
GitHub: [https://github.com/JP-Linux](https://github.com/JP-Linux)  
LinkedIn: [https://www.linkedin.com/in/jorgepaulo-santos](https://www.linkedin.com/in/jorgepaulo-santos)

---
**Nota**: Este projeto foi desenvolvido para fins educacionais e de simulação. Não representa um sistema real de negociação financeira.