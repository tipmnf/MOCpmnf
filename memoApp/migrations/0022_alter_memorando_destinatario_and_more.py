# Generated by Django 4.2.2 on 2023-08-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('memoApp', '0021_alter_memorando_assunto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorando',
            name='destinatario',
            field=models.ManyToManyField(related_name='memorandos_recebidos', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='memorando',
            name='destinatarios_copia',
            field=models.ManyToManyField(null=True, related_name='destinatarios_copia', to='auth.group'),
        ),
    ]