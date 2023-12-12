import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time, sys
from selenium.webdriver.common.by import By

from test_auth import auth


def test_main():
   options = webdriver.FirefoxOptions()
   
   driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

   driver.maximize_window()
   driver.implicitly_wait(60)
   
   driver.get("http://localhost:5000")

   result_auth = auth(driver=driver)
   assert result_auth == True, "Ошибка аутентификации."

   driver.close()
   driver.quit()