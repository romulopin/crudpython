# Generated by Django 2.2.4 on 2019-08-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuaplicativo', '0005_auto_20190813_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='produto_vendido',
            field=models.ManyToManyField(to='meuaplicativo.Produto'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='cpf',
            field=models.IntegerField(),
        ),
    ]
