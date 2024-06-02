"""
Definition of models.
"""

from django.db import models

# Create your models here.


class AppLogs(models.Model):
    time_stamp = models.TextField(default=None, null=True, blank=True)
    log_type = models.TextField(default=None, null=True, blank=True)
    level = models.TextField(default=None, null=True, blank=True)
    source = models.TextField(default=None, null=True, blank=True)
    message = models.TextField(default=None, null=True, blank=True)
    user_id = models.TextField(default=None, null=True, blank=True)
    session_id = models.TextField(default=None, null=True, blank=True)
    ip_address = models.TextField(default=None, null=True, blank=True)
    request_method = models.TextField(default=None, null=True, blank=True)
    request_path = models.TextField(default=None, null=True, blank=True)
    response_status = models.TextField(default=None, null=True, blank=True)
    data = models.TextField(default=None, null=True, blank=True)
    error_type = models.TextField(default=None, null=True, blank=True)
    error_message = models.TextField(default=None, null=True, blank=True)
    stack_trace = models.TextField(default=None, null=True, blank=True)
    execution_time = models.FloatField(default=0.00, null=True, blank=True)

class Categories(models.Model):
    category_name = models.TextField()

class Reports(models.Model):
    accuracy = models.TextField()
    precision = models.TextField()
    recall = models.TextField()
    f1_score = models.TextField()


