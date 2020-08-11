# Generated by Django 2.2.13 on 2020-08-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
            ],
        ),
        migrations.AlterModelTable(
            name='person',
            table='book',
        ),
    ]
