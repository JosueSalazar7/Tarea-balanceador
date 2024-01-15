#Utiliza una imagen de python
FROM python:3.9
#Establecer el directorio de trabajo dentro del contenedor
WORKDIR /Servidor1
#Copiar todos los archivos desde la carpeta del host al contendor(Primero el host y luego del contendor)
COPY servidor1.py . 
#Instalar las dependencias requeridas 
RUN pip install flask

#Comando para ejecutar mi aplicion
CMD ["python","servidor1.py"]
