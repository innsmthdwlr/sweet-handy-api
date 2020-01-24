# Generated by Django 3.0.2 on 2020-01-24 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='contents',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='imagelink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='timeofmeal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofmeasurement', models.DateTimeField(blank=True, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal')),
            ],
        ),
    ]