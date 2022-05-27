from django.core.management.base import BaseCommand
from rewards.models import Reward, Recommendation
from rewards.rewards import user_rewards
from rewards.ticketing_api_client import TicketingApiClient
ticket_client = TicketingApiClient()

class Command(BaseCommand):
    """Script to refresh recommendations."""

    def handle(self, *args, **options):
        users = ticket_client.get_users()

        # Reward 1
        reward_1 = user_rewards(users[0]["points"])
        saved_reward_1 = Reward.objects.create(
            name=reward_1["name"], points=reward_1["points"], max_per_user=reward_1["max_per_user"]
        )
        recommendation_1 = Recommendation.objects.create(
            user_id=users[0]["id"],
        )
        recommendation_1.rewards.add(saved_reward_1)
        
        # Reward 2
        reward_2 = user_rewards(users[1]["points"])
        saved_reward_2_0 = Reward.objects.create(name=reward_2[0]["name"], points=reward_2[0]["points"], max_per_user=reward_2[0]["max_per_user"])
        saved_reward_2_1 = Reward.objects.create(name=reward_2[1]["name"], points=reward_2[1]["points"], max_per_user=reward_2[1]["max_per_user"])
        recommendation = Recommendation.objects.create(
            user_id=users[1]["id"],
        )
        recommendation.rewards.add(saved_reward_2_0)
        recommendation.rewards.add(saved_reward_2_1)