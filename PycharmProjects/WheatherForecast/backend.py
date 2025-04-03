import requests
from api_key.APIKEY import API_KEY

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY()}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"] # Damn this shit hard - Usa el debugger para entender mas
    nr_values = 8 * forecast_days # Esta es la cantidad de valores que obtendremos por dia
    filtered_data = filtered_data[:nr_values] # Esta es el filtro de los datos dependiendo de los dias que busquemos
    #if kind == "Temperature": # Si el user elige temperatura
    #    filtered_data = [dict["main"]["temp"] for dict in filtered_data] # Filtramos la data (checa el debug de data para ver las "carpetas" del dict
    #if kind = = "Sky": # Si el user elige sky
    #    filtered_data = [dict["weather"][0]["main"] for dict in filtered_data] # Filtramos la data correspondiendo, denuevo, checa el debugger, es mas facil que si lo lees con un print
    return filtered_data

if __name__ =="__main__":
    print(type(get_data("Yucatan", 2)))