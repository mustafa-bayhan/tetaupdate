# Generated by Django 4.0.2 on 2022-08-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teta', '0016_alter_post_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='month',
            field=models.CharField(choices=[('ocak', 'OCAK'), ('subat', 'ŞUBAT'), ('mart', 'MART'), ('nisan', 'NİSAN'), ('mayis', 'MAYIS'), ('haziran', 'HAZİRAN'), ('temmuz', 'TEMMUZ'), ('AĞUSTOS', 'AĞUSTOS'), ('eylül', 'EYLÜL'), ('ekim', 'EKİM'), ('kasim', 'KASIM'), ('aralik', 'ARALIK')], default='NONE', max_length=200),
        ),
    ]
