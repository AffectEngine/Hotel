from .models import PGSRoomReserving, PGSRubric, HotelEmployees, HotelRooms
from .forms import PGSRubricForm, PGSRoomReservingForm, HotelEmployeesForm, HotelRoomsForm

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator


# LOGIN-LOGOUT ETC.

def signup(request):
	return render(request, 'PGapp/Account/signup.html')


# CONTENT of the main logic of the SITE

def start_page(request):
	return render(request, 'PGapp/Main_Logic/start_page.html')


def room_reserving(request):
	room_source = PGSRoomReserving.objects.all()
	return render(request, 'PGapp/Room/room_reserving.html', {'title': 'Rooms', 'room_source': room_source})


def add_room(request):
	form = PGSRoomReservingForm()
	if request.method == 'POST':
		form = PGSRoomReservingForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Room created successfully')
			return HttpResponseRedirect(reverse('PGapp:room_reserving'))
		else:
			messages.error(request, 'Failure occurs')
	context = {
		'form': form,
		}
	return render(request, 'PGapp/Room/add_room.html', context)


def edit_room(request, id):
	room = PGSRoomReserving.objects.get(pk=id)
	if request.method == 'POST':
		room_form = PGSRoomReservingForm(request.POST, instance=room)
		if room_form.is_valid():
			if room_form.has_changed():
				room_form.save()
				return HttpResponseRedirect(reverse('PGapp:room_reserving'))
	else:
		room_form = PGSRoomReservingForm(instance=room)
		context = {'form': room_form}
		return render(request, 'PGapp/Room/edit_room.html', context)


def delete_room(request, id):
	room = PGSRoomReserving.objects.get(pk=id)
	if request.method == 'POST':
		room.delete()
		return HttpResponseRedirect(reverse('PGapp:room_reserving'))
	else:
		context = {'room': room}
		return render(request, 'PGapp/Room/confirm_delete_room.html', context)


def rubrics(request):
	rubric_source = PGSRubric.objects.all()
	return render(request, 'PGapp/Rubric/rubrics.html', {'title': 'Rubrics', 'rubric_source': rubric_source})


def add_rubric(request):
	form = PGSRubricForm()
	if request.method == 'POST':
		form = PGSRubricForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Rubric added successfully')
			return HttpResponseRedirect(reverse('PGapp:rubrics'))
	context = {
		'form': form,
		}
	return render(request, 'PGapp/Rubric/add_rubric.html', context)


def edit_rubric(request, id):
	rubric = PGSRubric.objects.get(pk=id)
	if request.method == 'POST':
		rubric_form = PGSRoomReservingForm(request.POST, instance=rubric)
		if rubric_form.is_valid():
			if rubric_form.has_changed():
				rubric_form.save()
				return HttpResponseRedirect(reverse('PGapp:rubrics'))
	else:
		rubric_form = PGSRoomReservingForm(instance=rubric)
		context = {'form': rubric_form}
		return render(request, 'PGapp/Rubric/edit_rubric.html', context)


def delete_rubric(request, id):
	rubric = PGSRubric.objects.get(pk=id)
	if request.method == 'POST':
		rubric.delete()
		return HttpResponseRedirect(reverse('PGapp:rubrics'))
	else:
		context = {'rubric': rubric}
		return render(request, 'PGapp/Rubric/confirm_delete_rubric.html', context)


def employees(request):
	employee_source = HotelEmployees.objects.all()
	return render(request, 'PGapp/Employee/employees.html', {'title': 'Employees', 'employee_source': employee_source})


def add_employee(request):
	if request.POST:
		form = HotelEmployeesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(
				request,
				messages.SUCCESS,
				'Employee was successfully added.',
				)
			return redirect('PGapp:employees')
		else:
			raise Exception('Invalid')
	else:
		return render(request, 'PGapp/Employee/add_employee.html', {'form': HotelEmployeesForm})


def edit_employee(request, id):
	employee = HotelEmployees.objects.get(pk=id)
	if request.method == 'POST':
		form = HotelEmployeesForm(request.POST, instance=employee)
		if form.is_valid():
			if form.has_changed():
				form.save()
				return HttpResponseRedirect(reverse_lazy('PGapp:employees'))
	else:
		form = HotelEmployeesForm(instance=employee)
		context = {'form': form}
		return render(request, 'PGapp/Employee/edit_employee.html', context)


def delete_employee(request, id):
	employee = HotelEmployees.objects.get(pk=id)
	if request.method == 'POST':
		employee.delete()
		return HttpResponseRedirect(reverse('PGapp:employees'))
	else:
		context = {'employee': employee}
		return render(request, 'PGapp/Employee/confirm_delete_employee.html', context)


def hotel_rooms(request):
	hotel_room_source = HotelRooms.objects.all()
	paginator = Paginator(hotel_room_source, 4)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1
	page = paginator.get_page(page_num)
	context = {'page': page, 'hotel_room_source': page.object_list}
	return render(request, 'PGapp/HotelRooms/hotel_rooms.html', context)


def add_hotel_room(request):
	if request.POST:
		hotel_form = HotelRoomsForm(request.POST, request.FILES)
		if hotel_form.is_valid():
			hotel_form.save()
			messages.success(request, 'Hotel room added successfully')
			return redirect('PGapp:hotel_rooms')
		else:
			raise Exception('Invalid')
	else:
		return render(request, 'PGapp/HotelRooms/add_hotel_room.html', {'hotel_form': HotelRoomsForm})


def room_full_view(request, hotel_room_id):
	hotel_room_source = HotelRooms.objects.get(pk=hotel_room_id)
	return render(request, 'PGapp/HotelRooms/room_full_view.html', {'hotel_room_source': hotel_room_source})


def edit_hotel_room(request, hotel_room_id):
	hotel_room_source = HotelRooms.objects.get(pk=hotel_room_id)
	hotel_form = HotelRoomsForm(request.POST or None, request.FILES or None, instance=hotel_room_source)
	if hotel_form.is_valid():
		if hotel_form.has_changed():
			hotel_form.save()
			return redirect('PGapp:hotel_rooms')
	return render(request, 'PGapp/HotelRooms/edit_hotel_room.html', {'hotel_form': hotel_form})


def delete_hotel_room(request, hotel_room_id):
	hotel_room_source = HotelRooms.objects.get(pk=hotel_room_id)
	if request.method == 'POST':
		hotel_room_source.delete()
		return HttpResponseRedirect(reverse('PGapp:hotel_rooms'))
	else:
		context = {'hotel_room_source': hotel_room_source}
		return render(request, 'PGapp/HotelRooms/confirm_delete_hotel_room.html', context)


# MESSAGES


# TESTING

def email_test(request):
	return render(request, 'PGapp/Account/email.html')
