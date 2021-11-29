# Generated by Django 3.2.8 on 2021-11-17 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20211116_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='blockchain',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='denuncia',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]