from django.contrib import admin
from delivery.models import Location, Cargo, Car


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    '''
    Локация - отображение в админ-панели Jango.
    Фильтрует по городу и штату.
    Поиск в названии города и штата.
    '''
    list_display = ('city', 'state', 'zip_code', 'latitude', 'longitude')
    list_filter = ('city', 'state',)
    search_fields = ('city', 'state')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    '''
    Машина - отображение в админ-панели Jango.
    Фильтрует по current_location и грузоподъемности.
    Поиск в current_location.
    '''
    list_display = ('id', 'current_location', 'unique_number', 'cargo_capacity',)
    list_filter = ('current_location', 'cargo_capacity',)
    search_fields = ('current_location',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    '''
    Груз - отображение в админ-панели Jango.
    Фильтрует по pick_up_location и delivery_location.
    Поиск в описании.
    '''
    list_display = ('id', 'pick_up_location', 'delivery_location', 'weight', 'description')
    list_filter = ('pick_up_location', 'delivery_location',)
    search_fields = ('description', )
