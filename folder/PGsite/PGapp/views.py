from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import PGSRubric, HotelEmployees, HotelRooms, PGSThing
from .forms import PGSRubricForm, HotelEmployeesForm, HotelRoomsForm, EmailTestForm

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail, send_mass_mail

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import RubricSerializer, ThingSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response


# LOGIN-LOGOUT ETC.

def signup(request):
	return render(request, 'PGapp/Account/signup.html')


# CONTENT of the main logic of the SITE

def start_page(request):
	return render(request, 'PGapp/Main_Logic/start_page.html')


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
		rubric_form = PGSRubricForm(request.POST, instance=rubric)
		if rubric_form.is_valid():
			if rubric_form.has_changed():
				rubric_form.save()
				return HttpResponseRedirect(reverse('PGapp:rubrics'))
	else:
		rubric_form = PGSRubricForm(instance=rubric)
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


def edit_employee(request, pk):
	employee = HotelEmployees.objects.get(id=pk)
	form = HotelEmployeesForm(instance=employee)
	if request.method == 'POST':
		form = HotelEmployeesForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
			messages.add_message(
				request,
				messages.SUCCESS,
				'Employee was successfully edited.',
				)
			return redirect('/employees')
	context = {'form': form}
	return render(request, 'PGapp/Employee/edit_employee.html', context)


def delete_employee(request, id):
	employee = HotelEmployees.objects.get(pk=id)
	if request.method == 'POST':
		employee.delete()
		messages.add_message(
			request,
			messages.SUCCESS,
			'Employee was successfully deleted.',
			)
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


# REST

class RubricApiList(generics.ListCreateAPIView):
	queryset = PGSRubric.objects.all()
	serializer_class = RubricSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )


class RubricApiUpdate(generics.RetrieveUpdateAPIView):
	queryset = PGSRubric.objects.all()
	serializer_class = RubricSerializer
	permission_classes = (IsOwnerOrReadOnly, )


class RubricApiDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = PGSRubric.objects.all()
	serializer_class = RubricSerializer
	permission_classes = (IsAdminOrReadOnly, )


class ThingViewSet(viewsets.ModelViewSet):
	queryset = PGSThing.objects.all()
	serializer_class = ThingSerializer

	@action(methods=['get'], detail=True)
	def things_rubrics_list_display(self, request, pk=None):
		cats = PGSRubric.objects.get(pk=pk)
		return Response({'cats': cats.rubric})


# class RubricApiList(generics.ListCreateAPIView):
# 	queryset = PGSRubric.objects.all()
# 	serializer_class = RubricSerializer
#
#
# class RubricApiUpdate(generics.UpdateAPIView):
# 	queryset = PGSRubric.objects.all()
# 	serializer_class = RubricSerializer
#
#
# class RubricApiDetailView(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = PGSRubric.objects.all()
# 	serializer_class = RubricSerializer


# class RubricAPIView(APIView):
# 	def get(self, request):
# 		rub_objects = PGSRubric.objects.all()
# 		return Response({'rubrics': RubricSerializer(rub_objects, many=True).data})
#
# 	def post(self, request):
# 		serializer = RubricSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response({'post': serializer.data})
#
# 	def put(self, request, *args, **kwargs):
# 		pk = kwargs.get('pk', None)
# 		if not pk:
# 			return Response({'error': 'Method PUT not allowed'})
#
# 		try:
# 			instance = PGSRubric.objects.get(pk=pk)
# 		except:
# 			return Response({'error': 'Object does not exists'})
#
# 		serializer = RubricSerializer(data=request.data, instance=instance)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response({'post': serializer.data})
#
# 	def delete(self, request, *args, **kwargs):
# 		pk = kwargs.get('pk', None)
# 		if not pk:
# 			return Response({'error': 'Method DELETE not allowed'})
# 		try:
# 			instance = PGSRubric.objects.get(pk=pk)
# 		except:
# 			return Response({'error': 'Object does not exists'})
#
# 		instance.delete()
#
# 		return Response({'post': str(pk) + ' was deleted'})

# class RubricAPIView(generics.ListAPIView):
# 	queryset = PGSRubric.objects.all()
# 	serializer_class = RubricSerializer


# TESTING

def email_test(request):
	send_mail(
		'White',
		'World',
		'',
		['rayih81160@chotunai.com'],
		fail_silently=False,
		html_message='<h1>Hello</h1><br><h3>World</h3>',
		)
	msg1 = ('message1', 'Sub', '', ['rayih81160@chotunai.com'])
	msg2 = ('message2', 'Scribe', '', ['rayih81160@chotunai.com'])
	send_mass_mail((msg1, msg2))
	return render(request, 'PGapp/Options/send_email.html')
