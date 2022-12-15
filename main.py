from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Buscar pdf de precios de C.Argentino.
def correo_prices():
    url_link = (
        "https://www.correoargentino.com.ar/MiCorreo/public/faqs"  # Correo Argentino
    )

    web_driver_paths = "C:/PATH/TO/WEBDRIVER.EXE"  # Ruta al webdriver elegido.

    firefox_binary_path = "C:/PATH/TO/firefox.exe"  # Path a firefox requerido

    # Especificación de paths necesarios para Selenium
    driver = webdriver.Firefox(
        executable_path=web_driver_paths, firefox_binary=firefox_binary_path
    )

    # Abrir el link en navegador y maximizar ventana.
    driver.get(url_link)
    driver.implicitly_wait(3)
    driver.maximize_window()

    sleep(2)  # Esperar 2 seg.

    # Encontrar en el menú la opción "precios" y hacer click.
    element = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/h4[5]/a"
    )
    element.click()

    sleep(2)

    # Encontrar dentro de Precios la opción "¿Cuál es el precio de mi envío?"
    element2 = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[23]/div[1]/h4/a"
    )
    element2.click()

    sleep(2)  # Esperar 2 seg.

    # Guardar en <tag> el contenido del contenedor HTML del texto dado.
    tag = driver.find_element(By.LINK_TEXT, "Monotributista y Consumidor Final")

    # Obtener el Link del texto asociado.
    current_lnk = tag.get_attribute("href")
    driver.close()
    return current_lnk


# Guardar pdf.
def save_prices(current_lnk):
    import requests

    # Para guardar pdf vía link
    url = current_lnk
    data = requests.get(url, stream=True)


    #variable asociada con los ultimos caracteres del link en "str":
    #son números que nunca se repiten. Se usa para nombrar el archivo pdf
    filename = str(url[-14:-1])

    # Guardando el archivo en el directorio indicado.
    with open(f"C:/PATH/TO/SAVE/{filename}.pdf", "wb") as file:
        file.write(data.content)


link = correo_prices()
save_prices(link)
