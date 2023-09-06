from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(...)...

# Buscar el campo Contraseña y rellenarlo
driver.find_element(...)...

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(...)...

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3)...

# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/signin?lng=es'
...

driver.quit()
