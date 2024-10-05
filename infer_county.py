import csv
from geopy.geocoders import Nominatim
from time import sleep

# Initialize geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Open your CSV file
with open('adult_monarch_sightings.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Assuming your file has columns: 'Town', 'State/Province'
    fieldnames = csv_reader.fieldnames + ['County']
    
    # Open a new file to write results
    with open('city_data_with_county.csv', mode='w', newline='') as result_file:
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in csv_reader:
            city = row['City']
            state = row['State']
            location = geolocator.geocode(f"{city}, {state}", timeout=10) 
            sleep(10)  # Sleep to avoid hitting request limits
            
            if location:
                # Parse county from location.raw
                county = None
                for component in location.raw['address']:
                    if 'county' in component:
                        county = location.raw['address']['county']
                        break

                row['County'] = county
            else:
                row['County'] = "Not found"
            
            writer.writerow(row)
