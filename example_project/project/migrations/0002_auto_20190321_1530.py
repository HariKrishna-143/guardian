# Generated by Django 2.1.1 on 2019-03-21 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('project_task', 'project Task'),)},
        ),
    ]
