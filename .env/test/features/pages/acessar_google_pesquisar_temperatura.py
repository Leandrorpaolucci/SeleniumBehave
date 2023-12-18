#Autor Leandro Ribeiro Paolucci

## .. volta o diretorio para fazer os import's

from time import sleep

from ..support.ambiente import *
from ..support.elementos import *
from ..support.page_utils import PageUtils

page_utils = PageUtils()

class PesquisaTemperatura:

    def acessar_site_google(context):
        page_utils.abrir_browser(URL_GOOGLE)

    def pesquisar_temperatura(context):
        page_utils.clicar_elemento_pagina(CAIXA_CLIQUE_PESQUISA)
    
    def inserir_texto_no_elemento(context):
        page_utils.inserir_dados_no_elemento(CAIXA_CLIQUE_PESQUISA, TEXTO_PESQUISA)
        sleep(2)
        
    def clicar_para_realizar_pesquisa(context):
        page_utils.clicar_elemento_pagina(TEXTO_PESQUISA_ELEMENTO)
        sleep(15)
