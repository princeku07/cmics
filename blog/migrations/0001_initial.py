# Generated by Django 3.1.7 on 2021-04-18 18:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published', models.BooleanField(default=None)),
                ('category', models.CharField(default='', max_length=255)),
                ('snippet', models.CharField(default='click to read more', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-category'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('download', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published', models.BooleanField(default=True)),
                ('snippet', models.CharField(default='read more', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notes', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published', models.BooleanField(default=True)),
                ('pdf_file', models.FileField(default='', upload_to='documents')),
                ('snippet', models.CharField(default='click to read more', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published', models.BooleanField(default=True)),
                ('snippet', models.CharField(default='click to read more', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Vedios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='forumcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.forum')),
            ],
        ),
        migrations.CreateModel(
            name='commentblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('body', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Category'),
        ),
    ]
