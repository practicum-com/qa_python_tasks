import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.es.practicum-services.com/")

# Iniciar sesión
...

# Agregar una espera explícita para que se cargue la página
...

# Guardar el título de la tarjeta más reciente
title_before = ...

# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(...)...

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
new_title = ...
driver.find_element(...)...

# Insertar el enlace a la imagen en el campo Enlace
driver.find_element(...)...

# Guardar los datos
driver.find_element(...)...

# Esperar a que aparezca el botón Eliminar
WebDriverWait(...).until(...)

# Comprobar que la tarjeta tiene el título correcto
title_after = ...
assert ...

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(...)

# Delete the card
driver.find_element(...)...

# Wait for the title of the most recent card to become equal to title_before
WebDriverWait(...).until(...)

# Check that there is one less card now 
cards_after = len(...)
assert ...

driver.quit()
