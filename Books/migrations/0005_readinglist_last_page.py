# Generated by Django 3.1.5 on 2021-01-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_auto_20210108_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinglist',
            name='last_page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
