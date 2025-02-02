# Generated by Django 3.2.16 on 2023-12-06 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_auto_20231206_0307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='congratulation',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='congratulation',
            name='birthday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday.birthday', verbose_name='congratulation'),
        ),
    ]
