# Generated by Django 3.1.4 on 2023-03-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20230327_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('problem', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cus_service',
        ),
    ]