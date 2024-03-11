import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from page_objects import phone_code

import data


class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    home_page = (By.ID, 'root')
    button_pedir_taxi = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_tariff = (By.CLASS_NAME, 'tcard')
    phone_number = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.NAME, 'phone')
    button_phone_number_next = (By.XPATH, "//button[text()='Siguiente']")
    code_phone_number_field = (By.XPATH, "//input[@class='input'][@type='text'][@id='code']")
    confirm_phone_number = (By.XPATH, "//button[text()='Confirmar']")
    pay_method_field = (By.CLASS_NAME, 'pp-button')
    button_add_new_card = (By.CLASS_NAME, 'pp-plus-container')
    card_field = (By.ID, 'number')
    cvv_field = (By.NAME, 'code')
    enable_add_card = (By.CLASS_NAME, 'card-wrapper')
    button_add_card = (By.XPATH, "//button[text()='Agregar']")
    button_close_pay_method = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    message_field = (By.ID, 'comment')
    switch_selector_blanket_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    chocolate_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]')
    confirm_taxi = (By.CLASS_NAME, 'smart-button-secondary')
    temporizador = (By.CLASS_NAME, 'order-header-title')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)



    def select_taxi(self):
        self.driver.find_element(*self.button_pedir_taxi).click()

    def select_comfort_tariff(self, index):
        driver = self.driver
        comfort_tariff_button = driver.find_elements(*self.comfort_tariff)
        comfort_tariff_button[index].click()

    def select_phone_number_field(self):
        self.driver.find_element(*self.phone_number).click()

    def set_phone_number(self):
        number = data.phone_number
        self.driver.find_element(*self.phone_number_field).send_keys(number)

    def click_netx_button_phone_field(self):
        self.driver.find_element(*self.button_phone_number_next).click()

    def set_phone_number_code(self):
        code = phone_code.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_phone_number_field).send_keys(code)

    def confirm_phone(self):
        self.driver.find_element(*self.confirm_phone_number).click()

    def set_pay_method(self):
        self.driver.find_element(*self.pay_method_field).click()

    def add_credit_card(self):
        self.driver.find_element(*self.button_add_new_card).click()

    def set_card_number(self):
        card_number = data.card_number
        self.driver.find_element(*self.card_field).send_keys(card_number)

    def set_card_code(self):
        card_code = data.card_code
        self.driver.find_element(*self.cvv_field).send_keys(card_code)

    def enable_add_card_button(self):
        self.driver.find_element(*self.enable_add_card).click()

    def click_button_add_card(self):
        self.driver.find_element(*self.button_add_card).click()

    def close_pay_method(self):
        self.driver.find_element(*self.button_close_pay_method).click()

    def set_message(self):
        message = data.message_for_driver
        self.driver.find_element(*self.message_field).send_keys(message)

    def enable_switch_selector(self):
        self.driver.find_element(*self.switch_selector_blanket_scarves).click()

    def order_ice_cream(self):
        order_ice_cream = self.driver.find_element(*self.ice_cream_counter)
        actions = ActionChains(self.driver)
        actions.double_click(order_ice_cream).perform()
        time.sleep(2)
        how_many_ice_creams = self.driver.find_element(*self.chocolate_ice_cream)
        actions = ActionChains(self.driver)
        actions.double_click(how_many_ice_creams).perform()

    def request_taxi(self):
        self.driver.find_element(*self.confirm_taxi).click()

    def cuenta_regresiva(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element
                                             ((By.CLASS_NAME, 'order-header-title'), 'El conductor'))


