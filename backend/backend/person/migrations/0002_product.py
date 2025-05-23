# Generated by Django 5.1.7 on 2025-03-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='img')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
