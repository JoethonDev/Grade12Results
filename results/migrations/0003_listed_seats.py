# Generated by Django 4.2.4 on 2024-07-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_rename_results_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='listed_seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=300)),
                ('chat_id', models.IntegerField()),
            ],
        ),
    ]