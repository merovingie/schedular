# Generated by Django 2.1.7 on 2019-03-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulerapi', '0002_auto_20190227_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='timeNow',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]