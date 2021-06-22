import MySQLdb

connection = MySQLdb.connect(
    host="localhost", user="root", passwd="Mrowka$04", db="cinematic"
)
create_tables_query = """CREATE TABLE IF NOT EXISTS directors(
  director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
  name VARCHAR(30) NOT NULL, 
  surname VARCHAR(30) NOT NULL, 
  rating INT NOT NULL
);
CREATE TABLE IF NOT EXISTS  movies(
  movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
  title VARCHAR(30) NOT NULL, 
  year INT UNSIGNED NOT NULL, 
  category VARCHAR(30) NOT NULL, 
  director_id INT NOT NULL, 
  rating INT NOT NULL, 
  FOREIGN KEY (director_id) REFERENCES directors(director_id)
);
"""

insert_director_query = """INSERT INTO directors(name, surname, rating) VALUES(%s, %s, %s)"""
directors = [('Frank', 'Darabont', 7), ('Francis Ford', 'Coppola', 8), ('Quentin', 'Tarantino', 10),
             ('Christopher', 'Nolan', 9), ('David', 'Fincher', 7)]

insert_movies_query = """ INSERT INTO movies(title, year, category, director_id, rating) VALUES(%s, %s, %s , %s, %s);"""
movies = [('The Shawshank Redemption', 1994, 'Drama', 1, 8), ('The Green Mile', 1999, 'Drama', 1, 6),
          ('The Godfather', 1972, 'Crime', 2, 7), ('The Godfather III', 1990, 'Crime', 2, 6),
          ('Pulp Fiction', 1994, 'Crime', 3, 9), ('Inglourious Basterds', 2009, 'War', 3, 8),
          ('The Dark Knight', 2008, 'Action', 4, 9), ('Interstellar', 2014, 'Sci-fi', 4, 8),
          ('The Prestige', 2006, 'Drama', 4, 10), ('Fight Club', 1999, 'Drama', 5, 7),
          ('Zodiac', 2007, 'Crime', 5, 5), ('Seven', 1995, 'Drama', 5, 8), ('Alien 3', 1992, 'Horror', 5, 5)]
year = 2002
select_movie_query = """SELECT * from movies where year > %s ;"""
delete_tables_query = """ DROP table movies ,directors """

with connection:
    cursor = connection.cursor()
    # cursor.execute("CREATE DATABASE IF NOT EXISTS cinematic;")
    # cursor.execute(create_tables_query)
    #
    # for director in directors:
    #     cursor.execute(insert_director_query, director)
    # connection.commit()
    #
    # for movie in movies:
    #     cursor.execute(insert_movies_query, movie)
    # connection.commit()

    cursor.execute(select_movie_query, (year,))
    data = cursor.fetchall()
    for row in data:
        print(row)

    # cursor.execute(delete_tables_query)
