from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar las variables de entorno desde el archivo dotenv.env
load_dotenv(dotenv_path="dotenv.env")

# URL base para la API de TheMovieDB
url_base = "https://api.themoviedb.org/3/"

# Obtener la clave de la API desde las variables de entorno
api_key = os.getenv("api_key")

# Definir la ruta de inicio
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener el título de la película del formulario
        titulo = request.form.get('title')
        if titulo:
            # Redirigir a la ruta para mostrar los resultados de la búsqueda
            return redirect(url_for('buscar_pelicula', titulo=titulo))
    # Si es una solicitud GET o no se proporcionó un título, renderizar el formulario de búsqueda
    return render_template("index.html")

# Definir la ruta para buscar películas
@app.route('/pelicula/<titulo>')
def buscar_pelicula(titulo):
    # Parámetros de la solicitud a la API de TheMovieDB
    payload = {'api_key': api_key, 'query': titulo, 'language': 'en-EN'}
    # Realizar la solicitud GET a la API
    r = requests.get(url_base + 'search/movie', params=payload)
    if r.status_code == 200:
        # Si la solicitud es exitosa, obtener los resultados y mostrarlos en la plantilla
        data = r.json()
        peliculas = data.get('results', [])
        return render_template("pelicula.html", peliculas=peliculas)
    else:
        # Si hay un error en la solicitud, mostrar un mensaje de error en la plantilla
        return render_template("error.html", error=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run("0.0.0.0", debug=True)
