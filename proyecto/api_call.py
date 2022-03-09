import requests

# Metodo que toma una cadena y ve si esta compuesta de numeros
def check_str(str):
    # Quita el simbolo de menos y divide la cadena en dos a partir del punto
    ls = str.lstrip("-").split(".")
    result = all(n.isdigit() for n in ls) and len(ls) <= 2
    return result

#Metodo que pide una latitud y longitud y regresa la respuesta del API
def peticion(lat, lon):
    # Checa si el tipo de la entrada es una string
    if type(lat) is not str or type(lon) is not str:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")
    # Checa que la cadena solo tenga valores numericos
    if check_str(lat) == False or check_str(lon) == False:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")

    llave = "0da7f0c5abd77248e66d02b44236020b"
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}&units=metric"
    respuesta = requests.get(url).json()
    return respuesta

r = peticion("25.7785", "-100.107")
print(r)
