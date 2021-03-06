# Generated by Django 3.0.5 on 2020-04-09 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'agile_principles',
                'ordering': ['order', 'name'],
            },
        ),
    ]
