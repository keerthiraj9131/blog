# Generated by Django 3.1.3 on 2021-06-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20210530_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=256),
        ),
    ]