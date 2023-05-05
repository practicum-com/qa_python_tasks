from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around.en.practicum-services.com/")

# Выполни авторизацию
...

# Добавь явное ожидание для загрузки списка карточек контента
...

# Найди карточку контента и сделай скролл до неё
...

driver.quit()
