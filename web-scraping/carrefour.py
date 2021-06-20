from produtos_comprar import produtos
from capturar_eventos import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep
from json import dump

driver = Firefox()
ef_driver = EventFiringWebDriver(driver, MyListener())

url_carrefour = 'https://mercado.carrefour.com.br/?crfimt=home|shop|seletor|\
    mercado_4p_161020|2'

ef_driver.get(url_carrefour)
sleep(5)

elemento_html = ef_driver.find_element_by_name('zipcode')
elemento_html.send_keys('06210040')
sleep(2)
elemento_html = ef_driver.find_element_by_name('submit-zipcode')
elemento_html.submit()
sleep(2)
elemento_html = ef_driver.find_element_by_id('onetrust-accept-btn-handler')
elemento_html.click()
sleep(5)

carrefour_vs_big = {}
carrefour_vs_big['carrefour'] = {}

for produto in produtos:
    elemento_html = ef_driver.find_element_by_css_selector(
        'input[role="searchbox"]')
    sleep(2)
    elemento_html.clear()
    elemento_html.send_keys(produto, Keys.ENTER)
    sleep(5)

    try:
        botao_mais_produtos = ef_driver.find_element_by_css_selector('button[aria-label="Mostrar Mais"]')
        botao_mais_produtos.click()
        sleep(3)
    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException):
        'Não foram encontrados mais de 10 produtos.'

    elementos_html = ef_driver.find_elements_by_class_name('css-1u9y7ms')

    for elemento in elementos_html:
        nome_produto = elemento.find_element_by_class_name('css-1xmtsk1').text
        preco_produto = elemento.find_element_by_class_name('css-1xc4ph5').text
        carrefour_vs_big['carrefour'][nome_produto] = preco_produto

ef_driver.quit()

with open('carrefour_vs_big.json', 'w', encoding='utf8') as f:
    dump(carrefour_vs_big, f, ensure_ascii=False, indent=True)
