import mysql.connector
from mysql.connector import errorcode

# Our config files
config = {
    "user": "root",
    "password": "P@ssword123",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect the database to our code
    db = mysql.connector.connect(**config)

    # Print confirmation that databse was connected
    print("\nDatabase user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))

    # Make sure the cursor is made for typing the commands
    cursor = db.cursor()
    
    # Create a querie for our studio table
    # Execute the select command to display all contents in the studio table
    cursor.execute("SELECT * FROM studio")
    
    # Fetch all contents that were displayed
    studio = cursor.fetchall()
    
    # Give the studio querie a title
    print("\n-- DISPLAYING Studio RECORDS --")
    
    # Print everything
    for studio in studio:
        print("Studio ID: {}\n-- Studio Name: {}\n".format(studio[0], studio[1]))
        
    
    
    # Create a querie for our studio table
    # Execute the select command to display all contents in the studio table
    cursor.execute("SELECT * FROM genre")
    
    # Fetch all contents that were displayed
    genre = cursor.fetchall()
    
    # Give the studio querie a title
    print("\n\n-- DISPLAYING Genre RECORDS --")
    
    # Print everything
    for genre in genre:
        print("Genre ID: {}\n-- Genre Name: {}\n".format(genre[0], genre[1]))
        
    
    # Create a querie for our studio table
    # Execute the select command to display all contents in the studio table
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    
    # Fetch all contents that were displayed
    film = cursor.fetchall()
    
    # Give the studio querie a title
    print("\n\n-- DISPLAYING Short Film RECORDS --")
    
    # Print everything
    for film in film:
        print("Film Name: {}\n-- Film Runtime: {} minutes\n".format(film[0], film[1]))


    # Create a querie for our studio table
    # Execute the select command to display all contents in the studio table
    cursor.execute("SELECT any_value(film_name), film_director FROM film ORDER BY film_director")
    
    # Fetch all contents that were displayed
    directors = cursor.fetchall()
    
    # Give the studio querie a title
    print("\n\n-- DISPLAYING Director RECORDS in Order --")
    
    # Print everything
    for director in directors:
        print("Film Name: {}\nDirector {}\n".format(director[0], director[1]))

# If the databse has issues connecting
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

# Close the database after the code is done
finally:
    db.close()