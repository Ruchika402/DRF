from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
#from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import StudentPagination
from .throttles import StudentThrottle

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    throttle_classes = [StudentThrottle]
    
    #permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ['city', 'course']

    search_fields = ['name']

    ordering_fields = ['age']

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

from django.http import JsonResponse

def home(request):
    data = {
        "message": "Hello World"
    }
    return JsonResponse(data)



