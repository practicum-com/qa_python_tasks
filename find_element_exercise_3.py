from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar elementos
email = driver...
password = driver...

# Probar el atributo placeholder para cada elemento
assert ...
assert ...

# Cerrar el navegador
driver...
