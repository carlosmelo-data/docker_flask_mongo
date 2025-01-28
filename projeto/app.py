from flask import Flask, jsonify, render_template, request
from mongo_client import get_mongo_connection
from omdb_client import fetch_movie

app = Flask(__name__)
movies_collection = get_mongo_connection()

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route("/get_movies", methods=["GET"])
def get_movies():
    """
    Retorna todos os filmes armazenados no MongoDB.
    """
    movies = list(movies_collection.find({}, {"_id": 0}))
    return jsonify(movies)

@app.route("/add_movie", methods=["POST"])
def add_movie():
    """
    Adiciona um novo filme ao MongoDB usando a OMDb API.
    """
    title = request.form.get("titulo")

    if not title:
        return jsonify("O campo 'title' é obrigatório.")
    
    # Verificar se o filme já existe no banco
    filme_existente = movies_collection.find_one({"title": title})
    if filme_existente:
        return jsonify("O filme já está cadastrado no banco de dados.")
    else: 
        movie = fetch_movie(title)

        if not movie:
            return jsonify("Filme não encontrado na OMDb API.")
        
        movies_collection.insert_one(movie)
        return jsonify("Filme adicionado com sucesso!")

if __name__ == "__main__":
    app.run(debug=True, port=9000)