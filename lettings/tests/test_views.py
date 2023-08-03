from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Letting, Address


class LettingViewsTest(TestCase):
    def setUp(self):
        """
        Set up the test by creating a Client instance
            and some Letting and Address objects.
        """
        self.client = Client()
        self.address = Address.objects.create(
            number=123, street="Main St", city="Cityville", state="NY",
            zip_code=12345, country_iso_code="USA")
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address)

    def test_index_view(self):
        """
        Test that the 'index' view returns a 200 status code,
            uses the correct template, and contains the expected content.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, "Test Letting")

    def test_letting_view(self):
        """
        Test that the 'letting' view returns a 200 status code,
            uses the correct template, and contains the expected content.
        """
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "123 Main St")

    def test_letting_view_invalid_id(self):
        """
        Test that the 'letting' view handles an invalid id
            by displaying an error template.
        """
        invalid_id = 9999999
        response = self.client.get(
            reverse('lettings:letting', args=[invalid_id]))
        self.assertTemplateUsed(response, 'error.html')
