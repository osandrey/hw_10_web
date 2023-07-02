from django.test import TestCase

# Create your tests here.
from django.db import connection


def check_connected_database():
    # Get the name of the currently connected database
    database_name = connection.settings_dict['NAME']

    # Print the database name
    print(f"Connected database: {database_name}")


check_connected_database()