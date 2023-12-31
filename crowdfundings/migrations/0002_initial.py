# Generated by Django 4.2.6 on 2023-10-28 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crowdfundings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="crowdfundingcampaign",
            name="organizer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="crowdfundingcampaign",
            name="organizer_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="crowdfundings_campaingns",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="campaign",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to="crowdfundings.crowdfundingcampaign",
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="contributor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="campaignupdate",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="updates",
                to="crowdfundings.crowdfundingcampaign",
            ),
        ),
    ]
