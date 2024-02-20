import requests

from app.models import D_CLUB


class Geocoding:

    def get_departement(self, value):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'key': 'AIzaSyBC1OnjBomcXWYcCtL6N7LwTWwQiXlFpws',
            'address': value
        }

        result = requests.get(url, params=params)
        data = result.json()

        if 'results' in data and data['results']:
            address_components = data['results'][0]['address_components']
            if len(address_components) >= 2:
                return address_components[1]['long_name']

        return "Département non trouvé"

def run():
    geo = Geocoding()
    geocoding = D_CLUB.objects.values_list('code_code_qpv_code_commune', 'code_commune', 'commune').distinct()
    for code_code_qpv_code_commune, code_commune, commune in geocoding:
        value = f"{code_commune} - {commune}"
        department = geo.get_departement(value)
        print(f"Code commune: {code_commune}, Commune: {commune}, Department: {department}")

        instance = D_CLUB.objects.get(pk=code_code_qpv_code_commune)
        instance.nom_departement = department
        instance.save()