# Generated by Django 4.1 on 2022-08-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
        ),
    ]
