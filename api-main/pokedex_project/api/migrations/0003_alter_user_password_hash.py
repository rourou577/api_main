# Generated by Django 4.2.11 on 2024-04-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_last_login_alter_user_password_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(default='pbkdf2_sha256$600000$ionfTkuqJZwZKMlACIIWbR$oDLdDzLrxlFoqtyZmUej0ClCo2bCK96fP4UslJBK0ek=', max_length=255),
        ),
    ]