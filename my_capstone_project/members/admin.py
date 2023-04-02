from django.contrib import admin

# Register your models here.
from .models import Member
@admin.register(Member)
class membersAdmin(admin.ModelAdmin):
   list_display=['productname','brandname','price','reviews','ratings','reviewvotes']