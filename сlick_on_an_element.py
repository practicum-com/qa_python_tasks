from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.es.practicum-services.com/")

# Buscar el botón y hacer clic en él
driver.find_element(...)...

driver.quit()
