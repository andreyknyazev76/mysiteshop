from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(Products)
class ProductsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        ("price", "discount"),
        "quantity",
        "created_at",
        "status"
    ]

    summernote_fields = ("description")
