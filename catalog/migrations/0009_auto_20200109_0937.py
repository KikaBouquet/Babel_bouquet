# Generated by Django 3.0.2 on 2020-01-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200108_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='century_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
