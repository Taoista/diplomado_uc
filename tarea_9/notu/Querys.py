import mysql.connector as db
import csv


def resultados(select):
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )
    cursor = mydb.cursor() 
    
    query = ""

    if select == 1:
        query = "SELECT d.last_name, d.first_name, COUNT(movie_id) AS 'How Many'\
                    FROM movies_directors AS md\
                    JOIN directors AS d\
                    ON d.id = md.director_id\
                    GROUP BY d.last_name, d.first_name\
                    HAVING COUNT(movie_id) > 3\
                    ORDER BY COUNT(movie_id) DESC"
    elif select == 2:
        query = "SELECT a.last_name, a.first_name, COUNT(movie_id)\
                    FROM actors AS a\
                    JOIN movies_actors AS ma\
                    ON ma.actor_id = a.id\
                    GROUP BY a.last_name, a.first_name\
                    ORDER BY a.last_name, a.first_name"
    elif select == 3:
        query = "SELECT m.name AS Movie, m.year AS Year, d.last_name AS Director, m.ranking AS Ranking\
                    FROM (movies_directors AS md\
                            JOIN movies AS m on m.id = md.movie_id)\
                    JOIN directors AS d ON d.id = director_id\
                    WHERE m.ranking > 8\
                    ORDER BY m.ranking\
                    DESC"


    cursor.execute(query)
    rows = cursor.fetchall()

    return rows


