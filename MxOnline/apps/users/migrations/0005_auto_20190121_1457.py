# Generated by Django 2.1.1 on 2019-01-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190115_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverifyrecord',
            old_name='emol',
            new_name='email',
        ),
    ]
