# Generated by Django 3.2.6 on 2022-04-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Name')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('phone', models.BigIntegerField(verbose_name='Phone Number')),
                ('subject', models.CharField(max_length=250, verbose_name='Type of issues')),
                ('description', models.TextField(verbose_name='Issue Description')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
            ],
        ),
    ]
