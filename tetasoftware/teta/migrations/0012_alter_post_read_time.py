# Generated by Django 4.0.2 on 2022-08-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teta', '0011_post_read_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.CharField(default='5 dk', max_length=10, null=True),
        ),
    ]
