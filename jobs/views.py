from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['company', 'role']
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username pehle se hai!"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(
        username=username,
        password=password
    )
    
    return Response(
        {"message": f"Register ho gaya — {username}!"},
        status=status.HTTP_201_CREATED
    )
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard(request):
    user = request.user
    
    total = JobApplication.objects.filter(user=user).count()
    applied = JobApplication.objects.filter(user=user, status='applied').count()
    interview = JobApplication.objects.filter(user=user, status='interview').count()
    selected = JobApplication.objects.filter(user=user, status='selected').count()
    rejected = JobApplication.objects.filter(user=user, status='rejected').count()
    
    return Response({
        "total_applications": total,
        "applied": applied,
        "interview_scheduled": interview,
        "selected": selected,
        "rejected": rejected,
    })