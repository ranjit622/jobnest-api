from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = [
            'id',
            'company',
            'role',
            'location',
            'job_url',
            'salary_expected',
            'status',
            'interview_date',
            'interview_time',
            'interview_link',
            'hr_name',
            'hr_email',
            'hr_phone',
            'notes',
            'applied_date',
            'updated_at',
        ]
        read_only_fields = ['applied_date', 'updated_at']