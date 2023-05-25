from django.urls import path
from hello_recruiter import views

urlpatterns = [
	path('', views.hello_recruiter, name='hello_recruiter')
]
