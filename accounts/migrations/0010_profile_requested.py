# Generated by Django 3.1.2 on 2022-05-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='requested',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
