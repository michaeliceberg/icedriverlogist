# Generated by Django 3.2.9 on 2022-04-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_weights_car_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='weights',
            name='PBA',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
