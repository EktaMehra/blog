# Generated by Django 5.1.4 on 2025-01-05 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_post_field_2_post_field_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]