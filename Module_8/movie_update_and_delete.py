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

db = mysql.connector.connect(**config)

cursor = db.cursor()

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window
            
    # Inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    # Get the results from the cursor objects
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    
    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def insert_film(cursor, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id):
    
    cursor.execute("insert into film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) values(%s,%s,%s,%s,%s,%s)", (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id))

    db.commit()
    
def update_genre(cursor, new_genre_id, film_name):
    
    cursor.execute("update film set genre_id = %s where film_name = %s", (new_genre_id, film_name))
    
    db.commit()
    
def delete_movie(cursor, film_id):
    
    cursor.execute("delete from film where film_id = {}".format(film_id))
    
    db.commit()
    

show_films(cursor, "DISPLAYING FILMS")
#insert_film(cursor, "Superbad", 2007, 119, "Greg Mottola", 2, 2)
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
update_genre(cursor, 1, "Alien")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
#delete_movie(cursor, 4)
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


    