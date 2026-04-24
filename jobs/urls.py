from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet, register, dashboard

router = DefaultRouter()
router.register('applications', JobApplicationViewSet, basename='jobapplication')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),

]