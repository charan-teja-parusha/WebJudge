from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from members.models import Member


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the amazon mobile review data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from amazon_mobile.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Member.objects.exists():
            print('amazon reviews data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading amazon reviews data")


        #Code to load the data into database
        for row in DictReader(open('./Amazon_Mobile.csv',encoding='cp850')):
            try:
                votes = int(row['Review Votes'])
            except ValueError:
                votes=0
            try:
                cost = int(row['Price'])
            except ValueError:
                cost=0
            try:
                rate = int(row['Rating'])
            except ValueError:
                rate=0
            #if(row['Review Votes']!='' or row['Review Votes']!='NA'):
            #    votes=int(row['Review Votes'])
            #else:
            #    votes=0
            #if(row['Price']!='' or row['Price']!='NA'):
            #    cost=int(row['Review Votes'])
            #else:
            #    cost=0
            #if(row['Rating']!='' or row['Rating']!='NA'):
            #    rate=int(row['Review Votes'])
            #else:
            #    rate=0
            member=Member(productname=row['Product Name'], brandname=row['Brand Name'], price=cost,ratings=rate, reviews=row['Reviews'], reviewvotes=votes)  
            member.save()