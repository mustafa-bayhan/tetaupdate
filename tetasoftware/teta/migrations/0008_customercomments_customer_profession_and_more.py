# Generated by Django 4.0.2 on 2022-08-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teta', '0007_job_alter_post_image_alter_website_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercomments',
            name='customer_profession',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customercomments',
            name='website_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customercomments',
            name='website_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
