# Generated by Django 4.2.5 on 2023-09-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('Age', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]