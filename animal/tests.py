from django.test import TestCase
from django.utils import timezone
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AInotPredeterminedServiced,
    AIPredeterminedServiced,
    TreatmentRecords,
    MedicineTreatment,
    Dosagetreatment,
)

class RecordTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(name="TestCow")
        self.treatment_record = TreatmentRecords.objects.create(
            animal=self.animal,
            date_of_diagnosis=timezone.now(),
        )
        self.assertEqual(self.treatment_record.animal, self.animal)

    def test_medicine_treatment(self):
        medicine_treatment = MedicineTreatment.objects.create(
            animal = self.treatment_record,
            name_of_vet="TestVet",
            date_of_medicine_treatment=timezone.now(),
        )
        self.assertEqual(medicine_treatment.name_of_vet, "TestVet")

    def test_dosage_treatment(self):
        dosage_treatment = Dosagetreatment.objects.create(
            animal = self.treatment_record,
            name_of_vet="TestVet",
            date_of_medicine_treatment=timezone.now(),
            dosage_treatment_used="TestDosage",
        )
        self.assertEqual(dosage_treatment.name_of_vet, "TestVet")
        self.assertEqual(dosage_treatment.dosage_treatment_used, "TestDosage")

class ModelTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            name="TestCow", breed="Holstein", gender="F", source="purchased"
        )

    def test_purchased_creation(self):
        """Test the creation of a purchased object."""
        purchased = Purchased.objects.create(
            animal=self.animal, seller_name="TestSeller", date_purchased=timezone.now()
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
        ai_not_predetermined = AInotPredeterminedServiced.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )
        self.assertEqual(ai_not_predetermined.animal, self.animal)

    def test_ai_predetermined(self):
        ai_predetermined = AIPredeterminedServiced.objects.create(
            animal=self.animal,
            date_of_service=timezone.now(),
            birth_date=timezone.now(),
        )
        self.assertEqual(ai_predetermined.animal, self.animal)
