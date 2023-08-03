from django.core.exceptions import ValidationError
from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    def test_address_str_representation(self):
        """
        Test the string representation of the Address model.
        """
        address = Address(number=123, street="Main St", city="Cityville",
                          state="NY", zip_code=12345, country_iso_code="USA")
        self.assertEqual(str(address), "123 Main St")

    def test_address_max_value_validation(self):
        """
        Test the maximum value validation for fields in the Address model.
        """
        with self.assertRaises(ValidationError):
            Address(number=10000, street="Street", city="City", state="CA",
                    zip_code=12345, country_iso_code="USA").full_clean()

    def test_address_min_length_validation(self):
        """
        Test the minimum length validation for fields in the Address model.
        """
        with self.assertRaises(ValidationError):
            Address(number=123, street="St", city="City", state="C",
                    zip_code=12345, country_iso_code="USA").full_clean()


class LettingModelTest(TestCase):
    def test_letting_str_representation(self):
        """
        Test the string representation of the Letting model.
        """
        address = Address.objects.create(
            number=123, street="Main St", city="Cityville",
            state="NY", zip_code=12345, country_iso_code="USA")
        letting = Letting(title="Test Letting", address=address)
        self.assertEqual(str(letting), "Test Letting")
