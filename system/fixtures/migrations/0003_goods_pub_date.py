# Generated by Django 2.0.6 on 2018-06-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0002_auto_20180620_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]