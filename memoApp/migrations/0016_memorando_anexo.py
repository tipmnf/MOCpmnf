# Generated by Django 4.1.7 on 2023-07-18 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoApp', '0015_rename_ofício_oficio'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorando',
            name='anexo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anexo_recebido', to='memoApp.image'),
        ),
    ]