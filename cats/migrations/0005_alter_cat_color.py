# Generated by Django 3.2 on 2023-01-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_cat_achievements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Черный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]