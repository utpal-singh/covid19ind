# Generated by Django 3.0.3 on 2020-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0026_auto_20200412_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_enquiry',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='userposts'),
        ),
    ]
