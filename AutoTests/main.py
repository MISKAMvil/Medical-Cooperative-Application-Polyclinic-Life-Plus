import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, sys
from selenium.webdriver.common.by import By

from test_auth import auth
from test_medication import medicine
from test_visit import visit
def test_main():
   options = webdriver.ChromeOptions()
   options.add_experimental_option("excludeSwitches", ["enable-logging"])
   options.add_argument("--no-sandbox")
   
   #executable_path = "/usr/bin/chromedriver"
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
   #driver = webdriver.Chrome(executable_path)

   driver.maximize_window()
   driver.implicitly_wait(60)
   
   driver.get("http://172.16.238.10:8000")
   # driver.get("http://127.0.0.1:5000")

   result_auth = auth(driver=driver)
   assert result_auth == True, "Ошибка аутентификации."
   result_medication = medicine(driver=driver)
   assert result_medication == True, "Ошибка при добавлении лекарства."
   result_visit = visit(driver=driver)
   assert result_visit == True, "Ошибка при добавлении осмотра."

   driver.close()
   driver.quit()
