"""
URL configuration for care_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from staff.views import DoctorsListCreateView,DoctorsRetreiveUpdateDeleteView
from staff_v2 import views
from bookings.views import AppointmentsCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/',DoctorsListCreateView.as_view()),
    path('doctors/<int:pk>/',DoctorsRetreiveUpdateDeleteView.as_view()),

#v2 routes

    path('v2/doctors/',views.DoctorListCreateView.as_view()),
    path('v2/doctors/<int:pk>/',views.DoctorRetrieveUpdateDeleteView.as_view()),
    path('v2/admin-register/',views.AdminRegisterView.as_view()),

#appointment routes

    path('appointments/',AppointmentsCreateListView.as_view()),


#booking_v2
    path('v2/bookings/',include("booking_v2.urls")),
]

