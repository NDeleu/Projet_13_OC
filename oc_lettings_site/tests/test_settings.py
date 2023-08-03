from django.test import TestCase
from django.db import connection


class OCLettingsSiteSettingsTest(TestCase):

    def test_database_connection(self):
        """
        Test the database connection by executing a simple query
            and checking the result.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            self.assertEqual(cursor.fetchone()[0], 1)
