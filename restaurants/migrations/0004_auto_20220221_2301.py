# Generated by Django 3.2.12 on 2022-02-22 05:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='max_num_purchases',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('available', models.BooleanField(default=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
