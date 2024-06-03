from django.db import models

class RouteExclusion(models.Model):
    """Model for URL Routes"""
    route = models.CharField(unique=True, max_length=255)
    is_enabled = models.BooleanField(default = True)

    def __str__(self):
        remarks = ""
        if self.is_enabled == True:
            remarks = "Enabled"
        else:
            remarks = "Disabled"

        return remarks + " : " + self.route

class AppLogs(models.Model):
    """Model for application logs, whether API Level or Function Level"""
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
    execution_time = models.TextField(default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.time_stamp}"
    
class StackTrace(models.Model):
    app_log = models.ForeignKey(AppLogs, on_delete=models.CASCADE)
    description = models.TextField()

class Categories(models.Model):
    category_name = models.TextField()

class Reports(models.Model):
    accuracy = models.TextField()
    precision = models.TextField()
    recall = models.TextField()
    f1_score = models.TextField()
