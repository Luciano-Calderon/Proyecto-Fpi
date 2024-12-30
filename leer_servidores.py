import requests

def leer_computador1():
    
    url = "http://192.168.1.36:2647" #notar que cada computador emite una diferente, para adaptarla a eso
    try:
        #solicitud al servidor
        response = requests.get(url)

        #el 200 es para ver si se conectó
        if response.status_code == 200:
            return "Datos computador1 recibidos:"
    
    except:
        return "Error al conectar con el computador1"
    
def leer_computador2():
    url = "http://192.168.1.27:2641"
    response = requests.get(url)

    if response.status_code == 200:
        print("Datos computador2 recibidos:")
        print(response.json())
    else:
        print("Error al conectar con el computador2")
        
leer_computador1()    