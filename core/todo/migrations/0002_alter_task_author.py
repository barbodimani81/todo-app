# Generated by Django 3.2.25 on 2024-09-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
