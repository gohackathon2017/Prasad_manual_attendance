# Generated by Django 5.0.7 on 2024-11-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phase1', '0002_biochemistry_communitymedicine_eca_foundationcourse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase1student',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
