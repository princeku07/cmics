# Generated by Django 3.1.7 on 2021-03-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210308_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
