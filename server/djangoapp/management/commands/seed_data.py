from django.core.management.base import BaseCommand
import json
import os
from djangoapp.models import Dealership, Review

class Command(BaseCommand):
    help = 'Load dealership and review data from JSON files'

    def handle(self, *args, **kwargs):
        # Path to JSON files
        # Current file is in server/djangoapp/management/commands/
        # We need to go up 3 levels to get to 'server/djangoapp'
        # Then 1 more to 'server'
        current_dir = os.path.dirname(os.path.abspath(__file__))
        server_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
        
        # Check if we are too deep (e.g. if the file is command.py inside a package)
        # Let's try absolute path based on known structure
        # Expected: .../server/database/data
        
        # Fallback: Look for 'server' in the path and truncate there
        if 'server' in current_dir:
            server_dir = current_dir.split('server')[0] + 'server'
        else:
             # Assume we are running from server root via manage.py usually
             server_dir = os.getcwd()

        data_dir = os.path.join(server_dir, 'database', 'data')
        
        dealerships_path = os.path.join(data_dir, 'dealerships.json')
        reviews_path = os.path.join(data_dir, 'reviews.json')

        # Load Dealerships
        self.stdout.write("Loading Dealerships...")
        try:
            with open(dealerships_path, 'r') as f:
                data = json.load(f)
                dealerships = data['dealerships']
                for dealer in dealerships:
                    Dealership.objects.update_or_create(
                        id=dealer['id'],
                        defaults={
                            'city': dealer['city'],
                            'state': dealer['state'],
                            'address': dealer['address'],
                            'zip': dealer['zip'],
                            'lat': dealer['lat'],
                            'long': dealer['long'],
                            'short_name': dealer['short_name'],
                            'full_name': dealer['full_name']
                        }
                    )
            self.stdout.write(self.style.SUCCESS("Dealerships loaded successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading dealerships: {str(e)}"))

        # Load Reviews
        self.stdout.write("Loading Reviews...")
        try:
            with open(reviews_path, 'r') as f:
                data = json.load(f)
                reviews = data['reviews']
                for rev in reviews:
                    # Find dealership instance
                    try:
                        dealer = Dealership.objects.get(id=rev['dealership'])
                        Review.objects.update_or_create(
                            id=rev['id'],
                            defaults={
                                'dealership': dealer,
                                'name': rev['name'],
                                'review': rev['review'],
                                'purchase': rev['purchase'],
                                'purchase_date': rev.get('purchase_date', ''),
                                'car_make': rev.get('car_make', ''),
                                'car_model': rev.get('car_model', ''),
                                'car_year': rev.get('car_year', 0),
                            }
                        )
                    except Dealership.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"Dealership {rev['dealership']} not found for review {rev['id']}"))

            self.stdout.write(self.style.SUCCESS("Reviews loaded successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading reviews: {str(e)}"))
