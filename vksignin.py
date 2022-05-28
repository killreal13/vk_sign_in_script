from logger import info_logger
from typing import Any
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def create_driver(driver):
    match driver:
        case 'safari':
            return webdriver.Safari()
        case 'chrome':
            return webdriver.Chrome()
        case 'firefox':
            return webdriver.Firefox()
        case _:
            raise ValueError(f'{driver} not supported, try another. '
                             f'Supported drivers list: safari, chrome, firefox')


class VkSignIn:
    username: str
    password: str
    driver: Any

    # path_to_driver: str

    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = create_driver(driver)
        # self.path_to_driver = path_to_driver

    def signing_in(self, exception_counter: int = 0):
        try:
            exception_counter += 1
            self.driver.get('http://www.vk.com')
            response = self.driver.find_element(By.XPATH, '//*[@id="index_login"]/div/form/button[1]')
            response.send_keys(Keys.RETURN)
            wait = WebDriverWait(self.driver, 10)
            response = wait.until(EC.element_to_be_clickable((By.NAME, 'login')))
            response.send_keys('kirill.dyuzhij@yandex.ru')
            response.send_keys(Keys.RETURN)
            response = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
            response.send_keys('5534097Asd')
            response.send_keys(Keys.RETURN)
        except Exception:
            if exception_counter < 2:
                self.signing_in()
            else:
                return 'Too much tries'
        else:
            info_logger.info('Signed in successfully!')
        finally:
            self.driver.quit()


vk = VkSignIn('kirill.dyuzhij@yandex.ru', '5534097Asd', 'safari')
vk.signing_in()