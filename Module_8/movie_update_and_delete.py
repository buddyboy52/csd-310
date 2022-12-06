import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "P@ssword123",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    def show_films(cursor, title):
        # method to execute an inner join on a all tables,
        # iterateover the dataset and output the results to the terminal window
        
        # inner join query
        cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
        
        # Get the results from the cursor object
        films = cursor.fetchall()
        
        print("\n -- {} --".format(title))
        
        # Iterate over the film data set and display the results
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()