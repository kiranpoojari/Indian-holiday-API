import json
from api.models import Holiday
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('india_2024.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            Holiday.objects.create(
                name=item['name'],
                date=item['date'],
                local_name=item['localName'],
                country_code=item['countryCode'],
                types=','.join(item.get('types', []))
            )
