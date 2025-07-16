import os
import sqlite3

def fetchSongs(genres):
    genresTypes = list(genres.keys())

    base_path = os.path.dirname(__file__)
    db_path = os.path.join(base_path, "Spotify_IDs.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    clauses = []
    params = []

    for genre in genresTypes:
        clauses.append("genres LIKE ?")
        params.append(f"%{genre}%")

    statement = " OR ".join(clauses)

    query = f"SELECT * FROM songs WHERE {statement}"
    cursor.execute(query, params)

    results = cursor.fetchall()
    conn.close()
    
    return results
