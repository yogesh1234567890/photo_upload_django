from django.contrib import admin
from work.models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    def work(obj):
        return obj
    
    list_display=['name','email','image']
