# Generated by Django 2.1.1 on 2019-05-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='后端开发', max_length=30, verbose_name='课程类别'),
        ),
    ]
