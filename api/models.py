from django.db import models


class Dispensary(models.Model):
    licence_type = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    dba = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)
    email = models.EmailField()
    hours_of_operation = models.CharField(max_length=255)
    expiration_date = models.DateField()
    website = models.URLField()
    business_owner = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
