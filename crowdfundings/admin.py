from django.contrib import admin
from .models import CrowdfundingCampaign, CampaignUpdate, Contribution

admin.site.register(CrowdfundingCampaign)
admin.site.register(CampaignUpdate)
admin.site.register(Contribution)
