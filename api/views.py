from django.views.generic import TemplateView
from rest_framework import generics
from .models import Dispensary
from .serializers import DispensarySerializer

class NotAPageView(TemplateView):
    template_name = '404.html'


class DispensaryList(generics.ListCreateAPIView):
    queryset = Dispensary.objects.all()
    serializer_class = DispensarySerializer


class DispensaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispensary.objects.all()
    serializer_class = DispensarySerializer
