# Generated by Django 3.1.5 on 2021-01-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210114_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]
