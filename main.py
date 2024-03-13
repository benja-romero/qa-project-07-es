import data
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
        assert 'Comfort' in routes_page.get_comfort_title()  #comprobacion de que la tarifa se selecciono adecuadamente

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_number_field()
        routes_page.set_phone_number()
        routes_page.click_netx_button_phone_field()
        routes_page.set_phone_number_code()
        routes_page.confirm_phone()
        phone_number = data.phone_number
        assert routes_page.get_phone_number() == phone_number #comprobacion de que el numero de telefono ingresado es el correcto

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_pay_method()
        routes_page.add_credit_card()
        routes_page.set_card_number()
        routes_page.set_card_code()
        routes_page.enable_add_card_button()
        routes_page.click_button_add_card()
        routes_page.close_pay_method()
        card_number = data.card_number
        code_card = data.card_code
        # comprobacion de que el numero de tarjeta y el codigo de la misma sean los correctos
        assert routes_page.get_credit_card_number() == card_number
        assert routes_page.get_code_card() == code_card


    def test_set_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message()
        message = data.message_for_driver
        assert routes_page.get_message() == message #comprobacion del mensaje al conductor

    def test_blanket_and_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enable_switch_selector()
        # comprobacion de que se activo correctamente la opcion de "manta y pañuelos"
        assert routes_page.blanket_scarves_enabled() == 'Manta y pañuelos'

    def test_order_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_cream()
        assert routes_page.ice_cream_is_ordered() == "2" #comrobacioin de que se ordenaron 2 helados

    def test_confirm_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        routes_page.countdown_timer()
        assert "Pedir un taxi" in routes_page.taxi_requested() #comprobacion de que se hace click en el boton pedir taxi

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()