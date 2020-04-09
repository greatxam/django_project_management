# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Initializing Agile App."

    def handle(self, *args, **options):
        call_command('loaddata', 'agile_values.json')
        call_command('loaddata', 'agile_principles.json')
