# Generated by Django 4.1.7 on 2023-05-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoApp', '0003_alter_memorando_corpo_memorando'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorando',
            name='memo_numero',
            field=models.CharField(max_length=220),
        ),
    ]