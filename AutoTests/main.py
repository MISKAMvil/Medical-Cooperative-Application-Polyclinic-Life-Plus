import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, sys
from selenium.webdriver.common.by import By

from test_auth import auth


def test_main():
   options = webdriver.ChromeOptions()
   options.add_experimental_option("excludeSwitches", ["enable-logging"])

   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

   driver.maximize_window()
   driver.implicitly_wait(60)
   
   driver.get("http://https://172.16.238.10:8000")

   result_auth = auth(driver=driver)
   assert result_auth == True, "Ошибка аутентификации."

   driver.close()
   driver.quit()