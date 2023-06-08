from django import template

from psycopg2 import connect
register = template.Library()


def get_author_from_postgres(_id):
    conn = connect(
        database="postgres",
        user="postgres_quotes",
        password="567234",
        host="localhost",
        port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT fullname FROM author WHERE id = %s", (_id,))
    author = cursor.fetchone()
    print(author[0])
    return author[0]



register.filter('get_author_from_postgres', get_author_from_postgres)