from django.contrib import admin
from applications.models import Application




class ApplicationItemTabulareAdmin(admin.TabularInline):
    model = Application
    fields = "created_timestamp", "description_address", "status"
    search_fields = (
        "created_timestamp",
        "description_address",
    )
    extra = 0



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "description_address",
        "phone_number" ,
        "status",
        "created_timestamp",
        
    )

    search_fields = (
        "id",  
    )
    
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "description_address",
        "status",   
    )
   
