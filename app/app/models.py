"""
Definition of models.
"""

from django.db import models

# Create your models here.

class AppLogs(models.Model):
    
    time_stamp = models.TextField(default = None)
    log_type = models.TextField(default = None)
    source = models.TextField(default = None)
    message = models.TextField(default = None)
    user_id = models.TextField(default = None)
    session_id = models.TextField(default = None)
    ip_address = models.TextField(default = None)
    request_method = models.TextField(default = None)
    request_path = models.TextField(default = None)
    response_status = models.TextField(default = None)
    data = models.TextField(default = None)
    error_type = models.TextField(default = None)
    error_message = models.TextField(default = None)
    stack_tace = models.TextField(default = None)
    execution_time = models.FloatField(default = 0.00)

class Categories(models.Model):
    category_name = models.TextField()

class Reports(models.Model):
    accuracy = models.TextField()
    precision = models.TextField()
    recall = models.TextField()
    f1_score = models.TextField()


