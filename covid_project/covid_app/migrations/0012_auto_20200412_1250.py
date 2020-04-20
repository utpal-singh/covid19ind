# Generated by Django 3.0.3 on 2020-04-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0011_auto_20200412_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_enquiry',
            name='feedback',
            field=models.CharField(db_index=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_enquiry',
            name='name',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_enquiry',
            name='suggestions',
            field=models.CharField(db_index=True, max_length=2000, null=True),
        ),
    ]
