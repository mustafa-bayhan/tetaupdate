# Generated by Django 4.0.2 on 2022-08-21 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teta', '0013_about_detail_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='right_1_detail',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_1_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_2_detail',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_2_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_3_detail',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_3_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_4_detail',
        ),
        migrations.RemoveField(
            model_name='about',
            name='right_4_title',
        ),
    ]
