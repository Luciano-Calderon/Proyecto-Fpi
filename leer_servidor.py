import requests

url = "http://192.168.1.27:2647"

#solicitud al servidor
response = requests.get(url)

#el 200 es para ver si se conectó
if response.status_code == 200:
    print("Datos recibidos:")
    print(response.json())
else:
    print("Error al conectar con el servidor")