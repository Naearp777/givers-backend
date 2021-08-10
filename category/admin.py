from django.contrib import admin
from .models import EventCategory, Skills, Country, Province, District, Municipality, Ward
# Register your models here.
admin.site.register(EventCategory)
admin.site.register(Skills)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Ward)
