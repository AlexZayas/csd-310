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

def show_films(cursor, title):
    # Query to select film name, genre name, and studio name
    query = """
        SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    print(f"\n-- {title} --")
    for film in films:
        print(f"Name: {film[0]}, Director: {film[1]}, Genre: {film[2]}, Studio: {film[3]}")

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display initial films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film record
    insert_query = """
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, ("Inception", "2010", 148, "Christopher Nolan", 3, 2))
    db.commit()

    # Display films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the film "Alien" to be a Horror film
    update_query = """
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien'
    """
    cursor.execute(update_query)
    db.commit()

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the film "Gladiator"
    delete_query = """
        DELETE FROM film WHERE film_name = 'Gladiator'
    """
    cursor.execute(delete_query)
    db.commit()

    # Display films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

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


