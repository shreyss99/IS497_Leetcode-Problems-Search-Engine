from LC_SearchEngine.models import LeetcodeData
from django.db import connection

def get_data():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM "LC_SearchEngine_leetcodedata" where difficulty = 'Easy'""")
        rows = cursor.fetchall()
    return rows
