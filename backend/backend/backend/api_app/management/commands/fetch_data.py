from django.core.management.base import BaseCommand
import requests
from django.utils import timezone
from api_app.models import DataPoint

class Command(BaseCommand):
    help = 'Fetch sample data from an external API and save as DataPoint'

    def handle(self, *args, **options):
        # example: fetch bitcoin price
        url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            price = float(data['bpi']['USD']['rate_float'])
            DataPoint.objects.create(name='bitcoin_usd', value=price, ts=timezone.now(), meta={'source':'coindesk'})
            self.stdout.write(self.style.SUCCESS('Saved datapoint'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Fetch failed: {e}'))
