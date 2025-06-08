from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import WasteBank
from .serializers import WasteBankSerializer

class WasteBankListView(ListAPIView):
    queryset = WasteBank.objects.all()
    serializer_class = WasteBankSerializer
    permission_classes = [IsAuthenticated]