from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around.en.practicum-services.com/")

# Выполни авторизацию
...

# Добавь явное ожидание загрузки страницы
...

# Кликни по изображению профиля
driver.find_element(...)...

# В поле ссылки на изображение введи ссылку, используй переменную avatar_url
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(...)....

# Сохрани новое изображение
driver.find_element(...)...

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(...)...
# Проверь, что в style содержится ссылка на аватар
assert ...

driver.quit()
