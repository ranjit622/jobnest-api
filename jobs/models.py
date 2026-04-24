from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):

    # Job ki details
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_url = models.URLField(blank=True)
    salary_expected = models.CharField(max_length=100, blank=True)

    # Status
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )

    # Interview details
    interview_date = models.DateField(null=True, blank=True)
    interview_time = models.TimeField(null=True, blank=True)
    interview_link = models.URLField(blank=True)

    # HR details
    hr_name = models.CharField(max_length=200, blank=True)
    hr_email = models.EmailField(blank=True)
    hr_phone = models.CharField(max_length=15, blank=True)

    # Notes
    notes = models.TextField(blank=True)

    # Dates
    applied_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.company} - {self.role} - {self.status}"

    class Meta:
        # Latest jobs pehle
        ordering = ['-applied_date']