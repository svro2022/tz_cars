from rest_framework import serializers
from .models import Cargo, Location, Car
from geopy.distance import distance as geopy_distance


class LocationSerializer(serializers.ModelSerializer):
    '''Сериализатор локации (Location)'''

    class Meta:
        model = Location
        fields = ['id', 'city', 'state', 'zip_code', 'latitude', 'longitude']


class CarSerializer(serializers.ModelSerializer):
    '''Сериализатор машины (Car)'''

    class Meta:
        model = Car
        fields = ['id', 'unique_number', 'current_location', 'cargo_capacity']


class CargoSerializer(serializers.ModelSerializer):
    '''Сериализатор груза (Cargo)'''

    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()
    cars_with_distance = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up_location', 'delivery_location', 'weight', 'description', 'cars_with_distance']

    def get_car_with_distance(self, obj):
        cars = Car.objects.all()
        pick_up_location = obj.pick_up_location
        cars_with_distance = []
        for car in cars:
            distance_to_pick_up = geopy_distance(
                (car.current_location.latitude, car.current_location.longitude),
                (pick_up_location.latitude, pick_up_location.longitude)
            ).miles
            cars_with_distance.append({
                'car': car,
                'distance_to_pick_up': distance_to_pick_up,
            })
        return cars_with_distance

