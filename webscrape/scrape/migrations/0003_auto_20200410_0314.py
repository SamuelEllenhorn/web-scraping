# Generated by Django 3.0.4 on 2020-04-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0002_auto_20200408_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]