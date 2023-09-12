from django.contrib import admin
from vegapp.models import recform
# Register your models here.
class showres(admin.ModelAdmin):
    list_display=("rec_name","rec_dec","rec_img")
admin.site.register(recform,showres)