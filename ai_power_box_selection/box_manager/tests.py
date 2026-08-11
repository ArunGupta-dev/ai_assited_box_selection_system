from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from box_manager.models import Box

class BoxSelectionAPITests(APITestCase):
    
    def setUp(self):
        self.box = Box.objects.create(
            name="Test Medium Box",
            length=30.0,
            width=20.0,
            height=15.0,
            max_weight=5.0,
            cost=2.50
        )
        self.api_url = '/box/selection/get/'  # Update if your URL is different

    def test_single_item_fits(self):
        """Test that a small, light item successfully finds the box."""
        payload = {
            "order_id": "TEST-1",
            "items": [{
                "name": "Mouse", "length": 10.0, "width": 5.0, "height": 3.0, "weight": 0.5, "quantity": 1
            }]
        }
        response = self.client.post(self.api_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['best_box']['name'], "Test Medium Box")

    def test_item_too_heavy(self):
        payload = {
            "order_id": "TEST-2",
            "items": [{
                "name": "Dumbbell", "length": 10.0, "width": 10.0, "height": 10.0, "weight": 10.0, "quantity": 1
            }]
        }
        response = self.client.post(self.api_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['best_box']['code'], "not-possible-in-single-box")

    def test_item_too_large(self):
        """Test that an item that is physically too long for the box is rejected."""
        payload = {
            "order_id": "TEST-3",
            "items": [{
                "name": "Long Sword", "length": 50.0, "width": 5.0, "height": 5.0, "weight": 2.0, "quantity": 1
            }]
        }
        response = self.client.post(self.api_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['best_box']['code'], "not-possible-in-single-box")

    def test_multiple_items_fit(self):
        """Tast that the algorithm unrolls quantities and fits multiple items."""
        payload = {
            "order_id": "TEST-4",
            "items": [{
                "name": "Rubiks Cube", "length": 5.0, "width": 5.0, "height": 5.0, "weight": 0.5, "quantity": 4
            }]
        }
        response = self.client.post(self.api_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['best_box']['name'], "Test Medium Box")
