from flask import Flask, render_template, request, redirect, url_for
import tmdb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        peliculas = tmdb.buscar_peliculas(title)
        return render_template('pelicula.html', peliculas=peliculas)
    return render_template('index.html')

@app.route('/pelicula/<int:id>')
def pelicula(id):
    pelicula = tmdb.obtener_detalle_pelicula(id)
    return render_template('pelicula.html', pelicula=pelicula)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)
