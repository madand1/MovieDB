from flask import Flask, render_template, request, redirect, url_for
import tmdb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    peliculas = []
    error = None
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            peliculas = tmdb.buscar_peliculas(title)
            if not peliculas:
                error = "No se encontraron películas con ese título."
        else:
            error = "Por favor, ingrese un título de película."
    return render_template('index.html', peliculas=peliculas, error=error)

@app.route('/pelicula/<int:id>')
def detalle_pelicula(id):
    pelicula = tmdb.obtener_detalle_pelicula(id)
    return render_template('pelicula.html', pelicula=pelicula)

@app.route('/buscar_actores', methods=['GET', 'POST'])
def buscar_actores():
    actores = []
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            actores = tmdb.buscar_actores(name)
            if not actores:
                error = "No se encontraron actores con ese nombre."
        else:
            error = "Por favor, ingrese un nombre de actor."
    return render_template('actores.html', actores=actores, error=error)

@app.route('/actor/<int:id>')
def detalle_actor(id):
    actor = tmdb.obtener_detalle_actor(id)
    return render_template('actor.html', actor=actor)


if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)
