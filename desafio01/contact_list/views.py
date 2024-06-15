from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Contact

from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """

    queryset = Contact.objects.all().order_by("name")
    serializer_class = ContactSerializer

    @action(detail=False)
    def favorites(self, request):
        fav_contacts = Contact.objects.filter(favorite=True)
        serializer = self.get_serializer(fav_contacts, many=True)

        return Response(serializer.data)
