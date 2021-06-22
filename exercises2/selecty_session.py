

# Przy pomocy Sesji
from sqlalchemy import select, and_, between, or_, join, func, text, subquery
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
from exercises2.ex2 import engine, Movies, Directors

Session = sessionmaker(bind=engine, autocommit=False)  ### dodatek do zad o transakcji
session = Session()


######################################################################################
result = session.query(Movies).all()
print(result)
# result = session.query(Movies).filter(Movies.category == "Crime", Movies.year >= 1994).all()
# for movie in result:
#     print(f"Film {movie.title} został nakręcony w {movie.year} roku")


#######################################################################################
# result2 = session.query(Movies.category, Movies.title, Movies.rating).filter(
#     and_(Movies.rating > 7, between(Movies.year, 2000, 2010))
# ).order_by(Movies.rating.desc()).all()


#######################################################################################
# result3 = session.query(Directors).filter(
#     and_(Directors.rating >= 6, or_(Directors.name.like("D%"), Directors.name.like("%n")))
# ).all()


#######################################################################################
# result4 = session.query(Directors.name, Directors.surname).join(Movies).filter(
#     and_(between(Movies.year, 2011, 2014), Movies.rating < 9)
# ).all()


######################################################################################
# result5 = session.query(
#     Directors.name,
#     Directors.surname,
#     func.count(Movies.id),
#     func.avg(Movies.rating)
# ).join(
#     Movies
# ).group_by(
#     Directors.id
# )
# print(result5)


######################################################################################
#### zadanie 5 poprzednie zadanie sformatuj do postaci tekstowej
#### uzywajac text(). Zmodyfikuj je tak , aby mozna bylo uzyc tego zapytania podajac
#### przedzial lat , w ktorych rezyserowie tworzyli filmy jako parametr do zapytania
# raw_sql = text("""
# SELECT directors.name, directors.surname, count(movies.id) AS count_1, avg(movies.rating) AS avg_1
# FROM directors JOIN movies ON directors.id = movies.director_id
# WHERE movies.year BETWEEN :start_year AND :end_year
# GROUP BY directors.id
# """)
# result = session.query(
#     text("name"), text("surname"), text("count_1"), text("avg_1")
# ).from_statement(raw_sql).params(start_year=1950, end_year=2020).all()
# print(result)


######################################################################################
#### do poprzedniego zapytania tekstowego zbinduj patrametry korzystając z bind_params() okreslajac wymagane typy
# raw_sql = text("""
# SELECT directors.name, directors.surname, count(movies.id) AS count_1, avg(movies.rating) AS avg_1
# FROM directors JOIN movies ON directors.id = movies.director_id
# WHERE movies.year BETWEEN :start_year AND :end_year
# GROUP BY directors.id
# """).bindparams(
#     start_year=1950, end_year=2020
# )
# result = session.query(
#     Directors.name, Directors.surname, text("count_1"), text("avg_1")
# ).from_statement(raw_sql).all()


######################################################################################
#### utworzone zapytanie opakuj w funkcję przyjmująca paramestry(session, dwa paramatery przedziału lat)
# def get_director_statistics(sess, start_year, end_year):
#     result = sess.query(Directors.name, Directors.surname).join(Movies).filter(
#         and_(between(Movies.year, start_year, end_year), Movies.rating < 9)
#     ).all()
#     return result

# print(get_director_statistics(session, 2011, 2015))
# ### rozwiazanie trenera
# def get_director_statistics(sess, start_year, end_year):
#     raw_sql = text("""
#     SELECT directors.name, directors.surname, count(movies.id) AS count_1, avg(movies.rating) AS avg_1
#     FROM directors JOIN movies ON directors.id = movies.director_id
#     WHERE movies.year BETWEEN :start_year AND :end_year
#     GROUP BY directors.id
#     """).bindparams(
#         start_year=start_year, end_year=end_year
#     )
#     result = sess.query(
#         Director.name, Director.surname, text("count_1"), text("avg_1")
#     ).from_statement(raw_sql).all()
#     return result
######################################################################################
### wszystkim reżyserom ktorych filmy zostaly wyprodukowane przed 2001 rokiem oraz ich tytuł zaczyna
### się na litere T, zwiększ rating o 1. Skorzystaj z podzapytania
#
# subquery = session.query(Movies.director_id).filter(
#     and_(Movies.year < 2001, Movies.title.like("T%"))
# ).distinct()
# session.query(Directors).filter(
#     Directors.id.in_(subquery)
# ).update(
#     {"rating": Directors.rating - 1}, synchronize_session=False
# )
# session.commit()

######################################################################################
### przy pomocy transakcji usun rezyser o imieniu frank
# with session.begin():
#     subquery = session.query(Directors.id).filter(Directors.name == "Quentin")
#     session.query(Movies).filter(Movies.director_id.in_(subquery)).delete(synchronize_session=False)
#     session.query(Directors).filter(Directors.name == "Frank").delete()


######################################################################################
### utworzoną w poprzednim zadaniu transakcję opakuj w funkcje ktora bedzie przyjmowac imie i nazwisko jako kwargs
### funkcja na podstawi podanego imienia lub nazwiska bedzie decydowac ktorego query uzyć do wyszukania rezysera
### a następnie go usunie
# def delete_director(**kwargs):
#     if "session" in kwargs:
#         session = kwargs["session"]
#     else:
#         session = Session()
#     if "name" in kwargs:
#         condition = Directors.name == kwargs["name"]
#     elif "surname" in kwargs:
#         condition = Directors.surname == kwargs["surname"]
#     else:
#         raise ValueError("Neither name nor surname provided")
#     with session.begin():
#         subquery = session.query(Directors.id).filter(condition)
#         session.query(Movies).filter(Movies.director_id.in_(subquery)).delete(synchronize_session=False)
#         session.query(Directors).filter(condition).delete()
#
#
# delete_director(surname="Fincher")


######################################################################################
###Stwórz 2 funkcje: add_director() add_movie() które pozwolą na dodanie reżyserów i filmów. Pamiętaj o użyciu transakcji.

# def add_director(name:str, surname:str, rating:int, database, **sess):
#     if "session" in sess:
#         session = sess["session"]
#     else:
#         session = Session()
#
#     with session.begin():
#         result = session.database.add(Directors(name, surname, rating))
#     return result
#
#
# add_director('Tom', 'Hanks', 7, "//cinematic3.db")
######################################################################################


session.close()
