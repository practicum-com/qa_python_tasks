import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around.en.practicum-services.com/")

# Выполни авторизацию
...

# Добавь явное ожидание для загрузки списка карточек контента
...

# Запомни title последней карточки
title_before = ...

# Кликни по кнопке добавления нового контента
driver.find_element(...)...

# сгенерируй новое место и введи его в поле названия
new_title = ...
driver.find_element(...)...

# В поле ссылки на изображение введи ссылку
driver.find_element(...)...

# Сохрани контент
driver.find_element(...)...

# Дождись появления кнопки удаления карточки
WebDriverWait(...).until(...)

# Проверь, что на карточке отображается верное название
title_after = ...
assert ...

# Запомни количество карточек до удаления
cards_before = len(...)

# Удали карточку
driver.find_element(...)...

# Дождись, что title последней карточки равен title_before
WebDriverWait(...).until(...)

# Проверь, что количество карточек стало на одну меньше
cards_after = len(...)
assert ...

driver.quit()
