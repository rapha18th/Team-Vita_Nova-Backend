# Generated by Django 3.1.1 on 2020-09-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200916_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='type_of_review',
            field=models.CharField(choices=[('Sender Review', 'Sender Review'), ('Distributor Review', 'Distributor Review')], max_length=100),
        ),
    ]
