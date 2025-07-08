import sqlite3

# Connect to your database
conn = sqlite3.connect('Spotify_IDs.db')
cursor = conn.cursor()

# The search terms
genre_search = 'rock'
artist_search = '3qm845BOgUEQ2vn4fUTTFC'

# Execute query with partial matching using LIKE and parameters
cursor.execute("""
    SELECT * FROM songs
    WHERE genres LIKE ? OR artists LIKE ?
""", (f'%{genre_search}%', f'%{artist_search}%'))

# Fetch all matching rows
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close connection
conn.close()
