import requests

# URL base para la API de TheMovieDB
url_base = "https://api.themoviedb.org/3/"
# Definir la clave de la API y el código de país directamente en el código
api_key = "1b5e4c5722010f132052504f17ae4c6c"
country_code = "ES"
def buscar_peliculas(titulo):
    url = f'{url_base}/search/movie'
    params = {
        'api_key': api_key,
        'query': titulo,
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])

def obtener_detalle_pelicula(id_pelicula):
    url = f'{url_base}/movie/{id_pelicula}'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    return response.json()
