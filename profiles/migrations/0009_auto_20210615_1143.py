from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210615_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='https://newirishlife.s3.eu-west-1.amazonaws.com/static/media/default.jpg', null=True, upload_to=''),
        ),
    ]
