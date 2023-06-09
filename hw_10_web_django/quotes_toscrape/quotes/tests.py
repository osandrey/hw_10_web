# from bson import ObjectId
# from psycopg2 import connect
# from django.test import TestCase
#
# from hw_10_web_django.quotes_toscrape.quotes.utils import get_mongo_db
#
#
# # Create your tests here.
# def get_author_from_postgres(fullname):
#     conn = connect(
#         database="postgres",
#         user="postgres_quotes",
#         password="567234",
#         host="localhost",
#         port='5432'
#     )
#
#     cursor = conn.cursor()
#     cursor.execute("SELECT id FROM quotes_author WHERE fullname = %s", (fullname,))
#     author = cursor.fetchone()
#     print(author[0])
#     return author
#
#
# get_author_from_postgres('Albert Einstein')
#
# def get_author_obj(_id):
#
#     db = get_mongo_db()
#     author = db.author.find_one({'_id': ObjectId(_id)})
#     return author['bio']
#
# print(get_author_obj('647f6935a60a576c43769462'))
#
#
# object_id = ObjectId('647f6935a60a576c43769466')
#
# # Convert the ObjectId to a hexadecimal string
# hex_str = str(object_id)
#
# # Convert the hexadecimal string to an integer
# integer_value = int(hex_str, 16)
#
# # Print the integer value
# print(integer_value)
