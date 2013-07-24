from django.contrib import admin
from Menu.models import Cooker, Menu


class CookerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')

class MenuAdmin(admin.ModelAdmin):
	list_display = ('title', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	fields = ('title', 'cookers',)
	filter_horizontal = ('cookers',)


# admin.site.register(Publisher) 
admin.site.register(Cooker,CookerAdmin) 
admin.site.register(Menu, MenuAdmin)