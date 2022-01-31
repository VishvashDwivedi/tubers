from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    def name(self, object):
        fullname = object.first_name + " " + object.last_name
        return fullname

    list_display = ('id', 'myphoto', 'name', 'role', 'created_date')
    list_display_links = ('name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)
    ordering = ('id',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)