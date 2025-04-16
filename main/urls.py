from django.urls import path
from .views import TeacherViewSet, StudentViewSet, ClassViewSet

urlpatterns = [
    path('teachers/', TeacherViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('teachers/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'patch': 'partial_update', 'delete': 'destroy'})),
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'patch': 'partial_update', 'delete': 'destroy'})),
    path('classes/', ClassViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('classes/<int:pk>/', ClassViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'patch': 'partial_update', 'delete': 'destroy'})),
]