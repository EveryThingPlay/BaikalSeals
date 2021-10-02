# Generated by Django 3.2.7 on 2021-10-02 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_solved_requesst_approved'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='requesst',
            new_name='finrequest',
        ),
        migrations.CreateModel(
            name='vacation_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(null=True)),
                ('last_date', models.DateField(null=True)),
                ('price', models.FloatField(null=True)),
                ('approved', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
