# Generated by Django 3.1.1 on 2020-09-16 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200916_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='overall_rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('type_of_review', models.CharField(choices=[('SR', 'Sender Review'), ('DR', 'Distributor Review')], max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
