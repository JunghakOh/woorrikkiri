# Generated by Django 3.0.8 on 2020-08-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='전화번호'),
        ),
    ]
