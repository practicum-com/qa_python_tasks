from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.en.practicum-services.com/")

# Найди поле "Email" и заполни его
...

# Найди поле "Пароль" и заполни его
...

# Найди кнопку "Войти" и кликни по ней
...

# Добавь явное ожидание для загрузки страницы
WebDriverWait(...).until(...)

# Найди кнопку, получи её текст и проверь, что он равен 'Выйти'
assert ...

driver.quit()
