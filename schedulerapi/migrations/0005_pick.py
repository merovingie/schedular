# Generated by Django 2.1.7 on 2019-03-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulerapi', '0004_item_severity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayDate', models.DateTimeField(auto_now_add=True)),
                ('itemA', models.CharField(max_length=32)),
                ('isDoneA', models.BooleanField(default=False)),
                ('itemB', models.CharField(max_length=32)),
                ('isDoneB', models.BooleanField(default=False)),
                ('itemC', models.CharField(max_length=32)),
                ('isDoneC', models.BooleanField(default=False)),
            ],
        ),
    ]
