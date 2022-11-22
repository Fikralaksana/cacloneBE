# Generated by Django 4.1.3 on 2022-11-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_language_remove_course_language_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='type',
            field=models.CharField(choices=[('console', 'console'), ('browser', 'browser')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]