# Generated by Django 4.1.3 on 2022-11-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JustInTime', '0008_remove_devicehistoric_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicehistoric',
            name='id_device',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='devicehistoric',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
