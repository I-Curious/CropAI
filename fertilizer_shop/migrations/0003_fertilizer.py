# Generated by Django 2.1.5 on 2019-03-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fertilizer_shop', '0002_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
