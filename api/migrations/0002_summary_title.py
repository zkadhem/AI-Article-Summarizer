# Generated by Django 3.1.6 on 2021-02-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
