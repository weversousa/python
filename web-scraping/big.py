from produtos_comprar import produtos
from capturar_eventos import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep
from json import load, dump

driver = Firefox()
ef_driver = EventFiringWebDriver(driver, MyListener())

url_big = 'https://www.big.com.br/'

ef_driver.get(url_big)
sleep(5)

elemento_html = ef_driver.find_element_by_class_name('vtex-cep')
elemento_html.send_keys('06210040')
sleep(2)
elemento_html = ef_driver.find_element_by_class_name('vtex-whiteLB')
elemento_html.click()
sleep(8)
elemento_html = ef_driver.find_element_by_id('truste-consent-button')
elemento_html.click()
sleep(5)

big = {}

for produto in produtos:
    elemento_html = ef_driver.find_element_by_css_selector(
        'input[placeholder="O que você está procurando?"]')
    sleep(2)
    elemento_html.clear()
    elemento_html.send_keys(produto, Keys.ENTER)
    sleep(5)

    try:
        botao_mais_produtos = ef_driver.find_element_by_class_name('vtex-minicart-2-x-closeIconButton')
        botao_mais_produtos.click()
        sleep(3)
    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException):
        print('Meu carrinho não apareceu')

    try:
        botao_mais_produtos = ef_driver.find_element_by_class_name('vtex-button')
        botao_mais_produtos.click()
        sleep(3)
    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException):
        print('Não foi encontrado o botão para mais produtos.')

    elementos_html = ef_driver.find_elements_by_class_name('vtex-product-summary-2-x-container')
    sleep(5)

    try:
        for elemento in elementos_html:
            nome_produto = elemento.find_element_by_class_name('vtex-product-summary-2-x-productBrand').text
            preco_produto = elemento.find_element_by_class_name('vtex-productShowCasePrice').text
            big[nome_produto] = preco_produto
    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException):
        print('Não foi encontrado o botão para mais produtos.')

ef_driver.quit()

with open('carrefour_vs_big.json', 'r', encoding='utf8') as f:
    carrefour_vs_big = load(f)
    carrefour_vs_big['big'] = {}
    carrefour_vs_big['big'].update(big)

with open('carrefour_vs_big.json', 'w', encoding='utf8') as f:
    dump(carrefour_vs_big, f, ensure_ascii=False, indent=True)
