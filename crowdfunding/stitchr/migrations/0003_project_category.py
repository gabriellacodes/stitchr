# Generated by Django 3.0.8 on 2020-08-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stitchr', '0002_auto_20200828_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
    ]