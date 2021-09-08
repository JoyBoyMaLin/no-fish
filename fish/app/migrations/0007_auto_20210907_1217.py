# Generated by Django 3.2.6 on 2021-09-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210906_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='content',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='title',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='show_home',
        ),
        migrations.AddField(
            model_name='detail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/images/photos/', verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='DetailImage',
        ),
    ]
