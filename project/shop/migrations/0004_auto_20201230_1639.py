from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201228_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('New', 'New'), ('Bestseller', 'Bestseller'), ('Trending', 'Trending'), ('Featured', 'Featured'), ('Sale', 'Sale')], default='New', max_length=20),
        ),
    ]
