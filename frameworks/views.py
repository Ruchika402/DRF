from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

from django.http import JsonResponse

def home(request):
    data = {
        "message": "Hello World"
    }
    return JsonResponse(data)