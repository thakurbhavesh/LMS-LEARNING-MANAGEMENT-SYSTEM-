# Generated by Django 3.1.4 on 2021-01-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210104_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=254, primary_key='true', serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('regdate', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]