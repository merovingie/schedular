# Generated by Django 2.1.7 on 2019-03-25 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedulerapi', '0003_auto_20190310_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='severity',
            field=models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
