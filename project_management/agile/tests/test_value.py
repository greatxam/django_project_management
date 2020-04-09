# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from agile.tests.helpers import ValueTestHelper


class ValueAPITestCase(APITestCase):
    fixtures = ['agile_values.json']

    def test_list_value(self):
        """
        Listing agile value.

        :return:
        """
        response = self.client.get(reverse(ValueTestHelper.API_LIST_VALUE))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('count'), 4)

    def test_create_value(self):
        """
        Creating new agile value.

        :return:
        """
        payload = {
            'name': 'New Test Value',
        }
        response = self.client.post(reverse(ValueTestHelper.API_LIST_VALUE), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        self.assertEqual(response.data.get('name'), "New Test Value")

    def test_detail_value(self):
        """
        Getting the agile value detail.

        :return:
        """
        value = ValueTestHelper.get_value("Value 1")
        response = self.client.get(reverse(ValueTestHelper.API_DETAIL_VALUE, kwargs={'pk': value.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('name'), "Value 1")

    def test_change_value(self):
        """
        Changing the agile value.

        :return:
        """
        value = ValueTestHelper.get_value("Value 1")
        payload = {
            'name': "Value 1 New Name"
        }
        response = self.client.put(reverse(ValueTestHelper.API_DETAIL_VALUE, kwargs={'pk': value.pk}), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(response.data.get('name'), payload['name'])

    def test_delete_value(self):
        """
        Deleting agile value is not allowed.

        :return:
        """
        value = ValueTestHelper.get_value("Value 1")
        response = self.client.delete(reverse(ValueTestHelper.API_DETAIL_VALUE, kwargs={'pk': value.pk}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED, response.content)
