from rest_framework import serializers
from .models import Student,Teacher,Subject,Book

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

class BookListSerializer(serializers.ListSerializer):
    def validate(self, data):
        if len(data) > 10: 
            raise serializers.ValidationError("Too many books!")
        return data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
        list_serializer_class = BookListSerializer  