import requests

# URL base para la API de TheMovieDB
url_base = "https://api.themoviedb.org/3/"
# Definir la clave de la API y el código de país directamente en el código
api_key = "1b5e4c5722010f132052504f17ae4c6c"
country_code = "ES"

def buscar_pelicula(titulo):
    # Parámetros de la solicitud a la API de TheMovieDB
    payload = {'api_key': api_key, 'query': titulo, 'language': 'en-EN'}
    # Realizar la solicitud GET a la API
    r = requests.get(url_base + 'search/movie', params=payload)
    if r.status_code == 200:
        # Si la solicitud es exitosa, obtener los resultados y retornarlos
        data = r.json()
        return data.get('results', [])
    else:
        # Si hay un error en la solicitud, retornar None
        return None
