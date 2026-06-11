from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet,home,TestAuthView

router = DefaultRouter()

router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/',home),
     path('test-auth/', TestAuthView.as_view()),
]