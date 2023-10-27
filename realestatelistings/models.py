from django.db import models
from users.models import User


class RealEstateListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    features = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("sold", "Sold"), ("pending", "Pending"), ("expired", "Expired")],
        default="active",
    )
    real_estate_agent = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="listings"
    )
    slug = models.SlugField(unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
