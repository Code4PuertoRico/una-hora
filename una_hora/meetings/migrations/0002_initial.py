# Generated by Django 3.2.5 on 2021-09-13 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("meetings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="canceled_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
                verbose_name="canceled by user",
            ),
        ),
        migrations.AddField(
            model_name="meeting",
            name="mentee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meetings_as_mentee",
                related_query_name="mentee_meeting",
                to=settings.AUTH_USER_MODEL,
                verbose_name="mentee",
            ),
        ),
        migrations.AddField(
            model_name="meeting",
            name="mentor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meetings_as_mentor",
                related_query_name="mentor_meeting",
                to=settings.AUTH_USER_MODEL,
                verbose_name="mentor",
            ),
        ),
    ]
