# Generated by Django 3.2.5 on 2021-09-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp', '0004_alter_t_user_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_user',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
