# Generated by Django 3.0.5 on 2020-05-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_auto_20200418_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
