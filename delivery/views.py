from rest_framework import viewsets, generics
from .models import Cargo, Location, Car
from .serializers import CargoSerializer, LocationSerializer, CarSerializer


class CargoViewSet(viewsets.ModelViewSet):
    '''
    Cargo, viewset, Груз.
    Доступ для авторизированных (is_authenticated) пользователей.
    '''

    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Cargo.objects.filter(user=user)
        else:
            queryset = Cargo.objects.none()
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Location, viewset, Локация.
    Доступ для авторизированных (is_authenticated) пользователей.
    '''

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CarViewSet(viewsets.ModelViewSet):
    '''
    Car, viewset, Машина.
    Доступ для авторизированных (is_authenticated) пользователей.
    '''

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Car.objects.filter(user=user)
        else:
            queryset = Car.objects.none()
        return queryset


class CargoList(generics.ListAPIView):
    '''
    Cargo, generics, Список грузов.
    Доступ для авторизированных (is_authenticated) пользователей.
    '''

    serializer_class = CargoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            zip_code = self.request.query_params.get('zip_code')
            pick_up_location = Location.objects.get(zip_code=zip_code)
            queryset = Cargo.objects.filter(pick_up_location=pick_up_location, user=user)
        else:
            queryset = Cargo.objects.none()
        return queryset


class CargoDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Cargo, generics, Детальная информация о грузе.
    Доступ для авторизированных (is_authenticated) пользователей.
    '''

    serializer_class = CargoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Cargo.objects.filter(user=user)
        else:
            queryset = Cargo.objects.none()
        return queryset
