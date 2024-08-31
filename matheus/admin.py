from django.contrib import admin
from .models import Hobbie, Namorado, MaisFotos
from django.utils.html import format_html

# Register your models here.

@admin.register(Hobbie)
class HobbieAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Imagem'
    list_display = ['nome', 'nota', 'sobre', 'image_tag']

@admin.register(Namorado)
class NamoradoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Imagem'
    list_display = ['nome', 'idade', 'nota', 'sobre', 'image_tag']

@admin.register(MaisFotos)
class MaisFotosAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Imagem'
    list_display = ['titulo', 'image_tag']