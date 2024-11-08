# ParcialDiseño
## Instrucciones para ejecutar el programa

### Paso 1: Instalación de dependencias
Ejecuta el siguiente comando en la terminal para instalar todas las dependencias necesarias:
```bash
pip install -r requirements.txt
```
### Paso 2: Iniciar el programa
Ejecuta el archivo principal con el siguiente comando:
```bash
python main.py
```
### Paso 3: Configuración de Postman
Abre Postman y carga el archivo que se encuentra en la carpeta collection. 

### Paso 4: Verificación de secuencia de ADN
En Postman, selecciona la solicitud POST para enviar una secuencia de ADN y verificar si es mutante. Ingresa la secuencia de ADN en el cuerpo de la solicitud y envíala.

### Paso 5: Estadísticas
Para ver las estadísticas, selecciona la solicitud GET en Postman para obtener el número de mutantes y no mutantes registrados en la base de datos.  Postman se ejecutará en la siguiente URL: http://127.0.0.1:5000/