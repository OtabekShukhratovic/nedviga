# Generated by Django 4.1.3 on 2023-02-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0014_house_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
