# Generated by Django 4.1.4 on 2022-12-17 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newsapi", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Question",
        ),
    ]