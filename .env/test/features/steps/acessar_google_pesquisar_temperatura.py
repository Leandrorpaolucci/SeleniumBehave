# Autor: Leandro Ribeiro Paolucci
from behave import *
# chamando a classe em pages pesquisa temperatura o context, faz ele abrir os métodos
from features.pages.acessar_google_pesquisar_temperatura import PesquisaTemperatura

pesquisa_temperatura = PesquisaTemperatura


@given(u'que eu estou no site do google')
def step_impl(context):
    pesquisa_temperatura.acessar_site_google(context)


@when(u'eu pesquisar a temperatura de hoje')
def step_impl(context):
    pesquisa_temperatura.pesquisar_temperatura(context)
    pesquisa_temperatura.inserir_texto_no_elemento(context)
    pesquisa_temperatura.clicar_para_realizar_pesquisa(context)


@then(u'o navegador deve trazer a temperatura de hoje')
def step_impl(context):
    ...


@then(u'fecho o navegador')
def step_impl(context):
    ...
