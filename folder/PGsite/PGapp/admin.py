from django.contrib import admin
from .forms import HotelEmployeesForm
from .models import PGSRubric, HotelEmployees, HotelRooms, PGSThing
from django.db.models import F


@admin.register(PGSRubric)
class PGSRubricAdmin(admin.ModelAdmin):
	list_display = ('rubric', 'description', 'tags')
	list_display_links = ('rubric', 'description')
	search_fields = ('rubric', 'tags')


@admin.register(PGSThing)
class PGSThingAdmin(admin.ModelAdmin):
	list_display = ('thing_itself', 'hierarchy')
	list_display_links = ('thing_itself',)
	autocomplete_fields = ('thing_itself',)


@admin.register(HotelEmployees)
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

	def get_form(self, request, obj=None, **kwargs):
		if obj:
			return HotelEmployeesForm
		else:
			return HotelEmployeesForm


@admin.register(HotelRooms)
class HotelRoomsAdmin(admin.ModelAdmin):
	list_display = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	list_display_links = ('title', 'picture', 'picture_thumbnail', 'price', 'description')
	search_fields = ('title', 'price')
	readonly_fields = ('id',)
	view_on_site = True
	actions = ('price_down_half',)

	def price_down_half(self, request, queryset):
		current_price = F('price')
		for record in queryset:
			record.price = current_price / 2
			record.save()
		self.message_user(request, 'The deed is done')
	price_down_half.short_description = 'Reduces all rooms price for a half'
