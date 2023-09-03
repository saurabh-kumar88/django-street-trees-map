from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from street_trees_app.models import RK_Ashram_marg


# Change Admin header
admin.site.site_header = "Streets Trees Map"

Display_fields = [
    "id",
    "Tree_code",
    "created",
    "updated",
    "common_name",
    "scientific_name",
    "Age",
    "Height",
    "Diameter_girth",
    "closest_address",
    "Longitude",
    "Latitude",
    "specie_code",
    "condition",
]

Editable_fields = [
    "Tree_code",
    "common_name",
    "scientific_name",
    "Age",
    "Height",
    "Diameter_girth",
    "closest_address",
    "Longitude",
    "Latitude",
    "specie_code",
    "condition",
]


class CustomAdminPanel(admin.ModelAdmin):
    list_display = Display_fields
    list_editable = Editable_fields
    list_filter = ["common_name"]
    ordering = ["id"]


admin.site.register(RK_Ashram_marg, CustomAdminPanel)
# admin.site.unregister(User)
