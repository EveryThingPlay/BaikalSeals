# Generated by Django 3.2.7 on 2021-10-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20211002_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation_request',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vacation_request',
            name='worker',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
