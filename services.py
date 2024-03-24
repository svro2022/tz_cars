import csv
from delivery.models import Location


def load_locations_from_csv():
    '''Функция загрузки данных из файла uszips.csv'''
    with open('uszips.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            zip_code = row["zip"]
            city = row["city"]
            state = row["state_name"]
            latitude = row["lat"]
            longitude = row["lng"]

            Location.objects.create(zip_code=zip_code, city=city, state=state, latitude=latitude, longitude=longitude)
