from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
