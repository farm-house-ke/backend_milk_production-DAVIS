from django.test import TestCase
from django.utils import timezone
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)


class AnimalModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name="Bella",
            breed="Labrador",
            gender="F",
            date_of_next_service=timezone.now(),
            source="purchased",
        )

    def test_animal_creation(self):
        self.assertEqual(self.animal.name, "Bella")
        self.assertEqual(self.animal.breed, "Labrador")
        self.assertEqual(self.animal.gender, "F")
        self.assertEqual(self.animal.source, "purchased")
        self.assertIsNotNone(self.animal.date_of_next_service)

    def test_animal_str(self):
        self.assertEqual(str(self.animal), self.animal.name)


class PurchasedModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name="Bella",
            breed="Labrador",
            gender="F",
        )
        self.purchased = Purchased.objects.create(
            animal=self.animal,
            seller_name="John Doe",
            date_purchased=timezone.now(),
        )

    def test_purchased_creation(self):
        self.assertEqual(self.purchased.animal, self.animal)
        self.assertEqual(self.purchased.seller_name, "John Doe")

    def test_purchased_str(self):
        self.assertEqual(str(self.purchased), str(self.animal))


class LocallyServicedModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name="Bella",
            breed="Labrador",
            gender="F",
        )
        self.locally_serviced = LocallyServiced.objects.create(
            animal=self.animal,
            name_of_owner="Jane Doe",
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )

    def test_locally_serviced_creation(self):
        self.assertEqual(self.locally_serviced.animal, self.animal)
        self.assertEqual(self.locally_serviced.name_of_owner, "Jane Doe")

    def test_locally_serviced_str(self):
        self.assertEqual(str(self.locally_serviced), str(self.animal))


class AIPredeterminedServiceAnimalModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name="Bella",
            breed="Labrador",
            gender="F",
        )
        self.ai_predetermined = AIPredeterminedServiceAnimal.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )

    def test_ai_predetermined_creation(self):
        self.assertEqual(self.ai_predetermined.animal, self.animal)
        self.assertEqual(self.ai_predetermined.gender, "female")

    def test_ai_predetermined_str(self):
        self.assertEqual(str(self.ai_predetermined), str(self.animal))


class AInonPredeterminedServiceAnimalModelTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            name="Molly", breed="Jersey", gender="F", source="ai_non_predetermined"
        )

        self.ai_non_predetermined = AInonPredeterminedServiceAnimal.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )

    def test_ai_non_predetermined_creation(self):
        self.assertEqual(self.ai_non_predetermined.animal, self.animal)

    def test_api_non_predetermined_str(self):
        self.assertEqual(str(self.ai_non_predetermined), str(self.animal))
