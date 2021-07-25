from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210615_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
    ]
