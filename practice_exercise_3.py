from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around-v1.es.practicum-services.com/")

# Iniciar sesión
...

# Agregar una espera explícita para que se cargue la página
...

# Buscar la tarjeta y desplazarla a la vista
...

driver.quit()
