# Generated by Django 5.0.6 on 2024-07-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('STUDEMT', 'STUDENT'), ('CLIENT', 'client'), ('SALESMAN', 'SALESMAN'), ('ADMIN', 'admin')], max_length=30),
        ),
    ]