"""Recommendations tests.

   We use pytest internally but you can choose a library you're most comfortable with."""

from rewards.ticketing_api_client import TicketingApiClient
import json 
ticket_client = TicketingApiClient()


def test_get_user_recommendations(client):
    response = client.get("/recommendations/1")
    assert response.status_code == 200

def test_get_recommendations_nonexistent_user(client):
    response = client.get("/recommendations/0")
    assert response.status_code == 200

def test_updated_user_recommemdation(client):
    user_id = 1
    user = ticket_client.get_user(user_id)
    assert user["points"] == 100
    
    new_point = 300
    ticket_client.update_user(user_id, new_point)
    updated_user = ticket_client.get_user(user_id)
    assert updated_user["points"] == new_point + user["points"]




