from django.contrib import admin
from .models import PGSRoomReserving, PGSRubric, HotelEmployees, HotelRooms


class PGSRoomReservingAdmin(admin.ModelAdmin):
	list_display = ('name', 'reserving_date', 'reserving_time', 'price', 'cancelled')
	list_display_links = ('reserving_date', 'reserving_time')
	list_editable = ('name', 'price')
	search_fields = ('name', 'reserving_date', 'reserving_time', '=price')
	list_filter = ('name', 'reserving_date', 'price')
	date_hierarchy = 'reserving_date'


class PGSRubricAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'tags')
	list_display_links = ('name', 'description')
	search_fields = ('name', 'tags')


class HotelEmployeesAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'birth_date', 'address', 'hire_date', 'phone', 'photo')
	fields = (('first_name', 'last_name'), ('address', 'phone'), 'birth_date', 'photo')
	list_display_links = ('first_name', 'last_name', 'birth_date', 'address', 'phone', 'photo')
	search_fields = ('first_name', 'last_name', 'phone')
	readonly_fields = ('id',)

	def get_fields(self, request, obj=None):
		add_form_fields = ['first_name', 'last_name', 'birth_date', 'address', 'phone', 'photo']
		change_form_fields = ['birth_date', 'address', 'phone', 'photo']
		if obj:
			return change_form_fields
		return add_form_fields


class HotelRoomsAdmin(admin.ModelAdmin):
	list_display = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	list_display_links = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	search_fields = ('title', 'price')
	readonly_fields = ('id',)


admin.site.register(PGSRoomReserving, PGSRoomReservingAdmin)
admin.site.register(PGSRubric, PGSRubricAdmin)
admin.site.register(HotelEmployees, HotelEmployeesAdmin)
admin.site.register(HotelRooms, HotelRoomsAdmin)
