# Generated by Django 4.2.3 on 2023-08-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondApp', '0002_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subheading', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
