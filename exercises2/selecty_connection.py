from sqlalchemy import select, and_, between, or_, join, func, text
from sqlalchemy.orm import sessionmaker
from exercises2.ex2 import engine, Movies, Directors


conn = engine.connect()

# select_query = select([Movies]).where(Movies.category == "Crime", Movies.year >= 1994)
# result = conn.execute(select_query)
# print(result.fetchall())
########################################################################

# select_query2 = select([Movies.category, Movies.title, Movies.rating]).where(
#     and_(Movies.rating > 7, between(Movies.year, 2000, 2010))
# ).order_by(Movies.rating.desc())
# result = conn.execute(select_query2)
# print(result.fetchall())

#####################################################################

# select_query3 = select([Directors.name, Directors.surname]).where(
#     and_(Directors.rating >= 6, or_(Directors.name.like("D%"), Directors.name.like("%n")))
# )
# result = conn.execute(select_query3)
# print(result.fetchall())

###################################################################

# select_query4 = select(Directors.name, Directors.surname).select_from(
#     join(Directors, Movies)
# ).where(and_(between(Movies.year, 2011, 2014), Movies.rating < 9))
# result = conn.execute(select_query4)
# print(result.fetchall())

###################################################################

# select_query5 = select(
#     Directors.name,
#     Directors.surname,
#     func.count(Movies.id),
#     func.avg(Movies.rating)
# ).select_from(
#     join(Directors, Movies)
# ).group_by(
#     Directors.id
# )
# result = conn.execute(select_query5)
# print(result.fetchall())
# print(select_query5) ### printuje surowe zapytanie sql

##################################################################

#### zadanie 5 poprzednie zadanie sformatuj do postaci tekstowej
#### uzywajac text(). Zmodyfikuj je tak , aby mozna bylo uzyc tego zapytania podajac
#### przedzial lat , w ktorych rezyserowie tworzyli filmy jako parametr do zapytania
raw_sql = text("""
SELECT directors.name, directors.surname, count(movies.id) AS count_1, avg(movies.rating) AS avg_1
FROM directors JOIN movies ON directors.id = movies.director_id
WHERE movies.year BETWEEN :start_year AND :end_year
GROUP BY directors.id
""")
select_query6 = conn.execute(raw_sql, start_year=1950, end_year=2020).fetchall()
result = conn.execute(select_query6)
print(result.fetchall())
conn.close()
# #############################################################################



