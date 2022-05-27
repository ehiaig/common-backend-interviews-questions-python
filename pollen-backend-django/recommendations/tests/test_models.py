"""This just an example. You're not expected to make any changes here."""

import pytest

from rewards.models import Recommendation, Reward
from rewards.ticketing_api_client import TicketingApiClient
from rewards.rewards import user_rewards

ticket_client = TicketingApiClient()

pytestmark = pytest.mark.django_db

@pytestmark
def test_reward():
    user_1 = ticket_client.get_users()[0]
    reward = user_rewards(user_1["points"])
    saved_reward = Reward.objects.create(
        name=reward["name"], points=reward["points"], max_per_user=reward["max_per_user"]
    )
    recommendation = Recommendation.objects.create(
        user_id=user_1["id"],
    )
    recommendation.rewards.add(saved_reward)
    assert recommendation.user_id == user_1["id"]
    assert saved_reward.name == "General Ticket"
