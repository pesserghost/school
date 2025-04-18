from rest_framework.viewsets import ModelViewSet
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer