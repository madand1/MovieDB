import requests
import os

API_KEY = os.getenv("TMDB_API_KEY")
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
        results = response.json().get('results', [])
        results.sort(key=lambda x: x['title'])  # Ordenar alfabéticamente
        return results
    return []

def obtener_detalle_pelicula(id):
    url = f'{BASE_URL}/movie/{id}'
    params = {
        'api_key': API_KEY,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        pelicula = response.json()
        # Obtener el trailer de YouTube
        pelicula['trailer'] = obtener_trailer_pelicula(id)
        return pelicula
    return None

def obtener_trailer_pelicula(id):
    url = f'{BASE_URL}/movie/{id}/videos'
    params = {
        'api_key': API_KEY,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        videos = response.json().get('results', [])
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return f"https://www.youtube.com/watch?v={video['key']}"
    return None

def buscar_actores(query):
    url = f'{BASE_URL}/search/person'
    params = {
        'api_key': API_KEY,
        'query': query,
        'language': 'es-ES'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200):
        results = response.json().get('results', [])
        results.sort(key=lambda x: x['name'])  # Ordenar alfabéticamente
        return results
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
