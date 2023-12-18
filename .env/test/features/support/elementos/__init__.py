# AUTOR LEANDRO RIBEIRO PAOLUCCI

CAIXA_CLIQUE_PESQUISA = '//textarea[@class="gLFyf"]'
TEXTO_PESQUISA = 'Qual é a temperatura de hoje'

# procurando indice 2 do elemento, variavel indice2
indice_elemento_pesquisa = 2

# string compostas utilizando duas variaveis
# criar uma string onde valores de variáveis são inseridos em posições específicas.
ELEMENTO = '//div[@class="lnnVSe"]'
TEXTO_PESQUISA_ELEMENTO = f'({ELEMENTO})[{indice_elemento_pesquisa}]'