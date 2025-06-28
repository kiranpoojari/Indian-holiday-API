from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from .models import Holiday
from .serializers import HolidaySerializer

class HolidayListView(ListAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [AllowAny]
