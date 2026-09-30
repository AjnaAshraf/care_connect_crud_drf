from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer



# Create your view

class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request):

        qs = Doctor.objects.all()

        serializer_instance = DoctorSerializer(qs,many = True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Doctor.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

class DoctorRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk = None):

        qs = Doctor.objects.get(id=pk)

        serializer_instance = DoctorSerializer(qs)

        return Response(data=serializer_instance.data)

    def delete(self,request,pk=None):

        qs = Doctor.objects.get(id=pk).delete()

        return Response(data={"message":"deleted....."})

    def put(self,request,pk=None):

        form_data =request.data

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Doctor.objects.filter(id=pk).update(**cleaned_data)

            return Response(data= cleaned_data)

        else:

            return Response(data= serializer_instance.errors)


class AdminRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            # User.objects.create(**cleaned_data)  --- this will create a user but encrption of password doesnt take place
            # User.objects.create_user(**cleaned_data) --this will create a user ,password is encrypted but it will not be admin 
            User.objects.create_superuser(**cleaned_data) #password encrpted ,admin created 

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)
            

            