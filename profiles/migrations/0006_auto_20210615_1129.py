from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
