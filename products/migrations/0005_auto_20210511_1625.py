from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210509_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
    ]
