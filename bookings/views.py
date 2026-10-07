from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer
from staff.models import Doctor
# Create your views here.

class AppointmentsCreateListView(APIView):

    def get(self,request):

        qs = Appointment.objects.all()

        serializer_instance = AppointmentSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = AppointmentSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            """

            cleaned_data ={
                "patient_name":"sanya",
                "phone":"9876789765",
                "doctor":2,
                "appointment_date":"2025-10-01",
                "problem":"wheezing"
            }
            """

            doctor = cleaned_data.get("doctor")

            appointment_date = cleaned_data.get("appointment_date")

            last_appointment_object = Appointment.objects.filter(doctor=doctor,appointment_date = appointment_date).last()

            # new_token = 0

            if last_appointment_object:

                new_token=last_appointment_object.token_number+1

            else:

                new_token=1

            doctor_object = Doctor.objects.get(id=doctor)

            cleaned_data["doctor"] = doctor_object

            Appointment.objects.create(**cleaned_data,token_number=new_token)

            response_data = {

                "status ":"booked",
                "token_number":new_token

            }

            return Response(data=response_data)

        else:

            return Response(data=serializer_instance.errors)

        

            

