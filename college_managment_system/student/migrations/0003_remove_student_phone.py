# Generated by Django 4.1 on 2022-08-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_links_phone_links_email_links_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]