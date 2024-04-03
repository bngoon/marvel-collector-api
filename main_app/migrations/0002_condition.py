# Generated by Django 5.0.3 on 2024-04-03 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Collected')),
                ('rating', models.CharField(choices=[('N', 'New'), ('F', 'Fair'), ('U', 'Used')], default='N', max_length=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.character')),
            ],
        ),
    ]