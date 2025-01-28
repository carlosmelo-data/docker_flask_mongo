from pymongo import MongoClient

def get_mongo_connection():
    """
    Estabelece uma conexão com o MongoDB local e retorna a coleção 'movies'.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["movie_catalog"]
    return db["movies"]

if __name__ == "__main__":
    collection = get_mongo_connection()
    print("Conexão com o MongoDB estabelecida e coleção pronta!")