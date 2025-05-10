from django.test import TestCase
from django.urls import reverse


class DaycareViewsTests(TestCase):
    """Tests for daycare app views."""

    def test_index_view(self):
        """Test that the index view returns a 200 status code."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "daycare/index.html")

    def test_set_language_fr(self):
        """Test that setting language to French redirects correctly."""
        response = self.client.get(reverse("set_language", args=["fr"]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.cookies["django_language"].value, "fr")

    def test_set_language_en(self):
        """Test that setting language to English redirects correctly."""
        response = self.client.get(reverse("set_language", args=["en"]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.cookies["django_language"].value, "en")
