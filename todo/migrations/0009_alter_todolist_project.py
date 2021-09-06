# Generated by Django 3.2.6 on 2021-08-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
        ('todo', '0008_todolist_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist', to='projectapp.project'),
        ),
    ]
