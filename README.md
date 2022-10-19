<div align=center>
    <img src="https://bundlen.com/wp-content/uploads/2020/05/selenium_logo_square_green.png" width=90px>
    <img src="https://blog.bossylobster.com/images/requests-python-logo.png" width=80px >
</div>

<br>

<div align=center>
    <h1>Correo Argentino  e-commerce "paq.ar":<br>
    Buscando el archivo pdf de precios y guardándolo</h1>
</div>


### Descripción
Este proyecto es una aproximación y aprendizaje del módulo < selenium > y < requests >. El objetivo es automatizar la búsqueda del link que contiene el archivo pdf con la matriz de precios para e-commerce de [Correo Argentino][CA] y guardarlo en un directorio dado.

<br>

Dicho archivo pdf se encuentra despues de los siguientes pasos: 

>  ###### _**"preguntas frecuentes"**_   -->   _**"precios"**_   -->   _**"¿cúal es el precio de mis envíos?"**_   --> _**monotributista y consumidor final"**_  

<br>


Según los requerimientos para que Selenium pueda funcionar correctamente, éste código usa el webdriver para Mozilla Firefox: [geckodriver][FWB]. Aunque también fue probado el Webdriver de Microsoft [Edge][EWB].


---

<details><summary>Ver Código</summary>


 ```Python

from time import sleep

# Buscar pdf de precios de C.Argentino.
def correo_prices():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    url_link = "https://www.correoargentino.com.ar/MiCorreo/public/faqs"     # Correo Argentino

    web_driver_paths = "C:/PATH/TO/WEBDRIVER.EXE"     # Ruta al webdriver elegido.

    firefox_binary_path = "C:/Program Files/Firefox Developer Edition/firefox.exe"  #Path a firefox requerido
    
    # Especificación de paths necesarios para Selenium
    driver = webdriver.Firefox(
        executable_path=web_driver_paths, 
        firefox_binary=firefox_binary_path
    )

    # Abrir el link en navegador y maximizar ventana.
    driver.get(url_link)
    driver.implicitly_wait(3)
    driver.maximize_window()

    sleep(2) # Esperar 2 seg.
    
    # Encontrar en el menú la opción "precios" y hacer click.
    element = driver.find_element(
        By.XPATH, 
        "/html/body/div[1]/div[2]/div/div/div[1]/h4[5]/a"
    )
    element.click()

    sleep(2) 


    # Encontrar dentro de Precios la opción "¿Cuál es el precio de mi envío?"
    element2 = driver.find_element(
        By.XPATH, 
        "/html/body/div[1]/div[2]/div/div/div[2]/div/div[23]/div[1]/h4/a"
    )
    element2.click() 

    sleep(2) # Esperar 2 seg.

    # Guardar en <tag> el contenido del contenedor HTML del texto dado.
    tag = driver.find_element(
        By.LINK_TEXT, 
        "Monotributista y Consumidor Final")

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


    """
    variable asociada con los ultimos caracteres del link en "str":
    son números que nunca se repiten. Se usa para nombrar el archivo pdf
    """
    filename = str(url[-14:-1])    
                   
             

    # Guardando el archivo en el directorio indicado.
    with open(f"C:/PATH/TO/SAVE/{filename}.pdf", "wb") as file:
        file.write(data.content)

link = correo_prices()
save_prices(link) 
 ```
</details>


[CA]: https://www.correoargentino.com.ar/MiCorreo/public/faqs
[FWB]: https://github.com/mozilla/geckodriver/releases
[EWB]: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
