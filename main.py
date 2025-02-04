import requests
from dotenv import load_dotenv  
import os

load_dotenv()

api_key= os.getenv("OpenWeatherMap_API")


def get_coordinates(city, state, country, api_key):
    # URL da Geocoding API
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={api_key}"
    
    # Fazendo a requisição
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Verificando se a cidade foi encontrada
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            print("Cidade não encontrada.")
            return None, None
    else:
        print(f"Erro ao obter coordenadas: {response.status_code}")
        return None, None
  
    


def get_weather(latitude, longitude, api_key):
    # URL da API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    
    # Fazendo a requisição
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Extraindo informações relevantes
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        sensacao = data["main"]["feels_like"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        nome = data["name"]
        horario = data["dt"]
        
        # Exibindo os resultados
        print(f"Clima em {nome}:")
        print(f"Temperatura: {temperature}°C")
        print(f"Condição: {weather_description.capitalize()}")
        print(f"Máxima: {temp_max}")
        print(f"Mínima: {temp_min}")
        print(f"Sensação Térmica: {sensacao}")
        print(f'Horario?: {horario}')
    else:
        print(f"Erro ao obter dados climáticos: {response.status_code}")

if __name__ == "__main__":

    
    # Solicita ao usuário o nome da cidade, estado e país
    city = input("Digite o nome da cidade: ")
    state = input("Digite o nome do estado (opcional, pressione Enter para pular): ")
    country = input("Digite o nome do país (opcional, pressione Enter para pular): ")
    
    # Obtém as coordenadas
    latitude, longitude = get_coordinates(city, state, country, api_key)
    
    if latitude and longitude:
        # Obtém e exibe o clima
        get_weather(latitude, longitude, api_key)


