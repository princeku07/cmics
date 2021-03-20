# Generated by Django 3.1.7 on 2021-03-08 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=100)),
                ('answer', models.IntegerField()),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('option_three', models.CharField(blank=True, max_length=100)),
                ('option_four', models.CharField(blank=True, max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.course')),
            ],
        ),
    ]
