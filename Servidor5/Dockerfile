#Utiliza una imagen de python
FROM python:latest
#Establecer el directorio de trabajo dentro del contenedor
WORKDIR /Servidor5
#Copiar todos los archivos desde la carpeta del host al contendor(Primero el host y luego del contendor)
COPY servidor5.py . 
#Instalar las dependencias requeridas 
RUN pip install flask

#Comando para ejecutar mi aplicion
CMD ["python","servidor5.py"]
