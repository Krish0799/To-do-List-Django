# Generated by Django 4.1.7 on 2023-03-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoLi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctname', models.CharField(max_length=10)),
                ('ctDetails', models.CharField(max_length=100)),
            ],
        ),
    ]
