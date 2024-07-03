import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # First query: Select all fields from studio table
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("Studios:")
    for studio in studios:
        print(studio)
    
    # Second query: Select all fields from genre table
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("\nGenres:")
    for genre in genres:
        print(genre)

    # Third query: Select movie names for movies with runtime less than two hours
    cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    print("\nMovies with runtime less than 2 hours:")
    for film in short_films:
        print(film[0])

    # Fourth query: List of film names and directors, grouped by director
    cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') FROM film GROUP BY film_director")
    films_by_director = cursor.fetchall()
    print("\nFilms grouped by director:")
    for director in films_by_director:
        print(f"Director: {director[0]}\nFilms: {director[1]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    db.close()
