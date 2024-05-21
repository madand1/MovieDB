import requests

BASE_URL = 'https://api.themoviedb.org/3'

def buscar_peliculas(query):
    url = f'{BASE_URL}/search/movie'
    params = {
        'api_key': API_KEY,
        'query': query,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []

def obtener_detalle_pelicula(id):
    url = f'{BASE_URL}/movie/{id}'
    params = {
        'api_key': API_KEY,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def buscar_actores(query):
    url = f'{BASE_URL}/search/person'
    params = {
        'api_key': API_KEY,
        'query': query,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []

def obtener_detalle_actor(id):
    url = f'{BASE_URL}/person/{id}'
    params = {
        'api_key': API_KEY,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None
