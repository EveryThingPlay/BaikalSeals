# Generated by Django 3.2.7 on 2021-10-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_customuser_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
