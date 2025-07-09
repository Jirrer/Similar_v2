import sqlite3

def fetchSongs(genres):
    genresTypes = list(genres.keys())

    conn = sqlite3.connect('Spotify_IDs.db')
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
