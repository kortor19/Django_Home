# Generated by Django 2.0.6 on 2019-06-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20190624_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneno',
            field=models.CharField(max_length=11),
        ),
    ]
