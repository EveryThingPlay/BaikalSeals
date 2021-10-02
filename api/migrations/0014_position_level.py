# Generated by Django 3.2.7 on 2021-10-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_customuser_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='level',
            field=models.CharField(blank=True, choices=[('1', 'junior'), ('2', 'middle'), ('3', 'senior'), ('4', 'teamlead')], max_length=10),
        ),
    ]
