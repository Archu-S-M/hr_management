from django.db import models
from datetime import datetime
from django.utils import timezone
from Admin_Management.models import CustomUser
# Create your models here.


# Candidate profile model
class Candidate(models.Model):
    consultancy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100, null=False)
    candidate_email = models.CharField(max_length=120, null=False)
    candidate_resume = models.CharField(max_length=100, null=False)
    candidate_contact_no = models.CharField(max_length=15, null=False)
    candiate_interview_time = models.DateTimeField(null=False, default=timezone.now)
    candidate_status = models.CharField(max_length=10, null=True)


# candidate skill set model
class Skillset(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    candidate_skill = models.CharField(max_length=50, null=True)


# hr requirements model
class Requirements(models.Model):
    requirement_name = models.CharField(max_length=300, null=False)
    requirement_status =  models.BooleanField(default=1)



# Interview questions model
class Questions(models.Model):
    requirements = models.ForeignKey(Requirements, on_delete=models.CASCADE)
    question = models.CharField(max_length=500, null=False)
    question_status = models.BooleanField(default=1)