## Autor: Leandro Ribeiro Paolucci Funcionalidades page_ultils

import unittest, base64, time, os, subprocess, pytz, allure, json, urllib3, behave, behave_html_formatter
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from .ambiente import *

class PageUtils(unittest.TestCase):
    # Configurações e opções Microsoft Edge
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--disable-site-isonation-trials')
    edge_options.add_argument('--ignore-certificate-erros')
    edge_options.add_argument('--start-maximized')
    driver = webdriver.Edge(options=edge_options)

    # Métodos execuções em PageUtils
    def abrir_browser(context, base_url):
        context.driver.get(base_url)

    def limpar_browser(context):
        context.driver.delete_all_cookies()

    def fechar_browser(context): 
        context.driver.quit()

    def clicar_elemento_pagina(context, pesquisa):
        context.driver.find_element(By.XPATH, pesquisa).click()

    def inserir_dados_no_elemento(context, insert, texto):
        context.driver.find_element(By.XPATH, insert).send_keys(texto)

    
        
        






