import os
from flask import Flask, render_template, request, redirect, url_for
from tmdb import buscar_pelicula  # Importar la función desde tmdb.py

# Inicializar la aplicación Flask
app = Flask(__name__, template_folder='templates')

# Definir la ruta de inicio
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener el título de la película del formulario
        titulo = request.form.get('title')
        if titulo:
            # Redirigir a la ruta para mostrar los resultados de la búsqueda
            return redirect(url_for('buscar_pelicula_route', titulo=titulo))
    # Si es una solicitud GET o no se proporcionó un título, renderizar el formulario de búsqueda
    return render_template("index.html")

# Definir la ruta para buscar películas
@app.route('/pelicula/<titulo>')
def buscar_pelicula_route(titulo):
    peliculas = buscar_pelicula(titulo)
    if peliculas is not None:
        # Si la solicitud es exitosa, mostrar los resultados en la plantilla
        return render_template("pelicula.html", peliculas=peliculas)
    else:
        # Si hay un error en la solicitud, mostrar un mensaje de error en la plantilla
        return render_template("error.html", error=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run("0.0.0.0", port=port, debug=True)
