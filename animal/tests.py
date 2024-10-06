from rest_framework.test import APITestCase
from django.urls import reverse
from .models import MilkProduction, AnimalBase


class MilkProductionViewTest(APITestCase):
    def setUp(self):
        self.animal = AnimalBase.objects.create(animal_name="Test Animal")
        self.milk_production = MilkProduction.objects.create(
            animal=self.animal,
            date_of_production="2023-10-01",
            morning_quantity=5.0,
            evening_quantity=3.0,
        )

    def test_get_daily_production(self):
        url = reverse("milk_production-list")
        response = self.client.get(
            url, {"animal_id": self.animal.id, "date": "2023-10-01"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_daily_quantity"], 8.0)

    def test_get_production_in_range(self):
        url = reverse("milk_production-list")
        response = self.client.get(
            url,
            {
                "animal_id": self.animal.id,
                "start_date": "2023-10-01",
                "end_date": "2023-10-31",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_weekly_and_monthly_totals(self):
        url = reverse("milk_production-list")
        response = self.client.get(url, {"animal_id": self.animal.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn("weekly_total", response.data)
        self.assertIn("monthly_total", response.data)

    def test_invalid_query_parameters(self):
        url = reverse("milk_production-list")
        response = self.client.get(url, {"invalid_param": "invalid"})
        self.assertEqual(response.status_code, 400)
