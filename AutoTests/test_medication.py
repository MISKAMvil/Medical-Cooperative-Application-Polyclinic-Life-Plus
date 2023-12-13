from selenium.webdriver.common.by import By

def medicine(driver):
    if not med_create(driver=driver):
        return False
    return True

def med_create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/button").click()
        med_name = "русский стандарт"
        method_of_use = "наружный"
        description = "тестовое лекарство"
        impact = "положительное"
        side_effects = "нет."
        data = {
            'med_name': med_name,
            'method_of_use': method_of_use,
            'description': description,
            'impact': impact,
            'side_effects': side_effects
        }

        input_med_name = driver.find_element(By.ID, "name")
        input_meth_to_use = driver.find_element(By.ID, "method_of_use")
        input_descp = driver.find_element(By.ID, "description")
        input_impact = driver.find_element(By.ID, "effects")
        input_side_effects = driver.find_element(By.ID, "side_effects")

        input_med_name.send_keys(data['med_name'])
        input_meth_to_use.send_keys(data['method_of_use'])
        input_descp.send_keys(data['description'])
        input_impact.send_keys(data['impact'])
        input_side_effects.send_keys(data['side_effects'])

        driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div[2]/form/div[6]/button[1]").click()

        if "Успешно добавлено новое лекарство." in driver.find_element(By.XPATH, "/html/body/div").text:
            return True
        else:
            return False
    except:
        return False