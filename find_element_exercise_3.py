from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.en.practicum-services.com/")

# Найди элементы
email = driver...
password = driver...

# Проверь атрибут placeholder для каждого элемента
assert ...
assert ...

# Закрой браузер
driver...
