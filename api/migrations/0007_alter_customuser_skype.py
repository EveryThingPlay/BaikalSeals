# Generated by Django 3.2.7 on 2021-10-01 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='skype',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
