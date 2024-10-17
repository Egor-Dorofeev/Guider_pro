from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from datetime import datetime

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request):
        queryset = self.queryset
        street = request.query_params.get('street')
        city = request.query_params.get('city')
        open_status = request.query_params.get('open')

        if street:
            queryset = queryset.filter(street__name=street)
        if city:
            queryset = queryset.filter(city__name=city)
        if open_status is not None:
            current_time = datetime.utcnow().time()
            if open_status == '1':
                queryset = queryset.filter(opening_time__lte=current_time, closing_time__gte=current_time)
            elif open_status == '0':
                queryset = queryset.exclude(opening_time__lte=current_time, closing_time__gte=current_time)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)