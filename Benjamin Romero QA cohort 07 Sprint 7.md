# Benjamin Romero QA cohort 07 Sprint 7
## _Automatizacion de pruebas en UrbanRoutes_



En este proyecto se automatizan las pruebas requeridas para pedir un taxi con la tarifa Comfort, asì mismo agregando elementos como solicitar helado, manta y pañuelos y dejando un mensaje para el conductor.

 __Las pruebas se realizaron dentro de la interfaz Web de UrbanRoutes; la técnica fue a través de automatización de pruebas con lenguaje de programación Python en su versión 3.12, utilizando como IDE a PyCharm en su versión Community 2023.3.3__
 
 
Las acciones que se tomaron en cuenta para realizar las prubeas fueorn:


- Configurar la dirección.
- Seleccionar la tarifa Comfort.
- Rellenar el número de teléfono.
- Agregar una tarjeta de crédito. 
- Escribir un mensaje para el controlador.
- Pedir una manta y pañuelos.
- Pedir 2 helados.
- Confirmar el taxi.
- Esperar a que aparezca la información del conductor.

Dentro del archivo data.py se tienen los datos que se van a usar para llenar los campos necesarios, asi como la URL de la interfaz Web de UrbanRoutes.

En el archivo main.py se encuentran todas las pruebas de la lista.

En el archivo UrbanRoutesPage.py se encuentran todos los localizadores y mètodos necesarios para llevar a cabo las pruebas del archivo main.py.

Hay un archivo extra llamado phone_code.py donde està la clase que recupera el còdigo de verificaciòn para poder agregar el numero de telèfono.