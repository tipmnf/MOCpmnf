# Generated by Django 4.1.7 on 2023-07-04 19:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memoApp', '0010_memorando_destinatario_copia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memorando',
            name='destinatario_copia',
        ),
        migrations.AddField(
            model_name='memorando',
            name='destinatarios_copia',
            field=models.ManyToManyField(null=True, related_name='destinatarios_copia', to=settings.AUTH_USER_MODEL),
        ),
    ]
