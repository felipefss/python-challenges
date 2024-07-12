from rest_framework import viewsets

from .models import Meal
from .serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    # queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get_queryset(self):
        # In an ideal world, the user info would come in an JWT header
        if "user" in self.request.query_params:
            return Meal.objects.filter(user=int(self.request.query_params["user"]))
        return Meal.objects.all()
