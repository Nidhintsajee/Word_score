# Generated by Django 2.2 on 2022-02-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_str', models.CharField(max_length=50)),
                ('sum_score', models.IntegerField()),
            ],
        ),
    ]
