# Generated by Django 3.0.3 on 2020-04-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0009_auto_20200412_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=1000, null=True)),
                ('suggestions', models.CharField(blank=True, db_index=True, max_length=2000, null=True)),
                ('date_time', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
        ),
    ]
