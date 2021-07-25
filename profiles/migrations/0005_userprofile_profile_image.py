from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
