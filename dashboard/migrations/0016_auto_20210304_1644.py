# Generated by Django 3.1.6 on 2021-03-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_cv2_profileareaofexpertisecv2_profileawardscv2_profilebooksauthoredcv2_profilecertificatecv2_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiletitlecv2',
            old_name='titlecv2',
            new_name='titcv2',
        ),
    ]
