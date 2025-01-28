import requests

OMDB_API_KEY = "d3362e91" # Substitua pela sua chave da OMDb API
OMDB_BASE_URL = "http://www.omdbapi.com/"

def fetch_movie(title):
    """
    Busca informações de um filme pelo título na OMDb API.
    Retorna um dicionário com os dados do filme ou None caso não
    encontrado.
    """
    params = {"t": title, "apikey": OMDB_API_KEY}
    response = requests.get(OMDB_BASE_URL, params=params)
    if response.status_code == 200 and response.json().get("Response") == "True":
        return {
            "title": response.json()["Title"],
            "year": response.json()["Year"],
            "genre": response.json()["Genre"],
            "director": response.json()["Director"],
            "imdb_rating": response.json()["imdbRating"]
        }
    return None


if __name__ == "__main__":
    movie = fetch_movie("Titanic")
    print(movie)