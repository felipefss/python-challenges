from rest_framework import serializers

from daily_diet.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "name", "description", "timestamp", "is_in_diet", "user"]
