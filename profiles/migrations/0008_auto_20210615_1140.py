from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210615_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default="{% static '/media/default.jpg' %}", null=True, upload_to=''),
        ),
    ]
