
# Create your models here.
from django.db import models


class CustomerInquiry(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    inquiry_type = models.CharField(
        max_length=50,
        choices=[
            ("home", "Home Supply"),
            ("office", "Office Supply"),
            ("distributor", "Distributor"),
        ],
        default="home"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name