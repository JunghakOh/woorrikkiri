# Generated by Django 2.2.4 on 2020-10-11 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(choices=[('computing', '컴퓨팅 사고력'), ('basicC', 'C언어 기초'), ('GC', '고급응용 C프로그래밍'), ('basicEngineering', '기초공학설계'), ('univMath', '대학수학'), ('principlesodEconomics1', '경제학원론1'), ('principlesodEconomics2', '경제학원론2')], max_length=30, verbose_name='과목')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField(default='')),
                ('coffee', models.IntegerField(default=0, verbose_name='커피')),
                ('file', models.FileField(blank=True, upload_to='documents/%Y, %m/')),
                ('respondent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respondent', to=settings.AUTH_USER_MODEL, verbose_name='답변자')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(choices=[('computing', '컴퓨팅 사고력'), ('basicC', 'C언어 기초'), ('GC', '고급응용 C프로그래밍'), ('basicEngineering', '기초공학설계'), ('univMath', '대학수학'), ('principlesodEconomics1', '경제학원론1'), ('principlesodEconomics2', '경제학원론2')], max_length=30, verbose_name='과목')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0, verbose_name='포인트')),
                ('account_num', models.IntegerField(blank=True, null=True, verbose_name='계좌번호')),
                ('bank', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='은행')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approve', models.BooleanField(default=False, verbose_name='결제승인')),
                ('point_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='포인트사용자', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(blank=True, upload_to='documents/%Y, %m/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Content')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
