# Generated by Django 3.2.9 on 2022-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginproject', '0002_rename_student_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
