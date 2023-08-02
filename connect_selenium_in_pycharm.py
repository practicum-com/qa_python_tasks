from selenium import webdriver
import time

# Inicializar el controlador
driver = webdriver.Chrome()

# Agregar una espera
time.sleep(5)

# Cerrar el navegador
driver.quit()
