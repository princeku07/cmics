# Generated by Django 3.1.7 on 2021-03-14 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210313_2202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comment',
        ),
    ]
