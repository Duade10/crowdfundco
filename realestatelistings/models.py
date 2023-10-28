from django.db import models
from users.models import User


class RealEstateListing(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=50, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("sold", "Sold"), ("pending", "Pending"), ("expired", "Expired")],
        default="active",
        blank=True,
        null=True,
    )
    real_estate_agent = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="listings"
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.title


class ExtraDocument(models.Model):
    DOCUMENT_TYPES = [
        ("deed", "Deed"),
        ("title insurance policy", "Title Insurance Policy"),
        ("property tax records", "Property Tax Records"),
        ("survey", "Survey"),
        ("mortgage documents", "Mortgage Documents"),
        ("homeowners association (hoa) records", "Homeowners Association (HOA) Records"),
        ("utility bills", "Utility Bills"),
        ("estate planning documents", "Estate Planning Documents"),
        ("affidavit of title", "Affidavit of Title"),
    ]

    listing = models.ForeignKey(
        RealEstateListing, on_delete=models.CASCADE, related_name="extra_documents", blank=True, null=True
    )
    document_type = models.CharField(choices=DOCUMENT_TYPES, blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="extra-document/", blank=True, null=True)

    def __str__(self):
        return f"{self.listing.title} - {self.document_type}"


class TokenDetail(models.Model):
    listing = models.OneToOneField(
        RealEstateListing, on_delete=models.CASCADE, related_name="token_detail", blank=True, null=True
    )
    inital_token_price = models.FloatField(blank=True, null=True)
    is_token_fractional = models.BooleanField(default=False)
    fractions = models.IntegerField(blank=True, null=True)


class Image(models.Model):
    listing = models.ForeignKey(
        RealEstateListing, on_delete=models.CASCADE, related_name="images", blank=True, null=True
    )
    file = models.ImageField(upload_to="realestatelistings/")
