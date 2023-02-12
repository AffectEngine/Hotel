from .models import PGSRoomReserving, PGSRubric, HotelEmployees, HotelRooms
from django.forms import *
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.core import validators
from django.conf import settings
from easy_thumbnails.widgets import ImageClearableFileInput


class PGSRoomReservingForm(ModelForm):
	name = forms.CharField(
		label='Room',
		min_length=2,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter room name'
			}))
	reserving_date = DateField(
		widget=forms.DateInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter room reserving date'
			}))
	reserving_time = TimeField(
		widget=forms.TimeInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter room reserving time'
			}))
	price = IntegerField(
		widget=forms.NumberInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter room price'
			}))
	cancelled = BooleanField(
		label='Cancel reserving',
		widget=CheckboxInput(),
		)

	class Meta:
		model = PGSRoomReserving
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PGSRoomReservingForm, self).__init__(*args, **kwargs)
		self.fields['cancelled'].required = False

	def clean(self):
		super().clean()
		errors = {}
		if not self.cleaned_data['name']:
			errors['name'] = ValidationError(
				'Thou name is too short')
		if not self.cleaned_data['reserving_date']:
			errors['reserving_date'] = ValidationError(
				'Please enter date')
		if not self.cleaned_data['reserving_time']:
			errors['reserving_time'] = ValidationError(
				'Please enter time')
		if self.cleaned_data['price'] < 0:
			errors['price'] = ValidationError(
				'Please enter positive price number')
		if errors:
			raise ValidationError(errors)


class PGSRubricForm(ModelForm):
	name = forms.CharField(
		label='Rubric',
		widget=TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter rubric name',
			}))
	description = forms.CharField(
		label='Description',
		widget=Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Enter rubric name',
			}))
	tags = ArrayField(base_field=forms.CharField(max_length=90))

	class Meta:
		model = PGSRubric
		fields = '__all__'


class HotelEmployeesForm(ModelForm):
	first_name = forms.CharField(
		label='First Name',
		widget=TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter first name',
			}))
	last_name = forms.CharField(
		label='Last Name',
		widget=TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter last name',
			}))
	birth_date = forms.DateField(
		label='Birth Date',
		input_formats=settings.DATE_INPUT_FORMATS,
		widget=DateInput(attrs={
			'class': 'form-control',
			'placeholder': 'format "DD-MM-YYYY"',
			}))
	address = forms.CharField(
		label='Address',
		widget=TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter address',
			}))
	phone = forms.CharField(
		label='Phone',
		widget=TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter phone',
			}))
	photo = forms.ImageField(
		label='Photo',
		validators=[validators.FileExtensionValidator(
			allowed_extensions=('jpg', 'png'))],
		error_messages={
			'invalid_extension': 'This format is not allowed'
			})

	class Meta:
		model = HotelEmployees
		fields = '__all__'


class HotelRoomsForm(forms.ModelForm):
	title = forms.CharField(
		label='Room Title',
		widget=TextInput(attrs={
			'placeholder': 'Enter room title',
			}))
	picture = forms.ImageField(
		label='Room Picture',
		validators=[validators.FileExtensionValidator(
			allowed_extensions=('jpg', 'png'))],
		error_messages={
			'invalid_extension': 'This format is not allowed'
			})
	picture_thumbnail = forms.ImageField(widget=ImageClearableFileInput(
		thumbnail_options={'size': (300, 200)}))
	price = forms.IntegerField(
		label='Room Price',
		widget=NumberInput(attrs={
			'placeholder': 'Enter room price',
			}))
	description = forms.CharField(
		label='Description',
		widget=Textarea(attrs={
			'placeholder': 'Enter room description',
			}))

	class Meta:
		model = HotelRooms
		fields = '__all__'


class EmailTestForm(forms.Form):
	name = forms.CharField(max_length=100, min_length=2)
	phone = forms.CharField(max_length=70, min_length=11, help_text='Enter your phone in format: +7-000-000-00-00')
	email = forms.EmailField(max_length=150, min_length=4, help_text='Enter your Email')
	message = forms.CharField(widget=forms.Textarea, max_length=2000, required=False)

	def clean(self):
		cleaned_data = super().clean()
		return cleaned_data
