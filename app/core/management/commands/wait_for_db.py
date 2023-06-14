"""
Django command to wait to database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2upError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entry point for command"""

        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2upError, OperationalError):
                self.stdout.write('Database unavilable, wait 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available'))