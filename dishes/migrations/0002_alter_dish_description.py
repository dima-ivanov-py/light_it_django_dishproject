# Generated by Django 3.2.5 on 2021-08-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dishes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(
                blank=True, default="The dish description", max_length=200
            ),
            preserve_default=False,
        ),
    ]