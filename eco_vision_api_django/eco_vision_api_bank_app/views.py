from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from .models import WasteBank
from .serializers import WasteBankSerializer, WasteBankCreateSerializer

class WasteBankListCreateView(ListCreateAPIView):
    queryset = WasteBank.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WasteBankCreateSerializer
        return WasteBankSerializer
