# Generated by Django 4.2.6 on 2023-11-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户数据', 'verbose_name_plural': '用户数据'},
        ),
    ]
