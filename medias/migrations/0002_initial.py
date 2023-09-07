# Generated by Django 4.2.3 on 2023-08-02 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medias",
                to="rooms.room",
            ),
        ),
    ]
