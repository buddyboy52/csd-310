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

# For our cursor
cursor = db.cursor()

# Create a show_films method to show the films with a nice title
def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window
            
    # Inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    # Get the results from the cursor objects
    films = cursor.fetchall()
    
    # Print the title
    print("\n -- {} --".format(title))
    
    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Create a insert_film function to insert a film into the films table
def insert_film(cursor, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id):
    
    # Execute the insert with the desired criteria
    cursor.execute("insert into film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) values(%s,%s,%s,%s,%s,%s)", (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id))

    # Commit the new film to the database
    db.commit()
    
# Create a update_genre method to update the genre of an existing movie
def update_genre(cursor, new_genre_id, film_name):
    
    # Execute the command to change the genre
    cursor.execute("update film set genre_id = %s where film_name = %s", (new_genre_id, film_name))
    
    # Commit the change to the database
    db.commit()
    
# Create a delete_movie method to delete a movie from the database
def delete_movie(cursor, film_id):
    
    # Execute the command to delete the specified movie with the specified film_id
    cursor.execute("delete from film where film_id = {}".format(film_id))
    
    # Commit the change to the database
    db.commit()
    
# Call the methods
show_films(cursor, "DISPLAYING FILMS")
#insert_film(cursor, "Superbad", 2007, 119, "Greg Mottola", 2, 2)
insert_film()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
update_genre(cursor, 1, "Alien")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
#delete_movie(cursor, 4)
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


    