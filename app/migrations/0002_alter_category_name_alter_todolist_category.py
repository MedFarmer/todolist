# Generated by Django 4.2.7 on 2023-12-01 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=30),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category'),
        ),
    ]
