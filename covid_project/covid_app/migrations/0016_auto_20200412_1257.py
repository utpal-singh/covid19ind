# Generated by Django 3.0.3 on 2020-04-12 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0015_auto_20200412_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback_enquiry',
            old_name='name_madatory',
            new_name='name_mandatory',
        ),
    ]
