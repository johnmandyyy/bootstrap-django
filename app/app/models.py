from django.db import models

# Default Python Models for Auto API

class RouteExclusion(models.Model):
    """Model for URL Routes"""
    required_token = models.BooleanField(default = False)
    route = models.CharField(unique=True, max_length=255)
    is_enabled = models.BooleanField(default = False)

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

# Address
class TableRegion(models.Model):
    region_name = models.CharField(unique=True, max_length=50)
    region_description = models.CharField(max_length=100)

    def __str__(self):
        return self.region_name


class TableProvince(models.Model):
    region = models.ForeignKey(TableRegion, on_delete=models.CASCADE)
    province_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["region"]),  # Index on ForeignKey field
        ]

    def __str__(self):
        return str(self.province_name)

class TableMunicipality(models.Model):
    province = models.ForeignKey(
        TableProvince, on_delete=models.CASCADE, blank=True, null=True
    )
    municipality_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.municipality_name

    class Meta:
        indexes = [
            models.Index(fields=["province"]),  # Index on ForeignKey field
        ]


class TableBarangay(models.Model):
    municipality = models.ForeignKey(TableMunicipality, on_delete=models.CASCADE)
    barangay_name = models.CharField(max_length=100)

    def __str__(self):
        return self.barangay_name

    class Meta:
        indexes = [
            models.Index(fields=["municipality"]),  # Index on ForeignKey field
        ]
