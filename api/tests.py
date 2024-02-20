from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import API_Store_City
from app.models import City
import json

class TestCities(TestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = API_Store_City.as_view()
        self.test_city = City.objects.create(
            postal_code="10000",
            name="Test City",
            departement="Test Department",
            region="Test Region",
            country="Test Country"
        )

    def test_get_city_list(self):
        request = self.factory.get('/formation/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['count'], City.objects.count())

    def test_get_city_detail(self):
        request = self.factory.get(f'/formation/{self.test_city.postal_code}/')
        response = self.view(request, postal_code=self.test_city.postal_code)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['data'][0]['postal_code'], self.test_city.postal_code)

    def test_create_city(self):
        new_city_data = {
            'postal_code': '12345',
            'name': 'Test City',
            'departement': 'Test Departement',
            'region': 'Test Region',
            'country': 'Test Country'
        }
        request = self.factory.post('/formation/', new_city_data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(City.objects.count(), 2)

    def test_update_city(self):
        updated_data = {
            'postal_code': '20000',
            'name': 'Updated City Name',
            'departement': self.test_city.departement,
            'region': 'Updated Region',
            'country': self.test_city.country
        }
        request = self.factory.put(f'/formation/{self.test_city.postal_code}/', updated_data, format='json')
        response = self.view(request, postal_code=self.test_city.postal_code)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, 200)
        updated_city = City.objects.get(postal_code=updated_data['postal_code'])
        self.assertEqual(updated_city.name, updated_data['name'])
        self.assertEqual(updated_city.region, updated_data['region'])

    def test_partial_update_city(self):
        updated_data = {
            'name': 'Updated City Name',
        }
        request = self.factory.patch(f'/formation/{self.test_city.postal_code}/', updated_data, format='json')
        response = self.view(request, postal_code=self.test_city.postal_code)
        self.assertEqual(response.status_code, 200)
        updated_city = City.objects.get(postal_code=self.test_city.postal_code)
        self.assertEqual(updated_city.name, updated_data['name'])

    def test_delete_city(self):
        request = self.factory.delete(f'/formation/{self.test_city.postal_code}/')
        response = self.view(request, postal_code=self.test_city.postal_code)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(City.objects.filter(postal_code=self.test_city.postal_code).exists())

