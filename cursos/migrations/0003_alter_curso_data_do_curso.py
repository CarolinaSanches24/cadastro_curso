# Generated by Django 4.2.10 on 2024-02-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='data_do_curso',
            field=models.DateField(help_text='aaaa-mm-dd'),
        ),
    ]