# Generated by Django 4.1.7 on 2023-03-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_students_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='imag',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]