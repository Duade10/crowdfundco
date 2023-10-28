from django.db import models
from users.models import User
from categories.models import Category
from realestatelistings.models import RealEstateListing


class CrowdfundingCampaign(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    funding_target = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="crowdfunding_campaign", blank=True, null=True
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    realestatelisting = models.OneToOneField(RealEstateListing, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Random"


class Contribution(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contributions", blank=True, null=True)
    no_of_token = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
    campaign = models.OneToOneField(CrowdfundingCampaign, on_delete=models.CASCADE, related_name="contributions")

    def __str__(self):
        return self.contributor.get_full_name()


class CampaignUpdate(models.Model):
    campaign = models.ForeignKey(
        CrowdfundingCampaign, related_name="updates", on_delete=models.CASCADE, blank=True, null=True
    )
    update_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.title
