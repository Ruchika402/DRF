from rest_framework import serializers
from .models import Student,Teacher,Subject

class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields='__all__'