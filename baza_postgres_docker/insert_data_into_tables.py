from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from baza_postgres_docker.create_tables import Director, engine, Movie

Session = sessionmaker(bind=engine)
session = Session()
directors = [{'name': 'Frank', 'surname': 'Darabont', 'rating': 7},
             {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8},
             {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10},
             {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9},
             {'name': 'David', 'surname': 'Fincher', 'rating': 7}]
movies = [{'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8},
          {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6},
          {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7},
          {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6},
          {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9},
          {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8},
          {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9},
          {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8},
          {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10},
          {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7},
          {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5},
          {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8},
          {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}]

conn = engine.connect()
insert_directors = insert(Director)
conn.execute(insert_directors, directors)
insert_movies = insert(Movie)
conn.execute(insert_movies, movies)
conn.close()
