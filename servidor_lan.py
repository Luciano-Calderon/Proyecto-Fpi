from flask import Flask, jsonify


app=Flask(__name__)

# salas son los datos que vamos a subir al servidor lan, una lista de diccionarios
salas = [
    {
        "computador1":"Encendido",
        "computador2":"Apagado",
        "computador3":"Directamente no fucniona"
    },
    {
        "computador1":"Encendido",
        "computador2":"Encendido",
        "computador3":"Apagado"
    }
]

#con el / indico que es la ruta raíz, yo puedo elegir la ruta que va a tener lo que se muestra
@app.route("/")
def informacion():
    return jsonify(salas)

if __name__=="__main__":
    #debug=True es para ver los cambios a tiempo real, modo de depuración
    #el puerto es completamente mi eleción (4 numeros por alguna razon), por defecto es 5000
    app.run(debug=True, port=2647, host="0.0.0.0")