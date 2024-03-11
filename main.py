import data
import time
from selenium import webdriver
from page_objects.UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(3)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_taxi()
        routes_page.select_comfort_tariff(4)

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_number_field()
        routes_page.set_phone_number()
        routes_page.click_netx_button_phone_field()
        routes_page.set_phone_number_code()
        routes_page.confirm_phone()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_pay_method()
        routes_page.add_credit_card()
        routes_page.set_card_number()
        routes_page.set_card_code()
        routes_page.enable_add_card_button()
        routes_page.click_button_add_card()
        routes_page.close_pay_method()

    def test_set_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message()

    def test_blanket_and_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enable_switch_selector()

    def test_order_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_cream()

    def test_confirm_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        routes_page.cuenta_regresiva()



    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.quit()

UrbanRoutes = TestUrbanRoutes()
UrbanRoutes.setup_class()
UrbanRoutes.test_set_route()
UrbanRoutes.teardown_class()