from selenium.webdriver.common.by import By

def visit(driver):
    if not visit_create(driver=driver):
        return False
    return True

def visit_create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[1]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/table/tbody/tr[2]/td[6]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/button").click()

        place = "улица Пушкина, дом Колотушкина"
        symptoms = "смешинка"
        diagnosis = "передозировка тиктоком"
        prescriptions = "ограничить прием мемов"
        data = {
            'place': place,
            'symptoms': symptoms,
            'diagnosis': diagnosis,
            'prescriptions': prescriptions,
        }

        input_place = driver.find_element(By.ID, "location")
        input_symp = driver.find_element(By.ID, "symptoms")
        input_diag = driver.find_element(By.ID, "diagnosis")
        input_prescriptions = driver.find_element(By.ID, "prescription")

        input_place.send_keys(data['place'])
        input_symp.send_keys(data['symptoms'])
        input_diag.send_keys(data['diagnosis'])
        driver.find_element(By.XPATH, '/html/body/main/div/div/div/div/form/div[1]/div[4]/select/option[6]').click()
        input_prescriptions.send_keys(data['prescriptions'])

        driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/form/div[2]/button[2]").click()

        if "Запись о пациенте успешно добавлена." in driver.find_element(By.XPATH, "/html/body/div").text:
            return True
        else:
            return False
    except:
        return False