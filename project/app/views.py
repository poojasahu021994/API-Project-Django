from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,JsonResponse
from .serializers import Stu_serializers
from rest_framework.renderers import JSONRenderer
def landingpage(request):
    return render(request,'landingpage.html')

def stu_list(request):
    stu=Student.objects.all()
    print(stu)
    serializer= Stu_serializers(stu,many=True)
    print("Serializer=",serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print("json_data=",json_data)
    return HttpResponse(json_data,content_type='application/json')



# Create your views here.
