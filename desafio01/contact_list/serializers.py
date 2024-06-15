from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "favorite",
            "created_at",
            "updated_at",
        ]
