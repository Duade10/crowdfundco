from django.db import models
from users.models import User
from categories.models import Category


class CrowdfundingCampaign(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    funding_target = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    categories = models.ManyToManyField(Category)
    organizer_profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class CampaignUpdate(models.Model):
    campaign = models.ForeignKey(CrowdfundingCampaign, on_delete=models.CASCADE)
    update_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.title
