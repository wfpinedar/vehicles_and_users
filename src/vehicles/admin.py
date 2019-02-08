from django.contrib import admin

# Register your models here.
from .models import Owner
from .models import Vehicle


class VehicleInline(admin.TabularInline):
    model = Vehicle


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [VehicleInline,]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
