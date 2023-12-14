from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import uuid

def auth(driver):
    result_login = login(driver)
    if not result_login:
        return False
    
    return True

def login(driver):
    try:
        driver.get("http://172.16.238.10:8000/auth/login")
        # driver.get("http://127.0.0.1:5000/auth/login")
        input_username = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/div[1]/input"))
        )
        input_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/div[2]/input"))
        )

        # Используем случайные данные
        randomize = str(uuid.uuid4())
        login = 'user1'
        password = 'qwerty'

        data = {
            'login': login,
            'password': password,
        }
        print(data)

        input_username.send_keys(data['login'])
        input_password.send_keys(data['password'])

        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/button"))
        )
        
        print("Попытка выполнить click()")
        button.click()
        print("click() выполнен успешно")

        if "Вы успешно аутентифицированы." in driver.find_element(By.XPATH, "/html/body/div").text:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
