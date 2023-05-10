from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.en.practicum-services.com/")

# Найди поле "Email" и заполни его
driver.find_element(...)...

# Найди поле "Пароль" и заполни его
driver.find_element(...)...

# Найди кнопку "Войти" и кликни по ней
driver.find_element(...)...

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3)...

# Проверь, что текущий url равен 'https://around-v1.en.practicum-services.com/'
...

driver.quit()
