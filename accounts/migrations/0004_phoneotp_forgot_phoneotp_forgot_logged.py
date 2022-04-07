# Generated by Django 4.0.3 on 2022-04-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_phoneotp_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='forgot',
            field=models.BooleanField(default=False, help_text='only true for forgot password'),
        ),
        migrations.AddField(
            model_name='phoneotp',
            name='forgot_logged',
            field=models.BooleanField(default=False, help_text='Only true if validdate otp forgot get successful'),
        ),
    ]