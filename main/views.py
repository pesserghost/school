from rest_framework.viewsets import ModelViewSet
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer
from .permissions import IsSuperUserOrReadOnly, IsAuthenticatedAndCanComment


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedAndCanComment]