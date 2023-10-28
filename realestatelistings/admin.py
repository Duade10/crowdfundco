from django.contrib import admin

from .models import RealEstateListing, ExtraDocument


class ExtraDocumentTabularInline(admin.TabularInline):
    model = ExtraDocument


@admin.register(RealEstateListing)
class RealEstateListingAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
        "location",
        "status",
    ]
    inlines = [
        ExtraDocumentTabularInline,
    ]
