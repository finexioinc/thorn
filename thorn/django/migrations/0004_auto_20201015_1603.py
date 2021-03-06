# Generated by Django 3.1.2 on 2020-10-15 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webhooks', '0003_auto_20171024_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='password',
            field=models.CharField(db_index=True, default='password', help_text='Basic Auth password', max_length=190, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='username',
            field=models.CharField(db_index=True, default='username', help_text='Basic Auth username', max_length=190, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='event',
            field=models.CharField(choices=[], db_index=True, help_text='Name of event to connect with', max_length=190, verbose_name='event'),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together={('event', 'user')},
        ),
    ]
