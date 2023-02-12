from django.db import models
from django.db.models import *

from django.contrib.postgres.fields import *
from django.core.validators import *
from django.core import validators

from easy_thumbnails.fields import ThumbnailerImageField


class PGSRoomReserving(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=50, verbose_name='Room')
	reserving_date = DateField(verbose_name='Reserving date')
	reserving_time = TimeField(verbose_name='Reserving time')
	price = IntegerField(verbose_name='Room price')
	cancelled = models.BooleanField(default=False, verbose_name='Cancel reserving')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Reserving'
		verbose_name_plural = 'Reservings'
		ordering = ['name']
		get_latest_by = 'reserving'


class PGSRubric(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=50, verbose_name='Rubric')
	description = models.TextField(verbose_name='Description')
	tags = ArrayField(base_field=models.CharField(max_length=90), verbose_name='Tags')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Rubric'
		verbose_name_plural = 'Rubrics'
		ordering = ['name']
		get_latest_by = 'name'


class HotelEmployees(models.Model):
	objects = models.Manager()
	first_name = models.CharField(max_length=50, verbose_name='Employee first name')
	last_name = models.CharField(max_length=50, verbose_name='Employee last name')
	birth_date = models.DateField(verbose_name='Employee birth date')
	address = models.CharField(max_length=100, verbose_name='Employee address')
	hire_date = models.DateField(auto_now=True, verbose_name='Employee hire date')
	phone = models.CharField(
		max_length=100,
		verbose_name='Employee phone',
		validators=[
			MinLengthValidator(10)
			]
		)
	photo = models.ImageField(
		verbose_name='Employee Photo',
		upload_to='img/Employee_pics/%Y/%m/%d/',
		default='D:/A_PYTHONPROJECTS/Revashing/folder/PGsite/media/img/default.jpg',
		null=True,
		blank=True,
		validators=[validators.FileExtensionValidator(
			allowed_extensions=('jpg', 'jpeg', 'png'))],
		error_messages={
			'invalid_extension': 'This format is not allowed'
			})

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'


class HotelRooms(models.Model):
	objects = models.Manager()
	title = CharField(max_length=90, verbose_name="Room Title")
	picture = ImageField(
		verbose_name="Room Picture",
		upload_to='img/Hotel_Room_pics/%Y/%m/%d/',
		default='D:/A_PYTHONPROJECTS/Revashing/folder/PGsite/media/img/room_default.png',
		null=True,
		blank=True,
		validators=[validators.FileExtensionValidator(
			allowed_extensions=('jpg', 'jpeg', 'png'))],
		error_messages={
			'invalid_extension': 'This format is not allowed'
			})
	picture_thumbnail = ThumbnailerImageField(
		resize_source={'size': (400, 300), 'crop': 'scale'},
		upload_to='img/Hotel_Room_thumbnails/%Y/%m/%d/',
		default='D:/A_PYTHONPROJECTS/Revashing/folder/PGsite/media/img/room_thumbnail_default.png',
		)
	price = IntegerField(verbose_name="Room Price")
	description = TextField(verbose_name="Room Description")

	class Meta:
		verbose_name = 'Hotel Room'
		verbose_name_plural = 'Hotel Rooms'

