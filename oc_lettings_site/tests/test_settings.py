from django.test import TestCase
from django.conf import settings
from django.db import connection


class OCLettingsSiteSettingsTest(TestCase):

    def test_database_connection(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            self.assertEqual(cursor.fetchone()[0], 1)
