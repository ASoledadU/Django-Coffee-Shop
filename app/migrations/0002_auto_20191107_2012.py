# Generated by Django 2.2.5 on 2019-11-07 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='coffee',
            new_name='item',
        ),
    ]
