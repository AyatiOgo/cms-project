# Generated by Django 5.1.7 on 2025-04-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0003_alter_doctors_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=''),
        ),
    ]
