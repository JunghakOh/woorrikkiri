# Generated by Django 2.2.4 on 2020-09-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='account_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='계좌번호'),
        ),
    ]
