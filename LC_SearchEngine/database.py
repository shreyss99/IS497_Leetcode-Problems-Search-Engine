from django.db import connection
from .models import LeetcodeData


def get_data():
    # with connection.cursor() as cursor:
    #     cursor.execute(""" SELECT id, title, url FROM "LC_SearchEngine_leetcodedata" """)
    #     rows = cursor.fetchall()
    # return rows

    """ TEMP QUERY
    Need to make use of user parameters
    """
    data = LeetcodeData.objects.filter(title__regex=r'',
                                       is_premium=0,
                                       acceptance_rate__gte=37,
                                       difficulty__regex=r'').all()
    return data
