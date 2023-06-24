from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class StudentApi(APIView):
    def get(self,request,id=None):
                if id==None:    
                    stu=Student.objects.all()
                    serilizer=StudentSerializer(stu,many=True)
                    return Response(serilizer.data)
                else:
                    stu=Student.objects.get(id=id)
                    serilizer=StudentSerializer(stu)
                    return Response(serilizer.data)

    def post(self,request):
            serilizer=StudentSerializer(data=request.data)
            if serilizer.is_valid():
                serilizer.save()
            return  Response(serilizer.data)
    
    def put(self,request,id):
            stu=Student.objects.get(id=id)
            serilizer=StudentSerializer(stu,data=request.data)
            if serilizer.is_valid():
                serilizer.save()
                return Response({'msg':'data updated sucessfully'})
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
          stu=Student.objects.filter(id=id).delete()
          return Response({'msg':'data deleted sucessfully'})