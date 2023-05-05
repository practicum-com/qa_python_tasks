from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around.en.practicum-services.com/")

# Найди элементы
email = driver...
password = driver...

# Проверь атрибут placeholder для каждого элемента
assert ...
assert ...

# Закрой браузер
driver...
