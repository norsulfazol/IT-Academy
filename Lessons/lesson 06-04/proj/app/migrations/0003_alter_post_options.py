# Generated by Django 3.2.3 on 2021-06-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210524_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_post', 'Can add post'), ('can_manage_post', 'Can manage post'))},
        ),
    ]
