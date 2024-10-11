from django.contrib import admin
from .models import table1,Category,aboutus


class table1Admin(admin.ModelAdmin):
        list_display = ('title','content')
        search_fields =('title','content')
        list_filter = ('category','created_at')


# Register your models here.
admin.site.register(table1,table1Admin)
admin.site.register(Category)
admin.site.register(aboutus)