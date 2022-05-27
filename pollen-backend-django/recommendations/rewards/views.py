from rest_framework.decorators import api_view
from rest_framework.response import Response
from rewards.serializer import RecommendationSerializer
from rewards.ticketing_api_client import TicketingApiClient
from rewards.models import Recommendation

ticket_client = TicketingApiClient()

@api_view(['GET'])
def getRecommendations(request, user_id):
    if user_id == '':
        orders = RecommendationSerializer(Recommendation.objects.all(), many=True)
    elif user_id != '':
        orders = RecommendationSerializer(Recommendation.objects.filter(user_id=user_id), many=True)
    return Response(orders.data)