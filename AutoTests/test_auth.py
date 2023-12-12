from selenium.webdriver.common.by import By
import uuid

def auth(driver):
    result_login = login(driver)
    if not result_login:
        return False
    
    return True

def login(driver):
    try:
        driver.get("http://https://172.16.238.10:8000/auth/login")
        input_username = driver.find_element(By.XPATH, "/html/body/main/div/div/form/div[1]/input")
        input_password = driver.find_element(By.XPATH, "/html/body/main/div/div/form/div[2]/input")
        randomize = str(uuid.uuid4())
        login = str(randomize)
        password = str(randomize)
        login = 'user1'
        password = 'qwerty'
        data = {
            'login': login,
            'password': password,
        }
        print(data)
        input_username.send_keys(data['login'])
        input_password.send_keys(data['password'])
        driver.find_element(By.XPATH, "/html/body/main/div/div/form/button").click()
        if "Вы успешно аутентифицированы." in driver.find_element(By.XPATH, "/html/body/div").text:
            return True
        else:
            return False
    except:
        return False