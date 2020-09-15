# Generated by Django 2.2.4 on 2020-09-14 10:49

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
                ('subjects', models.CharField(choices=[('computing', '컴퓨팅 사고력'), ('basicC', '기초 C언어'), ('GC', '고급응용 C프로그래밍'), ('math', '응용수학')], max_length=30, verbose_name='과목')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(choices=[('computing', '컴퓨팅 사고력'), ('basicC', '기초 C언어'), ('GC', '고급응용 C프로그래밍'), ('math', '응용수학')], max_length=30, verbose_name='과목')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField(default='')),
                ('file', models.FileField(blank=True, upload_to='documents/%Y, %m/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
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
