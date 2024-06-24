from django.test import TestCase
from django.utils import timezone
import uuid
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AInonPredeterminedServiceAnimal,
    AIPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)
from .serializers import AnimalSerializer


class AnimalSerializerTest(TestCase):
    """test for animal serializer."""

    def create_animal(self, source):
        unique_name = "TestAnimal_" + str(uuid.uuid4())
        animal_data = {
            "name": unique_name,
            "breed": "TestBreed",
            "gender": "F",
            "date_of_next_service": "2023-01-01",
            "source": source,
        }
        serializer = AnimalSerializer(data=animal_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())
        animal = serializer.save()
        if source == "purchased":
            purchased = Purchased.objects.create(animal=animal)
            purchased.save()
            self.assertTrue(Purchased.objects.filter(animal=animal).exists())
        elif source == "locally_serviced":
            locally_serviced = LocallyServiced.objects.create(animal=animal)
            locally_serviced.save()
            self.assertTrue(LocallyServiced.objects.filter(animal=animal).exists())
        elif source == "ai_predetermined":
            ai_predetermined = AIPredeterminedServiceAnimal.objects.create(
                animal=animal
            )
            ai_predetermined.save()
            self.assertTrue(
                AIPredeterminedServiceAnimal.objects.filter(animal=animal).exists()
            )
        elif source == "ai_not_predetermined":
            ai_not_predetermined = AInonPredeterminedServiceAnimal.objects.create(
                animal=animal
            )
            ai_not_predetermined.save()
            self.assertTrue(
                AInonPredeterminedServiceAnimal.objects.filter(animal=animal).exists()
            )
        return animal

    def test_create_animal_with_different_sources(self):
        sources = [
            "purchased",
            "locally_serviced",
            "ai_predetermined",
            "ai_not_predetermined",
        ]
        for source in sources:
            with self.subTest(source=source):
                self.create_animal(source)


class RecordTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            name="TestCow",
        )
        self.assertEqual(self.animal, "TestCow")

    def test_medicine_treatment(self):
        medicine_treatment = MedicineTreatment.objects.create(
            animal="TestCow",
            date_of_diagnosis=timezone.now(),
            name_of_vet="TestVet",
            date_of_medicine_treatment=timezone.now(),
        )
        self.assertEqual(medicine_treatment.name_of_vet, "TestVet")
        self.assertEqual(medicine_treatment.animal, "TestCow")

    def test_dosage_treatment(self):
        dosage_treatment = Dosagetreatment.objects.create(
            animal="TestCow",
            date_of_diagnosis=timezone.now(),
            name_of_vet="TestVet",
            date_of_medicine_treatment=timezone.now(),
            dosage_treatment_used="TestDosage",
        )
        self.assertEqual(dosage_treatment.name_of_vet, "TestVet")
        self.assertEqual(dosage_treatment.dosage_treatment_used, "TestDosage")
        self.assertEqual(dosage_treatment.animal, "TestCow")


class ModelTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            name="TestCow", breed="Holstein", gender="F", source="purchased"
        )

    def test_purchased_creation(self):
        """Test the creation of a purchased object."""
        purchased = Purchased.objects.create(
            animal=self.animal,
            seller_name="TestSeller",
            date_purchased=timezone.now(),
        )
        self.assertEqual(purchased.animal, self.animal)
        self.assertEqual(purchased.seller_name, "TestSeller")

    def test_locally_serviced(self):
        locally_serviced = LocallyServiced.objects.create(
            animal=self.animal,
            name_of_owner="TestOwner",
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )
        self.assertEqual(locally_serviced.animal, self.animal)
        self.assertEqual(locally_serviced.name_of_owner, "TestOwner")

    def test_ai_not_predetermined(self):
        ai_not_predetermined = AInonPredeterminedServiceAnimal.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )
        self.assertEqual(ai_not_predetermined.animal, self.animal)

    def test_ai_predetermined(self):
        ai_predetermined = AIPredeterminedServiceAnimal.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )
        self.assertEqual(ai_predetermined.animal, self.animal)
