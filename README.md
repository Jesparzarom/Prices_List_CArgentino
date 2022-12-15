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


[CA]: https://www.correoargentino.com.ar/MiCorreo/public/faqs
[FWB]: https://github.com/mozilla/geckodriver/releases
[EWB]: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
