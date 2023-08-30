from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
...

# Agregar una espera explícita para que se cargue la página
...

# Hacer clic en la foto de perfil
driver.find_element(...)...

# Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(...)....

# Guardar la nueva foto
driver.find_element(...)...

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(...)...
# Comprobar que style contiene el enlace a la foto de perfil
assert ...

driver.quit()
