# Generated by Django 3.0.3 on 2020-04-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid_ind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.IntegerField(db_index=True, null=True)),
                ('active', models.IntegerField(db_index=True, null=True)),
            ],
        ),
    ]
