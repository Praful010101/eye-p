# Generated by Django 3.2.7 on 2021-10-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostnames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('password', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
