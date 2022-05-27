import requests
import logging
from typing import Dict, Any
from rest_framework.response import Response
import json
logger = logging.getLogger(__name__)

class TicketingApiClient:
    """Ticketing API client stub.

    You can expand it and add implementations
    to get data using different API endpoints.
    """

    URL = 'http://127.0.0.1:3000'

    def get_user_orders(self, user_id):
        user_orders = requests.get(self.URL + f"/getOrders/{user_id}")
        return user_orders.json()

    def get_user(self, user_id):
        users = requests.get(self.URL + "/users/")
        user_data = users.json()
        users_list = [user["id"] for user in user_data]
        if user_id not in users_list:
            return Response(data="The requested user does not exist",status=400)
        return user_data[users_list.index(user_id)]

    def get_users(self):
        users = requests.get(self.URL + "/users/")
        return users.json()

    def update_user(self, user_id, points):
        payload = {
            "user_id": user_id,
            "add_points": points,
        }
        return requests.post(self.URL + "/update-user", json=payload)
        