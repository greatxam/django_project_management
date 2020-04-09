# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from agile.tests.helpers import PrincipleTestHelper


class PrincipleAPITestCase(APITestCase):
    fixtures = ['agile_principles.json']

    def test_list_principle(self):
        """
        Listing agile principle.

        :return:
        """
        response = self.client.get(reverse(PrincipleTestHelper.API_LIST_PRINCIPLE))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('count'), 12)

    def test_create_principle(self):
        """
        Creating new agile principle.

        :return:
        """
        payload = {
            'name': 'New Test Principle',
        }
        response = self.client.post(reverse(PrincipleTestHelper.API_LIST_PRINCIPLE), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        self.assertEqual(response.data.get('name'), payload['name'])

    def test_detail_principle(self):
        """
        Getting the agile principle detail.

        :return:
        """
        principle = PrincipleTestHelper.get_principle("Simplicity")
        response = self.client.get(reverse(PrincipleTestHelper.API_DETAIL_PRINCIPLE, kwargs={'pk': principle.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('name'), principle.name)

    def test_change_principle(self):
        """
        Changing the agile principle.

        :return:
        """
        principle = PrincipleTestHelper.get_principle("Simplicity")
        payload = {
            'name': "Principle 1 New Name"
        }
        response = self.client.put(reverse(PrincipleTestHelper.API_DETAIL_PRINCIPLE, kwargs={'pk': principle.pk}), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('name'), payload['name'])

    def test_delete_principle(self):
        """
        Deleting agile principle is not allowed.

        :return:
        """
        principle = PrincipleTestHelper.get_principle("Simplicity")
        response = self.client.delete(reverse(PrincipleTestHelper.API_DETAIL_PRINCIPLE, kwargs={'pk': principle.pk}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED, response.content)
