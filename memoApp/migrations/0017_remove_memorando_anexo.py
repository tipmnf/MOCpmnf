# Generated by Django 4.1.7 on 2023-07-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memoApp', '0016_memorando_anexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memorando',
            name='anexo',
        ),
    ]
