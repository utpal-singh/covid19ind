# Generated by Django 3.0.3 on 2020-04-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0030_covid_data_anal_states_conf_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_enquiry',
            name='suggestions_not_mandatory',
            field=models.CharField(blank=True, db_index=True, default='Hey', max_length=2000, null=True),
        ),
    ]
