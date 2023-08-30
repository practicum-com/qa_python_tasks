from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
...

# Buscar el campo Contraseña y rellenarlo
...

# Buscar el botón Iniciar sesión y hacer clic en él
...

# Agregar una espera explícita para que se cargue la página
WebDriverWait(...).until(...)

# Buscar el botón, recuperar su texto y comprobar que el valor del texto es 'Cerrar sesión'
assert ...

driver.quit()
