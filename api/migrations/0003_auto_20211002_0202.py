# Generated by Django 3.2.7 on 2021-10-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211002_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='employment',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastChanged',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='workStart',
            field=models.DateField(null=True),
        ),
    ]
