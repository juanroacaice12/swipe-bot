from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Configurar la ruta al ChromeDriver
chromedriver_path = r'C:\Users\Usuario\Desktop\Swipe-Bot\chromedriver.exe'

# Configurar el servicio del ChromeDriver
service = Service(chromedriver_path)

# Configurar las opciones del WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximizar la ventana del navegador al abrir

# Iniciar el WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Navegar a la página de Badoo
driver.get('https://badoo.com')

# Esperar a que cargue la página completamente
wait = WebDriverWait(driver, 20)  # Ajustar el tiempo de espera según sea necesario

try:
    # Esperar a que aparezca y sea clickable el botón "Entrar"
    entrar_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/signin"]')))
    entrar_button.click()
    
    # Esperar a que aparezca el campo de correo electrónico y luego ingresarlo
    email_input = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    email_input.send_keys('kmiciber1224@gmail.com')  # Reemplazar con tu correo
    
    # Ingresar la contraseña
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('Kingsman527*')  # Reemplazar con tu contraseña

    # Presionar el botón de inicio de sesión
    password_input.send_keys(Keys.RETURN)
    
    # Esperar a que se complete el inicio de sesión
    time.sleep(10)  # Ajustar este tiempo según sea necesario

except TimeoutException as e:
    print(f"Error: Tiempo de espera agotado - {e}")
    driver.quit()
    exit()

except NoSuchElementException as e:
    print(f"Error: No se encontró el elemento necesario - {e}")
    driver.quit()
    exit()

except Exception as e:
    print(f"Error al iniciar sesión: {e}")
    driver.quit()
    exit()

# Empezar a hacer swipes
while True:
    try:
        # Encuentra el botón de swipe a la derecha y haz click
        swipe_right_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
        swipe_right_button.click()
        
        # Esperar un momento antes del siguiente swipe
        time.sleep(2)
    
    except Exception as e:
        print(f"Error al hacer swipe: {e}")
        break

# Cerrar el navegador al terminar
driver.quit()
