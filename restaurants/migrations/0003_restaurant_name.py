# Generated by Django 3.2.12 on 2022-02-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20220221_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
