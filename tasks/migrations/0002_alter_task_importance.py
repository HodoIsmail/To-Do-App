# Generated by Django 4.2.16 on 2024-12-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.IntegerField(choices=[(0, 'LOW'), (1, 'MEDIUM'), (2, 'HIGH')], default=2),
        ),
    ]
