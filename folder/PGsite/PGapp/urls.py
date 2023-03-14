from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'PGapp'

urlpatterns = [
	path('', start_page, name='start_page'),
	path('accounts/register/', register_page, name='register'),
	path(
		'accounts/login/',
		LoginView.as_view(template_name='PGapp/Account/login.html', next_page='PGapp:start_page'),
		name='login'
		),
	path(
		'accounts/logout/',
		LogoutView.as_view(next_page='PGapp:login'),
		name='logout_verification'
		),

	path('rubrics/', rubrics, name='rubrics'),
	path('add_rubric/', add_rubric, name='add_rubric'),
	path('rubrics/edit_rubric/<int:id>/', edit_rubric, name='edit_rubric'),
	path('rubrics/delete_rubric/<int:id>/', delete_rubric, name='confirm_delete_rubric'),
	path('api/v1/rubrics/', RubricApiList.as_view()),
	path('api/v1/rubrics/<int:pk>/', RubricApiUpdate.as_view()),
	path('api/v1/rubricsdelete/<int:pk>/', RubricApiDestroy.as_view()),

	path('employees/', employees, name='employees'),
	path('add_employee/', add_employee, name='add_employee'),
	path('employees/edit_employee/<str:pk>/', edit_employee, name='edit_employee'),
	path('employees/delete_employee/<int:id>/', delete_employee, name='confirm_delete_employee'),

	path('hotel_rooms/', hotel_rooms, name='hotel_rooms'),
	path('add_hotel_room/', add_hotel_room, name='add_hotel_room'),
	path('hotel_rooms/edit_hotel_room/<int:hotel_room_id>/', edit_hotel_room, name='edit_hotel_room'),
	path('hotel_rooms/delete_hotel_room/<int:hotel_room_id>/', delete_hotel_room, name='confirm_delete_hotel_room'),
	path('hotel_rooms/room_full_view/<int:hotel_room_id>/', room_full_view, name='room_full_view'),

	path('email_test/', email_test, name='email_test'),
	]
