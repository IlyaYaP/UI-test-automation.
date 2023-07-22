import allure
import pytest
import time
from data.data import RegistrationData
from selenium.webdriver.common.by import By
from pages.registration_and_login_page import RegistrationAndLoginPage


@pytest.mark.registration_and_login_tests(scope='class', autouse=True)
@allure.feature('Тесты регистрации и аутентификации нового пользователя.')
class TestRegistrationAndLoginForm():

    main_page_url = 'https://www.demoblaze.com/'

    @pytest.mark.registration_form_tests()
    @allure.story('Тест регистрации нового пользователя.')
    def test_registration_form(self, browser):
        page = RegistrationAndLoginPage(browser, self.main_page_url)
        page.open_page()
        page.registration_new_user()
        page.is_alert_message_present(
            RegistrationData.sing_up_successful_message)

    @pytest.mark.login_form_tests()
    @allure.story('Тест аутентификации нового пользователя.')
    def test_login_form(self, browser):
        page = RegistrationAndLoginPage(browser, self.main_page_url)
        page.open_page()
        time.sleep(7)
        page.login_new_user()
        page.is_element_present(
            By.XPATH,
            f'//button[text()="Welcome \
            {RegistrationAndLoginPage.user_data[0]}"]')