# Generated by Django 3.0.7 on 2020-06-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AddField(
            model_name='search',
            name='location',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]